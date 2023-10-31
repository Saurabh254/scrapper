from bs4 import BeautifulSoup
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
        try:
            imgTag = self._html.find('img', class_='_396cs4')
            if (imgTag):
                return imgTag['alt']
            return None
        except Exception as e:
            print("Ran into an error:", e)
            return None

    def _getPrice(self):
        try:
            priceTag = self._html.find('div', class_=FLIPKART_PRODUCT_PRICE)
            if priceTag:
                return priceTag.contents[0]
            priceTag = self._html \
                .find('div', class_='_8VNy32') \
                .find('div', class_='_30jeq3')
            if priceTag:
                return priceTag.contents()
            return None
        except Exception as e:
            print("Ran into an error:", e)
            return None

    def _getDescriptionList(self):
        try:
            _desList = []
            _rawlist = self._html                        \
                .find('ul', FLIPKART_PRODUCT_DESCRIPTION_UL) \
                .findChildren('li', recursive=False)
            for i in _rawlist:
                if i:
                    _desList.append(

                        i.get_text().strip()
                    )
            return _desList
        except Exception as e:
            print("Ran into an error:", e)
            return None

    def _getRating(self):
        try:
            ratingTag = self._html.find_all(
                'div', class_=FLIPKART_PRODUCT_RATING)
            if ratingTag:
                return ratingTag[0].get_text()[:-1]
            return None
        except Exception as e:
            print("Ran into an error:", e)
            return None

    def _getProductImg(self):
        try:
            imgTag = self._html.find('img', class_=FLIPKART_PRODUCT_IMG)

            return imgTag['src']
        except Exception as e:
            print("Ran into an error:", e)
            return None

    def getData(self):
        try:
            return {
                'title': self._getTitle(),
                'price': self._getPrice(),
                'descriptionList': self._getDescriptionList(),
                'rating': self._getRating(),
                'productImage': self._getProductImg()
            }
        except Exception as e:
            print("Ran into an error:", e)
            return {}


class Extractor:
    """extracts the data from the html
    """

    def __init__(self, html) -> None:
        self._html = html
        # print(self._html)
        self._soup = BeautifulSoup(str(self._html), 'html.parser')

    def getAllDivs(self):
        divs = self._soup.find_all('div', class_=FLIPKART_PRODUCT_DIV)
        return divs[2:-1]

    def extractedRawDataOfDivs(self):
        _data = {}
        for i, html in enumerate(self.getAllDivs()):
            _data[i] = BaseExtractor(html).getData()
        return _data
