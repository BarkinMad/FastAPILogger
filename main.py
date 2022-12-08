import csv
from fastapi import FastAPI, Request, Response, logger, FileResponse
import pandas as pd

app = FastAPI()

@app.post("/log-error")
async def log_error(request: Request):
    # Parse the JSON-encoded error message from the request
    requestInfo = await request.json()
    error_message = requestInfo["error"]

    # Open the CSV file in append mode
    with open("errors.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        # Write the error message to the CSV file
        writer.writerow([error_message])
    # Return a success response
    return {"status": "SUCCESS"}

@app.get("/csv")
async def get_csv():
    df = pd.read_csv("./errors.csv")
    return FileResponse(df.to_csv, media_type="text/csv")