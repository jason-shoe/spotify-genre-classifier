import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statistics 
import re
import string

def get_playlist_tracks(username,playlist_id):
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

if __name__ == "__main__":
    
    regex = re.compile(".*?\((.*?)\)")
    client_id = "dd555e5dcb514c99bd5674e226882fcf"
    client_secret = "c185e52e743d4b6a9e14247aea41beb8"
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API
    df = pd.read_csv('data/playlists.csv')
    counts = {'Hip-Hop':0,'Pop':0,'Country':0,'R&B':0,'Dance/Electronic':0}
    songDataframe = pd.DataFrame(columns=['genre','songName','artistName','imageURL','songURL','lyricsURL'])
    for index, row in df.iterrows():
        a = get_playlist_tracks(row['Creator'],row['URI'])
        counts[row['Genre']] += len(a)
        print(int(index/len(df)*10000)/100, row['Playlist Name'])
        for x in a:
            try:
                # print("\t" + x['track']['name'])
                val = re.findall(regex, x['track']['name'])
                songname = re.sub(r'\(.*\)', '', x['track']['name']).translate(str.maketrans('', '', string.punctuation)).strip().replace(' ', '-')
                artistname = x['track']['artists'][0]['name'].translate(str.maketrans('', '', string.punctuation)).strip().replace(' ', '-')
                geniusurl = 'https://genius.com/{}-{}-lyrics'.format(
                    artistname, songname)
                # print("\t\t" + geniusurl)
                # print("\t\t" + x['track']['artists'][0]['name'])
                # print("\t\t" + x['track']['album']['images'][0]['url'])
                songDataframe.loc[len(songDataframe)] = [row['Genre'], x['track']['name'], x['track']['artists'][0]['name'], x['track']['album']['images'][2]['url'],x['track']['preview_url'], geniusurl]
            except:
                print("didn't work")
    print(counts)
    songDataframe.to_csv('data/songlist.csv')
