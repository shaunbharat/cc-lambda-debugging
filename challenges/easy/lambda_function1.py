"""
Simple Temperature Converter Lambda Function
Convert Celsius to Fahrenheit
    
Expected input: {"temperature": 25}
Expected output: {"statusCode": 200, "body": 77}
"""
import json

def lambda_handler(event, context=None):
    celsius = event.get('temperature')
    
    if celsius == None:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: temperature field is required')
        }
    
    fahrenheit = celsius * 9/5 + 32
    if type(fahrenheit) == float:
        fahrenheit = round(fahrenheit, 2) 
    
    return {
        'statusCode': 200,
        'body': fahrenheit
    }
