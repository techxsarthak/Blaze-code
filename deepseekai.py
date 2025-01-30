# Please install the required modules first
import requests
import json

url = "https://api.blackbox.ai/api/chat"

payload = json.dumps({
  "messages": [
    {
      "content": "make a simple python function",
      "role": "user"
    }
  ],
  "model": "deepseek-ai/DeepSeek-R1",
  "max_tokens": "1024"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
