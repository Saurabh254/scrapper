from bs4 import BeautifulSoup
from typing import List
from ...helpers import logger
from ...constants import (
    FLIPKART_PRODUCT_DESCRIPTION_UL,
    FLIPKART_PRODUCT_DIV,
    FLIPKART_PRODUCT_PRICE,
    FLIPKART_PRODUCT_RATING,
    FLIPKART_PRODUCT_IMG
)


class BaseExtractor:

    def __init__(self, html) -> None:
        self._html = html

    def _getTitle(self):
        # find the img tag
        try:
            imgTag = self._html.find('img', class_='_396cs4')
        except Exception as e:
            imgTag = None
        # if imgTag exists return alt text
        if (imgTag):
            return imgTag['alt']
        # if imgTag is None return None
        return None

    def _getPrice(self):

        # finds the div element of the price tag
        # if we flipkart suggest the exact product then it will works else it will return none
        try:
            priceTag = self._html.find('div', class_=FLIPKART_PRODUCT_PRICE)
        except Exception as e:
            priceTag = None
        # if priceTag is none we'll return the tag
        if priceTag:
            return priceTag.contents[0]

        # if flipkart doesn't able to find the exact product then
        # this will find the exact one (random products)
        try:
            priceTag = self._html \
                .find('div', class_='_8VNy32')
            priceTag = priceTag.find('div', class_='_30jeq3')
        except Exception as e:
            priceTag = None
        # if the price tag is fetched it will return the contents of the product
        if priceTag:
            return priceTag.contents().replace('₹', '').replace(',', '')

        # else None
        return None

    def _getDescriptionList(self):

        # parsed list in which description is stored
        _desList: List[str] = []

        # raw tags list of descriptions ul>li
        try:
            _rawlist = self._html \
                .find('ul', FLIPKART_PRODUCT_DESCRIPTION_UL) \
                .findChildren('li', recursive=False)
        except Exception as e:
            _rawlist = None
        # Appending the data into _desList by extracting it and formatting it
        if _rawlist:
            for i in _rawlist:
                if i:
                    _desList.append(
                        i.get_text().strip()
                    )
        # Returns parsed data if it founds the description else return empty dict
        return _desList

    def _getRating(self):

        # find all the rating tags
        try:
            ratingTag = self._html.find_all(
                'div', class_=FLIPKART_PRODUCT_RATING)
        except Exception as e:
            ratingTag = None

        if ratingTag:
            return ratingTag[0].get_text()
        return ratingTag

    def _getProductImg(self):
        try:
            imgTag = self._html.find('img', class_=FLIPKART_PRODUCT_IMG)
        except Exception as e:
            imgTag = None
        if imgTag:
            return imgTag['src']
        return imgTag

    def getData(self):
        return {
            'title': self._getTitle(),
            'price': self._getPrice(),
            'descriptionList': self._getDescriptionList(),
            'rating': self._getRating(),
            'productImage': self._getProductImg()
        }


class Extractor:
    """extracts the data from the html
    """

    def __init__(self, html) -> None:
        self._html = html
        # print(self._html)
        self._soup = BeautifulSoup(str(self._html), 'html.parser')

    def getAllDivs(self):
        try:
            divs = self._soup.find_all('div', class_=FLIPKART_PRODUCT_DIV)
        except Exception as e:
            logger.warn(e)
            return []
        return divs[2:-1]

    def extractedRawDataOfDivs(self):
        _data = {}
        for i, html in enumerate(self.getAllDivs()):
            _data[i] = BaseExtractor(html).getData()
        return _data
