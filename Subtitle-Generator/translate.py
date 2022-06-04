from google.cloud import translate_v2 as translate
import requests

def translation(sentences,src,target):
    
    translate_client = translate.Client()
    languages={}
    languages['English']='en'
    languages['French']='fr'
    languages['Japanese']='ja'
    languages['Chinese']='zh'
    languages['Korean']='ko'
    languages['German']='de'
    languages['Spanish']='es'
    
    results = translate_client.translate(sentences, source_language=languages[src], target_language=languages[target])

    output=[]

    for result in results:                             
      output.append(result['translatedText'])      
      
    return output
