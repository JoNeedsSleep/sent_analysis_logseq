import requests, time

API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-zh-en"
headers = {"Authorization": f"Bearer {API_URL}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	if 'error' in response.json() and 'estimated_time' in response.json():
        # Model is loading, wait for the estimated time plus a buffer
		wait_time = response.json()['estimated_time'] + 5
		print(f"Model is loading. Waiting for {wait_time} seconds.")
		time.sleep(wait_time)
		return query(payload)  # Retry the request
	return response.json()

def chinese_to_english(chinese_text):	
	output = query({
		"inputs": chinese_text,
	})
	print(output[0]['translation_text'])