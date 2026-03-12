"""
Medium Translator Lambda Function

Given a word, convert all vowels and Y into the NATO phonetic alphabet

A -> Alpha
E -> Echo
I -> India
O -> Oscar
U -> Uniform
Y -> Yankee

Note that conversion is not case sensitive, also note that consonants do not need to be converted.

Expected input: {"word": "alpha"}
Expected output: {"statusCode": 200, "body": "AlphalphAlpha"}

Expected input: {"word": "harlem"}
Expected output: {"statusCode": 200, "body": "hAlpharlEchom"}
"""
import json

def lambda_handler(event, context=None):

    word = event['word']
    res = []

    if word == None:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: word field does not exist')
        }
    
    for char in word:
        res.append(char)

    return {
        'statusCode': 200,
        'body': res
    }
