from pydub import AudioSegment
import sys
from ffprobe import FFProbe
import soundfile as sf


AudioSegment.converter = '/Users/admin/Documents/data-science/10-spotify-genre-classifier/ffmpeg/bin/ffmpeg'
AudioSegment.ffmpeg = '/Users/admin/Documents/data-science/10-spotify-genre-classifier/ffmpeg/bin/ffmpeg'
AudioSegment.ffprobe ='/Users/admin/Documents/data-science/10-spotify-genre-classifier/ffmpeg/bin/ffprobe'


for x in range(1,10418):
    print(int(x/10418*10000)/100,x)
    try:
        origin = 'songs/' + str(x) + '.mp3'
        destination = 'wav/' + str(x) + '.wav'
        song = AudioSegment.from_mp3(origin)
        song.export(destination, format="wav")
    except:
        print("no file")