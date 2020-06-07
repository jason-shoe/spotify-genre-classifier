import spotipy
import pandas as pd
import seaborn as sns
import statistics 
import re
import string
from bs4 import BeautifulSoup
from PIL import Image
import requests
from io import BytesIO
from numpy import asarray
import numpy as np

if __name__ == "__main__":
    imageDataframe = pd.DataFrame(columns = np.arange(12288))
    songDataframe = pd.read_csv('../data/songlist.csv')
    URL = songDataframe.loc[0,'lyricsURL']
    for index,row in songDataframe.iterrows():
        print(int(index/len(songDataframe)*10000)/100,"% - ",row['songName']," - ",row['imageURL'])
        response = requests.get(row['imageURL'])
        image = Image.open(BytesIO(response.content))
        data = asarray(image)
        try:
            dataResized = np.resize(data,(12288,))
        except:
            dataResized = np.zeros((12288,))
        imageDataframe = imageDataframe.append(pd.DataFrame(dataResized).T)
    imageDataframe.to_csv('../data/onlyImageFeatures.csv')
    print(imageDataframe)
    
    final = pd.concat([songDataframe, imageDataframe], axis=1)
    
    final.to_csv('../data/imageSongList.csv')




