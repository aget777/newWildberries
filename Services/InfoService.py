import requests
import Helpers.StringBuilder as stringBuilder
from Models import ResponseModels

# Разобраться почему не работает сокрытие
__all__ = ["getInfoModels"]
headers = stringBuilder.getHeaders()

def getInfoModels():
    # Параметры. Подумать, как задавать
    # Разобраться с конвертацией, пока это костыль!!!
    # dateStart = datetime.datetime(2021, 12, 1).isoformat()
    infoModels = []

    i = 0
    while i < 1:
        # Подумать над асинхронным запросом
        url = stringBuilder.getInfoUrl()
        response = requests.get(url, headers=headers)


        # Логировать ошибки!
        if response.status_code != 200:
            break

        jsonResults = response.json()
        # print(jsonResults)
        # Логировать такие случаи, чтобы понимать, сколько записей выгрузили
        if len(jsonResults) == 0:
            break

        infoModels += _mapModels(jsonResults)

        print(f'info: {len(jsonResults)}')
        i += 1
    return infoModels

# На первое время сойдет
# Почитать про мапперы и конвертацию из json в model
def _mapModels(jsonResults):
    infoModels = []
    for jsonResult in jsonResults:
        infoModel = ResponseModels.InfoModel(jsonResult)
        infoModels.append(infoModel)

    return infoModels