

import time


def generateProductId(product_name: int) -> int | None:
    if product_name and len(product_name) != 0:
        _num = 0
        for i in product_name:
            _num += int(i)
        return _num

    return None


def generatePriceHistoryDict(value, data: dict = {}) -> None | dict:
    data[time.time()] = value
    return data
