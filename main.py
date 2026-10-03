import requests
from dotenv import load_dotenv
import os
load_dotenv()
# print(os.environ)
api_key = os.environ["GROQ_API_KEY"]


# response =requests.get("https://api.groq.com/openai/v1")
# print(response)
# print(response.status_code)
# print(response.json())

# response =requests.get("https://api.groq.com/openai/v1/models",headers={
#     "Authorization":f"Bearer {api_key}"
# })
# print(response)
# print(response.status_code)
# print(response.json())

"openai/gpt-oss-120b"

# response =requests.post("https://api.groq.com/openai/v1/chat/completions",headers={
#     "Authorization":f"Bearer {api_key}"
# },
# json={
#     "model":"openai/gpt-oss-120b",
#     "messages":[{"role":"user","content":"hello, how are you?"}
#     ]
    
# })
# print(response.status_code)
# print(response.json()["choices"][0]["message"]["content"])
# for choice in response.json()["choices"]:  
#     print(choice["message"]["content"])
# history=[{"role":"system","content":"You are a rugged Port Harcourt Boy that speaks with only PH slangs."}]
history=[{"role":"system","content":"""You're a relationship expert and a therapist. 
You are an expert at match making. Ask the user questions about him/her such as name, 
personalities, likes, and that of the spouse, then give a rating if they are a match or not.
 You can use their zodiac sign as a strong indicator for compatibility. Be polite and short in your introduction. 
 Use a friendly and soft tone in your responses and ask questions in different tones. If the user asks anything outside of your proffession, just say 'Sorry, i can\'t help with that'"""}]
while True:
    user_message = input("You: ")
    if not user_message or user_message in ["quit","exit","bye"]:
        break
    history.append({"role":"user","content":user_message})
    response =requests.post("https://api.groq.com/openai/v1/chat/completions",headers={
    "Authorization":f"Bearer {api_key}"
    },
    json={
        "model":"openai/gpt-oss-120b",
        "messages":history
        
    })
    # print(response.status_code)
    print("Ai: "+response.json()["choices"][0]["message"]["content"])
    print()
    history.append({"role":"assistant","content":response.json()["choices"][0]["message"]["content"]})