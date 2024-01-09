import os, glob, re
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import time
import requests
import json

#modules 
from sentpop import sentpop
from sentpop import block_split, tokenizer, split_text_by_percentage
from calc_sent_score import normalize_sent_score, positive_emotions, negative_emotions
from json_file import recursive_merge, update_json_file

import logging
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')


#the RoBERTa sentiment analysis model we are using
#API_URL = "https://api-inference.huggingface.co/models/SamLowe/roberta-base-go_emotions"

#load from .env file
load_dotenv()
my_api = os.environ.get("HUGGINGFACE_API_KEY")
data_path = os.environ.get("DATA_PATH")
API_URL = os.environ.get("ENDPOINT_URL")
headers = {"Authorization": f"Bearer {my_api}"}

def sent_query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    
    
    # Log the raw response
    logging.debug(f"API Response: {response.json()}")

    response_json = response.json()

    if 'error' in response_json:
        error_message = response_json['error']

        # Check if the error is due to input length and we haven't already attempted to remove Chinese characters
        if 'Input is too long' in error_message:
            print("Input too long. Removing Chinese characters and retrying.")
            print(payload['inputs'])
            old_text = payload['inputs']
            payload['inputs'] = re.sub(r'[\u4e00-\u9fff]+', '', payload['inputs'])
            return sent_query(split_text_by_percentage(old_text, payload['inputs'],0.8))
        elif 'estimated_time' in response_json:
            # Model is loading, wait for the estimated time plus a buffer
            wait_time = response_json['estimated_time'] + 5
            print(f"Model is loading. Waiting for {wait_time} seconds.")
            time.sleep(wait_time)
            return sent_query(payload)  # Retry the request
    return response_json

#initiate sentpop object
sent_data = sentpop()

for file_path in glob.glob(os.path.join(data_path, "*.txt")):
    print(file_path)
    #split the content of the .txt into a list of strings separated by block and with max char of 1800 to accomodate for the token limit for calling roBERTa
    block_holder = block_split(file_path)

    for i, block in enumerate(block_holder):
        # Create a JSON object temp_data with the "inputs" key
        temp_data = {"inputs": block}
        # Call the model with temp_data
        score = sent_query(temp_data)
        #print(f"Block: {block}\n Score: {score}")
        if('error' in score):
            update_json_file('output.json',sent_data.data)
            print(score)
            print(block)
        print(score)
        normalized_score = normalize_sent_score(score)

        #extract the date from the file path
        date, _ = os.path.splitext(os.path.basename(file_path))

        sent_data.add_block(date, block, normalized_score, score[0])

update_json_file('output.json', sent_data.data)



