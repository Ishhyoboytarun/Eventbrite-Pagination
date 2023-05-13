#!/bin/python3

import math
import os
import random
import re
import sys
import json


def format_response(response):
    formatted_response = 'PageNumber: {}\n'.format(response['page_number'])
    formatted_response += 'ItemsPerPage: {}\n'.format(response['items_per_page'])
    formatted_response += 'TotalCount: {}\n'.format(response['total_count'])
    formatted_response += 'Items: '
    for item in response['items']:
        formatted_response += "\n    Item ID: {}, Name: {}".format(item['id'], item['name'])
    return formatted_response;

MAX_ID = 1000  # maximum ID of items in the service

#Custom implementation of get_request method
def getRequest(page_number, items_per_page=10):
    start_id = (page_number - 1) * items_per_page + 1
    end_id = start_id + items_per_page - 1
    if end_id > MAX_ID:
        end_id = MAX_ID
    result = []
    for id in range(start_id, end_id + 1):
        result.append({
            "id": id,
            "name": "Item " + str(id),
        })
    return {
        "total_count": MAX_ID,
        "page_number": page_number,
        "items_per_page": items_per_page,
        "items": result,
    }

def abstracted_request(page_number, items_per_page):
    if page_number <= 0 or items_per_page <= 0 or items_per_page > 50:
        return "404"
    result = getRequest(page_number, items_per_page)
    if not result["items"]:
        return "404"
    return format_response({
        "page_number": result["page_number"],
        "items_per_page": result["items_per_page"],
        "total_count": result["total_count"],
        "items": result["items"],
        })

#This is the external 3rd party API given in the question itself.
def get_request(page_number):
    number_of_items = 10
    result = []
    for i in range(number_of_items):
        id = ((page_number - 1) * number_of_items) + i + 1
        if(id > MAX_ID):
            break
        result.append({
            "id": id,
            "name": "Item " + str(id),
        })
    return result

MAX_ID = 1 # This constant is for internal use only and should not be referenced in the candidates code, candidates are expected to calculate this value based on calls to get_request

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    MAX_ID = int(input().strip())

    page_number = int(input().strip())

    items_per_page = int(input().strip())

    result = abstracted_request(page_number, items_per_page)

    fptr.write(result + '\n')

    fptr.close()
