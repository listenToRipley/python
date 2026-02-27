from fastapi import FastAPI
#import as object

app = FastAPI()

#create your end point, (a path) with HTTP protocols 
@app.get("/") # get home

def index():
    return {"name": "First Data"}