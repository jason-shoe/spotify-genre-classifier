import urllib.request
import pandas as pd

songlist = pd.read_csv('../data/songlist.csv')
print(songlist)

for index, row in songlist.iterrows():
    print(row['songURL'])
    if(not pd.isna(row['songURL'])):
        print(int(index/len(songlist)*10000)/100)
        url = row['songURL']
        name = 'songs/'+str(index)+'.mp3'
        urllib.request.urlretrieve(url, name)