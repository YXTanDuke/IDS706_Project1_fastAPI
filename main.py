from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Duke"}

@app.get("/StrMostFreq/{input_str}")
async def add(input_str: str):
    """Find the most frequent character in a string"""

    freq = {}
    for i in input_str:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    max_key = max(zip(freq.values(), freq.keys()))[1]
    max_val = max(freq.values()) 
    
    return {
        "most_frequent_key": max_key,
        "frequency": max_val
    }

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')