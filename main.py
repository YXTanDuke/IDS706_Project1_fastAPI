from typing import Dict
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Duke"}


@app.get("/StrMostFreq/{input_str}")
async def str_most_freq(input_str: str):
    """Find the most frequent character in a string"""
    return str_most_freq_helper(input_str)


def str_most_freq_helper(input_str: str) -> Dict:

    if len(input_str) == 0:
        return None

    freq = {}
    for i in input_str:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    max_key = max(zip(freq.values(), freq.keys()))[1]
    max_val = max(freq.values())

    return {"most_frequent_key": max_key, "frequency": max_val}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
