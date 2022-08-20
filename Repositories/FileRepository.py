import os

# Добавить нормальные проверки и нормальное отслеживание состояния файлов в каталоге
# Возможно, свои эксепшены. Логировать.
def setDealInFile(dealModels) -> None:
    # path = 'E:\\Wildberries\\API\\WildbberiesData\\DataTest'
    path = r'C:\Users\Lenovo\Downloads\01_Текущие'
    if not os.path.exists(path):
        createCatalog(path)

    file = open(path + '\\dealTestResult', 'w', encoding='utf-8')

    for dealModel in dealModels:
        file.writelines('dateCreated: ' + str(dealModel.dateCreated) + '\n')
        file.writelines('orderId: ' + str(dealModel.orderId) + '\n')
        # file.writelines('userId: ' + str(dealModel.userId) + '\n')
        file.writelines('officeAddress: ' + str(dealModel.officeAddress) + '\n')
        file.writelines('chrtId: ' + str(dealModel.chrtId) + '\n')
        file.writelines('rid: ' + str(dealModel.rid) + '\n')
        file.writelines('status: ' + str(dealModel.status) + '\n')
        file.writelines('totalPrice: ' + str(dealModel.totalPrice) + '\n')
        # file.writelines('OfficeLatitude: ' + str(dealModel.OfficeLatitude) + '\n')
        # file.writelines('OfficeLongitude: ' + str(dealModel.OfficeLongitude) + '\n')
        file.writelines('\n')

    file.close()

# Пока костыль, потом посмотреть доработать





def setStockInFile(stockModels) -> None:
    # path = 'E:\\Wildberries\\API\\WildbberiesData\\DataTest'
    path = r'C:\Users\Lenovo\Downloads\01_Текущие'
    if not os.path.exists(path):
        createCatalog(path)

    file = open(path + '\\stockTestResult', 'w', encoding='utf-8')

    for stockModel in stockModels:
        file.writelines('nmId: ' + str(stockModel.nmId) + '\n')
        file.writelines('chrtId: ' + str(stockModel.chrtId) + '\n')
        file.writelines('subject: ' + str(stockModel.subject) + '\n')
        file.writelines('brand: ' + str(stockModel.brand) + '\n')
        file.writelines('name: ' + str(stockModel.name) + '\n')
        file.writelines('article: ' + str(stockModel.article) + '\n')
        file.writelines('stock: ' + str(stockModel.stock) + '\n')
        file.writelines('\n')

    file.close()

# Пока костыль, потом посмотреть доработать


def setInfoInFile(infoModels) -> None:
    # path = 'E:\\Wildberries\\API\\WildbberiesData\\DataTest'
    path = r'C:\Users\Lenovo\Downloads\01_Текущие'
    if not os.path.exists(path):
        createCatalog(path)

    file = open(path + '\\infoTestResult', 'w', encoding='utf-8')

    for infoModel in infoModels:
        file.writelines('nmId: ' + str(infoModel.nmId) + '\n')
        file.writelines('price: ' + str(infoModel.price) + '\n')
        file.writelines('discount: ' + str(infoModel.discount) + '\n')
        file.writelines('promoCode: ' + str(infoModel.promoCode) + '\n')
        file.writelines('\n')

    file.close()

# Пока костыль, потом посмотреть доработать




def createCatalog(path):
    try:
        os.mkdir(path)
    except OSError:
        print("Создать директорию %s не удалось" % path)
    else:
        print("Успешно создана директория %s " % path)