import pyodide.http
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
  "max_tokens": 1024
})
headers = {
  'Content-Type': 'application/json'
}

async def fetch_data():
    try:
        response = await pyodide.http.pyfetch(
            url, 
            method="POST", 
            headers=headers, 
            body=payload
        )
        data = await response.json()
        print(data)
    except Exception as e:
        print(f"Error: {e}")

# Run the function
await fetch_data()