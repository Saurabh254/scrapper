from fastapi import FastAPI, Request
from .app import Scrapper
import uvicorn

app = FastAPI()


@app.get('/{productName}')
async def productData(productName: str, request: Request):
    scrapperObj = Scrapper(productName=productName)
    jsonData = await scrapperObj.flipkartScrapper.getFlipkartData()
    return {
        "client_host": request.client.host,
        "data": jsonData
    }


uvicorn.run(app)
