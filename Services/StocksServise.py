import requests
import Helpers.StringBuilder as stringBuilder
from Models import ResponseModels

# Разобраться почему не работает сокрытие
__all__ = ["getStockModels"]
headers = stringBuilder.getHeaders()

def getStockModels():
    # Параметры. Подумать, как задавать

    stockModels = []

    skip = 0
    take = 1000
    order = 'asc'

    i = 0
    # while True:
    while i < 1:
        # Подумать над асинхронным запросом

        url = stringBuilder.getStoksUrl(take, skip, order)
        response = requests.get(url, headers=headers)
        # Логировать ошибки!
        if response.status_code != 200:
            break


        jsonResults = response.json()['stocks']
        # print(len(jsonResults) )
        # Логировать такие случаи, чтобы понимать, сколько записей выгрузили
        if len(jsonResults) == 0:
            break

        stockModels += _mapModels(jsonResults)
        skip += 1000
        print(f'stock: {len(jsonResults)}')
        i += 1
    return stockModels

# На первое время сойдет
# Почитать про мапперы и конвертацию из json в model
def _mapModels(jsonResults):
    stockModels = []
    for jsonResult in jsonResults:
        stockModel = ResponseModels.StockModel(jsonResult)
        stockModels.append(stockModel)

    return stockModels