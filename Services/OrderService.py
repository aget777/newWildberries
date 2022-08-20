import requests
import Helpers.StringBuilder as stringBuilder
from Models import ResponseModels

# Разобраться почему не работает сокрытие
__all__ = ["getDealModels"]
headers = stringBuilder.getHeaders()

def getDealModels():
    # Параметры. Подумать, как задавать
    # Разобраться с конвертацией, пока это костыль!!!
    # dateStart = datetime.datetime(2021, 12, 1).isoformat()
    dealModels = []

    # dateStart = '2022-07-01T00%3A00%3A00%2B03%3A00'
    # dateEnd = '2021-07-25T00%3A00%3A00%2B03%3A00'
    dateStart = '2022-07-01T00%3A00%3A00.00Z'
    dateEnd = '2022-08-13T00%3A00%3A00.00Z'
    status = ""
    skip = 0
    take = 1000
    order = 'asc'
    while True:
        # Подумать над асинхронным запросом
        url = stringBuilder.getOrderUrl(dateStart=dateStart , take=take, skip=skip, dateEnd=dateEnd, status=status)
        response = requests.get(url, headers=headers)


        # Логировать ошибки!
        if response.status_code != 200:
            break


        jsonResults = response.json()['orders']
        # print(jsonResults)
        # Логировать такие случаи, чтобы понимать, сколько записей выгрузили
        if len(jsonResults) == 0:
            break

        dealModels += _mapModels(jsonResults)
        skip += 1000
        print(f'orders: {len(jsonResults)}')

    return dealModels

# На первое время сойдет
# Почитать про мапперы и конвертацию из json в model
def _mapModels(jsonResults):
    dealModels = []
    for jsonResult in jsonResults:
        dealModel = ResponseModels.DealModel(jsonResult)
        dealModels.append(dealModel)

    return dealModels