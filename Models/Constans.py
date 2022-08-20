class URLs:
    def __init__(self) -> None:
        self.baseURL = 'https://suppliers-api.wildberries.ru/'
        self.orderUrl = 'api/v2/orders'
        self.stocksUrl = 'api/v2/stocks'
        self.infoUrl = 'public/api/v1/info?quantity=0'
        self.warehousesUrl = 'api/v2/warehouses'

# Первое, что нужно убрать отсюда
# Или доработать
class Headers:
    def __init__(self) -> None:
        self.accept = 'accept'
        self.acceptValue = 'application/json'
        self.authorization = 'Authorization'

        # self.APIKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6IjhkZDIzYjVlLWU1YmYtNGUxMS1hZjRmLTk1NzI5YjhiMjg1NyJ9.f1Hz43nwXI5RIvJ9309oxsdUQjgxmIS4QiFc6rJVboQ'
        # self.APIKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6IjQ4NjVlNDAxLTRkMDktNGNhNy05NDI5LTcyZTY1MzhjZDBkOSJ9.RMSTeEd5C4MLI7lGyVyH8PVfXHK6QT7_X6oNRYiIBb4'
        self.APIKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6ImFjOTc0Y2Q4LTVjYzYtNDAwNC05N2VkLTc5NGRkMTBiNzI3MCJ9.V7zt7P1PSQOBB7R7-KtOjKrzC6X4tBObazmqiRENen0'

class OrderParameters:
    def __init__(self) -> None:
        self.dateStart = 'date_start'
        self.dateEnd = 'date_end'
        self.status = 'status'
        self.take = 'take'
        self.skip = 'skip'
        self.id = 'id'
        self.order = 'order'

# Вынести в конфиги, либо как-то еще избавиться от них
class PathsToFiles:
    def __init__(self) -> None:
        # self.catalogPath = 'E:\Wildberries\API\WildbberiesData'
        self.catalogPath = r'C:\Users\Lenovo\Downloads'
        self.dealPath = 'dealTest'