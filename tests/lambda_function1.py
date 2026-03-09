"""
Simple Temperature Converter Lambda Function
Convert Celsius to Fahrenheit
    
Expected input: {"temperature": 25}
Expected output: {"statusCode": 200, "body": "Temperature 25°C is equal to 77°F"}
"""
import json

def lambda_handler(event, context=None):
    celsius = event['temperature']
    
    if celsius == None:
        return {
            'statusCode': 200,
            'body': json.dumps('Error: temperature field is required')
        }
    
    fahrenheit = celsius * 9/5
    
    return {
        'body': fahrenheit
    }