# API Endpoint

A simple Python HTTP API server that performs basic math operations and returns results as JSON.

## How I Built It

### Step 1 — Created the math functions
First I created four simple functions for each math operation:
- `add(a, b)` — adds two numbers
- `subtract(a, b)` — subtracts two numbers
- `multiply(a, b)` — multiplies two numbers
- `divide(a, b)` — divides two numbers

### Step 2 — Created a class using Python's built in HTTP server
I created a class `MyHandler` that extends Python's built in `BaseHTTPRequestHandler`. This class listens for every GET request that comes into the server.

### Step 3 — Parsed the URL
When someone visits a URL like `http://localhost:7000/add?a=5&b=3`, I used `urlparse` to split it into two parts:
- The path: `/add`
- The query: `a=5&b=3`

Then I used `parse_qs` to extract `a` and `b` from the query string.

### Step 4 — Type casted the parameters
I converted `a` and `b` from strings to floats using `float()` so I could do math on them.

### Step 5 — Checked which endpoint was hit
I used `if/elif` conditions to check which path was visited and called the matching math function:
- `/add` → calls `add(a, b)`
- `/subtract` → calls `subtract(a, b)`
- `/multiply` → calls `multiply(a, b)`
- `/divide` → calls `divide(a, b)`

### Step 6 — Returned the result as JSON
I used `json.dumps()` to convert the result into JSON, set the response headers, and sent it back to the browser using `self.wfile.write()`.

## Setup

1. Clone the repo
2. Create virtual environment:
```bash
   python -m venv myenv
```
3. Activate it:
```bash
   source myenv/Scripts/activate
```
4. Run the server:
```bash
   python request.py
```

## Endpoints

Base URL: `http://localhost:7000`

| Endpoint | Operation | Example |
|----------|-----------|---------|
| `/add` | Addition | `/add?a=5&b=3` |
| `/subtract` | Subtraction | `/subtract?a=9&b=4` |
| `/multiply` | Multiplication | `/multiply?a=3&b=3` |
| `/divide` | Division | `/divide?a=9&b=3` |

## Example Response

```json
{"result": 8.0}
```