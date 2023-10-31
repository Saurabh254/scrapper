from .modules.scrapper import FlipkartDataHandler
import aiohttp
from fastapi import FastAPI


class Scrapper:
    """Base Scrapper class
    """

    def __init__(self,
                 productName) -> None:
        self.session = aiohttp.ClientSession()
        self.productName = productName
        self.flipkartScrapper = FlipkartDataHandler(
            session=self.session,
            productName=self.productName
        )
