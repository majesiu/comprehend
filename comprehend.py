import boto3
import json



def lambda_handler(event, context):
    comprehend = boto3.client(service_name='comprehend')
    text = "It is snowing today in Poznañ. "
    
    print('Calling DetectEntities')
    print(json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
    print('End of DetectEntities\n')
    
    print('Calling DetectSentiment')
    print(json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
    print('End of DetectSentiment\n')
    
    print('Calling DetectDominantLanguage')
    print(json.dumps(comprehend.detect_dominant_language(Text = text), sort_keys=True, indent=4))
    print("End of DetectDominantLanguage\n")
    
    print('Calling DetectEntities')
    print(json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
    print('End of DetectEntities\n')
    
    return 'Comprehende Cabron'
