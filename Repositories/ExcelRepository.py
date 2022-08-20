import pandas as pd

# Подумать, куда вынести отсюда имена как константы
# В принципе, уже сейчас думать над документацией проекта
def writeDataFramesInExcel(dealModels):
    writer = pd.ExcelWriter('./result.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    dealDataFrame = _getDataFrameByDealModels(dealModels)
    dataSheets = {'dealResult': dealDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()

# Уйти потом от этого
# Либо, написать нормальный маппер
def _getDataFrameByDealModels(dealModels):
    orderIdList = []
    dateCreatedList = []
    orderUIDList = []
    ridList = []
    barcodeList = []
    barcodesList = []
    scOfficesNamesList = []
    chrtIdList = []
    pidList = []
    wbWhIdList = []
    userStatusList = []
    storeIdList = []
    totalPriceList = []
    convertedPriceList = []
    deliveryTypeList = []
    currencyCodeList = []
    statusList = []
    officeAddressList = []
    deliveryAddressList = []
    provinceList = []
    areaList = []
    cityList = []
    streetList = []
    homeList = []
    flatList = []
    entranceList = []
    longitudeList = []
    latitudeList = []
    userInfoFioList = []
    userInfoEmailList = []
    userInfoPhoneList = []


    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for dealModel in dealModels:
        orderIdList.append(dealModel.orderId)
        dateCreatedList.append(dealModel.dateCreated)
        orderUIDList.append(dealModel.orderUID)
        ridList.append(dealModel.rid)
        barcodeList.append(dealModel.barcode)
        barcodesList.append(dealModel.barcodes)
        scOfficesNamesList.append(dealModel.scOfficesNames)
        chrtIdList.append(dealModel.chrtId)
        pidList.append(dealModel.pid)
        wbWhIdList.append(dealModel.wbWhId)
        userStatusList.append(dealModel.userStatus)
        storeIdList.append(dealModel.storeId)
        totalPriceList.append(dealModel.totalPrice)
        convertedPriceList.append(dealModel.convertedPrice)
        deliveryTypeList.append(dealModel.deliveryType)
        currencyCodeList.append(dealModel.currencyCode)
        statusList.append(dealModel.status)
        officeAddressList.append(dealModel.officeAddress)
        deliveryAddressList.append(dealModel.deliveryAddress)
        provinceList.append(dealModel.province)
        areaList.append(dealModel.area)
        cityList.append(dealModel.city)
        streetList.append(dealModel.street)
        homeList.append(dealModel.home)
        flatList.append(dealModel.flat)
        entranceList.append(dealModel.entrance)
        longitudeList.append(dealModel.longitude)
        latitudeList.append(dealModel.latitude)
        userInfoFioList.append(dealModel.userInfoFio)
        userInfoEmailList.append(dealModel.userInfoEmail)
        userInfoPhoneList.append(dealModel.userInfoPhone)


    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame({
                 'orderId': orderIdList,
                 'dateCreated': dateCreatedList,
                 'orderUID': orderUIDList,
                 'rid': ridList,
                 'barcode': barcodeList,
                 'barcodes': barcodesList,
                 'scOfficesNames': scOfficesNamesList,
                 'chrtId': chrtIdList,
                 'pid': pidList,
                 'wbWhId': wbWhIdList,
                 'userStatus': userStatusList,
                 'storeId': storeIdList,
                 'totalPrice': totalPriceList,
                 'convertedPrice': convertedPriceList,
                 'deliveryType': deliveryTypeList,
                 'currencyCode': currencyCodeList,
                 'status': statusList,
                 'officeAddress': officeAddressList,
                 'deliveryAddress': deliveryAddressList,
                 'province': provinceList,
                 'area': areaList,
                 'city': cityList,
                 'street': streetList,
                 'home': homeList,
                 'flat': flatList,
                 'entrance': entranceList,
                 'longitude': longitudeList,
                 'latitude': latitudeList,
                 'userInfoFio': userInfoFioList,
                 'userInfoEmail': userInfoEmailList,
                 'userInfoPhone': userInfoPhoneList,

                              })

    return dataFrame



def writeStockDataFramesInExcel(stockModels):
    writer = pd.ExcelWriter('./stockResult.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    stockDataFrame = _getStockDataFrameByDealModels(stockModels)
    dataSheets = {'stockResult': stockDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()

# Уйти потом от этого
# Либо, написать нормальный маппер

def _getStockDataFrameByDealModels(stockModels):
    subjectList = []
    brandList = []
    nameList = []
    sizeList = []
    barcodeList = []
    articleList = []
    stockList = []
    warehouseIdList = []
    idList = []
    chrtIdList = []
    nmIdCreatedList = []

    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for stockModel in stockModels:
        subjectList.append(stockModel.subject)
        brandList.append(stockModel.brand)
        nameList.append(stockModel.name)
        sizeList.append(stockModel.size)
        barcodeList.append(stockModel.barcode)
        articleList.append(stockModel.article)
        stockList.append(stockModel.stock)
        warehouseIdList.append(stockModel.warehouseId)
        idList.append(stockModel.id)
        chrtIdList.append(stockModel.chrtId)
        nmIdCreatedList.append(stockModel.nmId)

    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame({
                'subject': subjectList,
                'brand': brandList,
                'name': nameList,
                'size': sizeList,
                'barcode': barcodeList,
                 'article': articleList,
                 'stock': stockList,
                'warehouseId': warehouseIdList,
                'id': idList,
                'chrtId': chrtIdList,
                 'nmIdCreated': nmIdCreatedList,
                 })

    return dataFrame


def writeInfoDataFramesInExcel(infoModels):
    writer = pd.ExcelWriter('./infoResult.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    infoDataFrame = _getInfoDataFrameByDealModels(infoModels)
    dataSheets = {'infoResult': infoDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()

# Уйти потом от этого
# Либо, написать нормальный маппер

def _getInfoDataFrameByDealModels(infoModels):
    nmIdCreatedList = []
    priceList = []
    discountList = []
    promoCodeList = []



    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for infoModel in infoModels:
        nmIdCreatedList.append(infoModel.nmId)
        priceList.append(infoModel.price)
        discountList.append(infoModel.discount)
        promoCodeList.append(infoModel.promoCode)



    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame({'nmIdCreated': nmIdCreatedList,
                 'price': priceList,
                 'discount': discountList,
                 'promoCode': promoCodeList})

    return dataFrame



def writeWarehousesDataFramesInExcel(warehousesModels):
    writer = pd.ExcelWriter('./warehousesResult.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    warehousesDataFrame = _getWarehousesDataFrameByDealModels(warehousesModels)
    dataSheets = {'warehousesResult': warehousesDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()

# Уйти потом от этого
# Либо, написать нормальный маппер

def _getWarehousesDataFrameByDealModels(warehousesModels):
    nameList = []
    idList = []


    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for warehousesModel in warehousesModels:
        nameList.append(warehousesModel.name)
        idList.append(warehousesModel.id)

    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame({
                'name': nameList,
                 'id': idList,
                })

    return dataFrame
