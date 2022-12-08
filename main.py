import csv
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import pandas as pd
from io import BytesIO

app = FastAPI()

@app.post("/log-error")
async def log_error(request: Request):
    # Parse the JSON-encoded error message from the request
    requestInfo = await request.json()
    error_message = requestInfo["error"]
    print("Error message received from game server")
    print(error_message)
    # Open the CSV file in append mode
    with open("errors.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        # Write the error message to the CSV file
        writer.writerow([error_message])
    # Return a success response
    return {"status": "SUCCESS"}

@app.get("/csv")
async def get_csv():
    df = pd.read_csv("errors.csv")

    async def stream():
        yield df.to_csv(index=False)
    
    response = StreamingResponse(stream(), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=data.csv"
    return response