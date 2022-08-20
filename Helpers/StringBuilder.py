from Models import Constans

# Разобраться почему не работает сокрытие
__all__ = ["getHeaders", "getOrderUrl"]

urls = Constans.URLs()
headers = Constans.Headers()
parameters = Constans.OrderParameters()

# добавить нормальную сборку заголовков, почитать про это
def getHeaders() -> dict:
    return {headers.accept: headers.acceptValue, headers.authorization: headers.APIKey}

def getOrderUrl(dateStart, take, skip, dateEnd='', status='', id='') -> str:
    url = urls.baseURL + urls.orderUrl

    url = _addParameter(url, '?', parameters.dateStart, dateStart)
    url = _addParameter(url, '&', parameters.dateEnd, dateEnd)
    url = _addParameter(url, '&', parameters.status, str(status))
    url = _addParameter(url, '&', parameters.take, str(take))
    url = _addParameter(url, '&', parameters.skip, str(skip))
    url = _addParameter(url, '&', parameters.id, str(id))

    return url

def _addParameter(url, delimiter, name, value) -> str:
    if not value:
        return url

    return url + delimiter + name + '=' + value

def getStoksUrl(take, skip, order='') -> str:
    url = urls.baseURL + urls.stocksUrl

    url = _addParameter(url, '?', parameters.skip, str(skip))
    url = _addParameter(url, '&', parameters.take, str(take))
    url = _addParameter(url, '&', parameters.order, str(order))

    return url



def getInfoUrl() -> str:
    url = urls.baseURL + urls.infoUrl

    return url

def getwarehousesUrl() -> str:
    url = urls.baseURL + urls.warehousesUrl

    return url