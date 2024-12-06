import requests
import socket
import json
import tiktoken

def count_tokens(prompt, model="gpt-3.5-turbo"):
    tokenizer = tiktoken.encoding_for_model(model)
    return len(tokenizer.encode(prompt))

def split_prompt(prompt, chunk_size=2000, model="gpt-3.5-turbo"):
    tokenizer = tiktoken.encoding_for_model(model)
    tokens = tokenizer.encode(prompt)
    
    chunks = [tokens[i:i + chunk_size] for i in range(0, len(tokens), chunk_size)]
    return [tokenizer.decode(chunk) for chunk in chunks]

def call_llm(prompt):
    url = "https://www.dmxapi.com/v1/chat/completions"
    max_tokens = 8192  
    chunk_size = 7000  
    model = "gpt-4o"


    print(count_tokens(prompt, model="gpt-3.5-turbo"))
    if count_tokens(prompt, model="gpt-3.5-turbo") > max_tokens:
        prompt_chunks = split_prompt(prompt, chunk_size=chunk_size, model="gpt-3.5-turbo")
        print(prompt_chunks)
    else:
        prompt_chunks = [prompt]

    headers = {
        'Accept': "application/json",
        'Authorization': "YOUR API KEY",  
        'User-Agent': 'mtuopenai/1.0.0 (https://www.dmxapi.com)',
        'Content-Type': 'application/json'
    }


    combined_answer = ""
    for chunk in prompt_chunks:
        payload = json.dumps({
            "model": model,
            "messages": [
                {"role": "user", "content": chunk}
            ]
        })
        
        response = requests.post(url, headers=headers, data=payload, timeout=300)
        response_data = response.json()
        
        print(response_data)
        answer = response_data["choices"][0]["message"]["content"]
        combined_answer += answer  

    return {"answer": combined_answer, "usage": {"total_chunks": len(prompt_chunks)}}



