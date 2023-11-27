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

        # finding the rating tag
        try:
            ratingTag = self._html.find_all(
                'div', class_=FLIPKART_PRODUCT_RATING)
        # if unable to find rating tag return None
        except Exception as e:
            ratingTag = None

        # if ratingTag isn't none return the text within it
        if ratingTag:
            return ratingTag[0].get_text()
        # else return None
        return ratingTag

    def _getTotalReviewsAndRatingCount(self):

        # find the raw span elements
        try:
            countSpans = self._html \
                .find('div', class_='gUuXy-') \
                .find('span', class_='_2_R_DZ') \
                .find('span')       \
                .find_all('span')
        except Exception as e:
            countSpans = []

        # extract the text from the raw tags and add it into extractedString
        extractedString = ''

        # iterating over countSpans
        for rawTag in countSpans:
            # removing unused spaces and keywords
            extractedString += rawTag.get_text().strip().replace('&nbsp;', ' ') + ' '

        # check if the extractedString is empty or not
        if len(extractedString):
            return extractedString

        # if extractedString is empty return None
        else:
            return None

    def _getProductImg(self):
        # find the img tag of the product
        try:
            imgTag = self._html.find('img', class_=FLIPKART_PRODUCT_IMG)
        # in case it's not able to find the product imgTag is  None
        except Exception as e:
            imgTag = None

        # if imgTag is not none return the src url of the img tag
        # src tag will be url of the image

        if imgTag:
            return imgTag['src']

        # if imgTag is None return None

        return imgTag

    def getData(self):

        # return the data if any of the field failed to find the data it will be shipped with None value
        return {
            'title': self._getTitle(),
            'price': self._getPrice(),
            'descriptionList': self._getDescriptionList(),
            'rating': self._getRating(),
            'productImage': self._getProductImg(),
            'total_rating': self._getTotalReviewsAndRatingCount(),
        }


class Extractor:
    """extracts the data from the html
    """

    def __init__(self, html) -> None:
        self._html = html
        # create a soup obj
        self._soup = BeautifulSoup(str(self._html), 'html.parser')

    def getAllDivs(self):
        # find all the div of the products
        try:
            divs = self._soup.find_all('div', class_=FLIPKART_PRODUCT_DIV)
        # in case it failed to find the divs return a empty list
        except Exception as e:
            logger.warn(e)
            return []

        # slicing the list by filter divs and footer div at last
        return divs[2:-1]

    def extractedDataOfDivs(self) -> dict:

        # _data is the dict of values
        _data = {}

        # iterating over the divs
        for i, html in enumerate(self.getAllDivs()):
            # fetching the data and storing it in _data dict with key as index
            _data[i] = BaseExtractor(html).getData()

        # return the evaluated dict maybe with data or empty
        return _data
