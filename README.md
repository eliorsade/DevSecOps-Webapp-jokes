# Flask Joke API

## Overview

Simple web application that will fetch a random joke from https://official-joke-api.appspot.com/random_joke.  
The API supports only GET requests and returns a JSON-formatted response with a punchline ID and a random joke's punchline.

## Usage
To execute the script, type the command:  
```bash 
python3 main.py
```
### Prerequisites

- Python 3.10
- Flask
- Requests library

### Request

```bash
curl http://127.0.0.1:5000/
```

### Response
```JSON
{
    "punchline_id": 10,
    "punchline": "Sneakers"
}
```
