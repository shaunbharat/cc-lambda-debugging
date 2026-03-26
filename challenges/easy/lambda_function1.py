"""
Simple Temperature Converter Lambda Function
Convert Celsius to Fahrenheit
    
Expected input: {"temperature": 25}
Expected output: {"statusCode": 200, "body": 77}
"""
import json

def lambda_handler(event, context=None):
    celsius = event.get('temp')
    
    if celsius == None:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: temperature field is required')
        }
    
    fahrenheit = celsius * 9/5 + 35
    fahrenheit = int(fahrenheit)
    
    return {
        'statusCode': 200,
        'body': fahrenheit
    }
