"""This is python3.6 program."""

import boto3
import json
import uuid
from builtins import Exception
import os
import time
from utils import *
from decimal import *

# import requests

DYNAMODB_ENDPOINT = os.getenv('DYNAMODB_ENDPOINT')
SEAT_TABLE_NAME = os.getenv('SEAT_TABLE_NAME')
SEQ_TABLE_NAME = os.getenv('SEQ_TABLE_NAME')

DYNAMO = boto3.resource(
    'dynamodb',
    endpoint_url=DYNAMODB_ENDPOINT
)

SEAT_TABLE = DYNAMO.Table(SEAT_TABLE_NAME)
SEQ_TABLE = DYNAMO.Table(SEQ_TABLE_NAME)

'''
def next_id(table_name):
    data = SEQ_TABLE.update_item(
               key={
                 'current_number' : {
                   value: {
                     n: '1'
                   },
                   action: 'ADD',
                  },
               },
           return_values: 'UPDATED_NEW',
           ).data
 
  data['attributes']['current_number'][:n]
'''

def get_seats(event, context):
    try:
        seat_id = event['pathParameters']['seatId']

        print(DYNAMODB_ENDPOINT)
        print(SEAT_TABLE)

        dynamo_response = SEAT_TABLE.get_item(
            Key={
                'seat_id': seat_id
            }
        )
    
        return {
            "statusCode": 200,
            "body": "success"
        }

    except Exception as e:
        return create_response(500, {"message": str(e)})

def add_seats(event, context):
    try:
        seat_id = next_id(SEAT_TABLE)

        name = event.get('name')
        comment = event.get('comment')
        state = event.get('state')

        dynamo_response = SEAT_TABLE.put_item(
            Item={
                'seat_id': seat_id,
                'name': seat_id,
                'comment': seat_id,
                'state': seat_id
            }
        )
    
        return {
            "statusCode": 201,
            "body": "success"
        }

    except Exception as e:
        return create_response(500, {"message": str(e)})

def update_seats(event, context):
    try:
        seat_id = event['pathParameters']['seatId']

        name = event.get('name')
        comment = event.get('comment')
        state = event.get('state')

        dynamo_response = SEAT_TABLE.put_item(
            Item={
                'seat_id': seat_id,
                'name': seat_id,
                'comment': seat_id,
                'state': seat_id
            }
        )
        return {
            "statusCode": 201,
            "body": "success"
        }

    except Exception as e:
        return create_response(500, {"message": str(e)})

def decimal_default_proc(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

def create_response(statuscode, obj):
    return {"statusCode": statuscode, "body": json.dumps(obj,default=decimal_default_proc)}

