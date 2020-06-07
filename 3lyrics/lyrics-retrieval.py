import spotipy
import pandas as pd
import seaborn as sns
import statistics 
import re
import string
from bs4 import BeautifulSoup
import requests

def get_lyrics(URL):
    page = requests.get(URL)
    html = BeautifulSoup(page.text, "html.parser") # Extract the page's HTML as a string
    lyrics = html.find("div", class_="lyrics")
    if(lyrics is None):
        return ""
    return lyrics.get_text()

if __name__ == "__main__":
    
    songDataframe = pd.read_csv('data/newSongList.csv')
    URL = songDataframe.loc[0,'lyricsURL']
    for index,row in songDataframe.iterrows():
        if(pd.isna(row['lyrics'])):
            print(int(index/len(songDataframe)*10000)/100,"% - ",row['songName']," - not filled")
            songDataframe.loc[index,'lyrics'] = get_lyrics(row['lyricsURL'])
        else:
            print(int(index/len(songDataframe)*10000)/100,"% - ",row['songName']," - filled")
    songDataframe.to_csv('../data/newSongList.csv')
        

