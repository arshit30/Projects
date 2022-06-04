import regex as re
import moviepy.editor as mp
from google.cloud import speech
import os
import io
import datetime

def subtitle_data(file):

    time_pattern = r'(\d{2}:\d{2}:\d{2},d{3}$)|(\d{2}:\d{2}:\d{2})'
    timings=[]
    dialogues=[]

    with open(file,'r',encoding='utf-8') as f:
        text = f.readlines()
        for line in text:
            if re.match(time_pattern, line):
                timings.append(line)
            elif re.match(r'\p{L}',line,re.UNICODE):
                dialogues.append(line.strip())
    
    os.remove(file)
    
    return timings,dialogues

def extract(file):

    video=mp.AudioFileClip(file)
    duration=int(video.duration)
    for i in range(0,duration-3,3):
        clip=video.subclip(i,i+3)
        clip.write_audiofile('./clips/'+str(i//3)+'.wav')
    return duration
    
def transcribe(file,language):
    
    timings=[]
    dialogues=[]
    languages={}
    languages['English']='en-US'
    languages['French']='fr-FR'
    languages['Japanese']='ja-JP'
    languages['Chinese']='zh'
    languages['Korean']='ko-KR'
    languages['German']='de-DE'
    languages['Spanish']='es-ES'
    
    client=speech.SpeechClient()
    
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#        sample_rate_hertz=16000,
        language_code=languages[language],
	audio_channel_count=2
    )
    
    duration= extract(file)
    
    for i in range(0,duration-3,3):

        with io.open('./clips/'+str(i//3)+'.wav', "rb") as audio_file:
            content=audio_file.read()
        audio=speech.RecognitionAudio(content=content)
        response = client.recognize(config=config, audio=audio)
        os.remove('./clips/'+str(i//3)+'.wav')
        for result in response.results:
            dialogues.append(result.alternatives[0].transcript)
            if result.alternatives[0].transcript!='':
               timings.append(str(datetime.timedelta(seconds=i))+'-->'+str(datetime.timedelta(seconds=i+2.99))+'\n')

    os.remove(file)
    return timings,dialogues

def create_subtitles(timings,dialogues):

    with open('translated.srt','w',encoding='utf-8') as f:
        for i in range(len(timings)):
            f.write(timings[i])
            f.write(dialogues[i]+'\n\n')

