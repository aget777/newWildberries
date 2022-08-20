import requests
import Helpers.StringBuilder as stringBuilder
from Models import ResponseModels

# Разобраться почему не работает сокрытие
__all__ = ["getWarehousesModels"]
headers = stringBuilder.getHeaders()

def getWarehousesModels():
    # Параметры. Подумать, как задавать
    # Разобраться с конвертацией, пока это костыль!!!
    # dateStart = datetime.datetime(2021, 12, 1).isoformat()
    warehousesModels = []

    i = 0
    while i < 1:
        # Подумать над асинхронным запросом
        url = stringBuilder.getwarehousesUrl()
        response = requests.get(url, headers=headers)


        # Логировать ошибки!
        if response.status_code != 200:
            break

        jsonResults = response.json()
        # print(jsonResults)
        # Логировать такие случаи, чтобы понимать, сколько записей выгрузили
        if len(jsonResults) == 0:
            break

        warehousesModels += _mapModels(jsonResults)

        print(f'warehouses: {len(jsonResults)}')
        i += 1
    return warehousesModels

# На первое время сойдет
# Почитать про мапперы и конвертацию из json в model
def _mapModels(jsonResults):
    warehousesModels = []
    for jsonResult in jsonResults:
        warehousesModel = ResponseModels.WarehousesModel(jsonResult)
        warehousesModels.append(warehousesModel)

    return warehousesModels