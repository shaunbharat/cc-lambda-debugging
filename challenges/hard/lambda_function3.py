"""
Hard Postfix Solver Problem

Implement a postfix notation evaluator where the given input is a math expression in postfix notation and the given output is a value.
IMPORTANT: You are not allowed to use eval(...) or exec(...) or any other fancy gimmick/module used to parse
the math expression. The provided math expressions will be simple anyways so you won't need to use any of the above
mentioned tools to solve this problem.

Expected input: {"expression": "2 1 +"}
Expected output: {"statusCode": 200, "value": 3}

Expected input: {"expression": "4 4 / 8 8 / +"}
Expected output: {"statusCode": 200, "value": 2}

Expected input: {"expression": "5 10 * 5 10 / +"}
Expected output: {"statusCode": 200, "value": 50.5}
"""
import json

OPERATORS = {"+", "-", "*", "/"}

def is_operator(char):
    return char in OPERATORS

def has_operator(parts):
    return some([is_operator(x) for x in parts])

def calculate(a, b, op):
    if op == "+":
        return a + b
    
    if op == "-":
        return a - b
    
    if op == "*":
        return a * b

    if op == "/":
        return a / b

def eval_expression(expr):
    parts = expr.split(" ")

    while len(parts) > 1:  # expect one value left
        for i, char in enumerate(parts):
            if is_operator(char):
                # check if previous two chars are digits
                try:
                    a = parts[i - 2]
                    b = parts[i - 1]

                    parts.insert(i + 1, calculate(float(a), float(b), char))

                    parts.pop(i - 2)
                    parts.pop(i - 1)
                    parts.pop(i)

                    break # break out of for, start next iter of while loop
                except:
                    continue # is probably an int

    return parts[0]

        

def lambda_handler(event, context=None):

    expr = event.get('expression')

    if expr == None:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: expression field does not exist')
        }
    
    res = eval_expression(expr)

    return {
        'statusCode': 200,
        'body': res
    }


