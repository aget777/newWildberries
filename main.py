from Services import OrderService, StocksServise, InfoService, WarehousesService
from Repositories import FileRepository
from Repositories import ExcelRepository

if __name__ == '__main__':

    stockModels = StocksServise.getStockModels()
    infoModels = InfoService.getInfoModels()
    # warehousesModels = WarehousesService.getWarehousesModels()
    dealModels = OrderService.getDealModels()



    ExcelRepository.writeStockDataFramesInExcel(stockModels)
    ExcelRepository.writeInfoDataFramesInExcel(infoModels)
    # ExcelRepository.writeWarehousesDataFramesInExcel(warehousesModels)
    ExcelRepository.writeDataFramesInExcel(dealModels)
