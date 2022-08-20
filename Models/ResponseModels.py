# Модель сделок
class DealModel:
    def __init__(self, json) -> None:
        self.orderId = json['orderId']              # Идентификатор заказа
        self.dateCreated = json['dateCreated']      # Дата создания заказа (RFC3339)
        self.orderUID = json['orderUID']            # Идентификатор транзакции для группировки заказов
        self.rid = json['rid']                      # Уникальный идентификатор вещи, разный у одинаковых chrt_id
        self.barcode = json['barcode']              # Штрихкод товара
        self.barcodes = json['barcodes']              # Массив штрихкодов товара
        self.scOfficesNames = json['scOfficesNames']              # Склад доставки
        self.chrtId = json['chrtId']                                 # Идентификатор артикула
        self.pid = json['pid']                                 # Идентификатор ПВЗ/магазина, куда необходимо доставить заказ (если применимо)
        self.wbWhId = json['wbWhId']                                 # Идентификатор склада поставщика, на который пришел заказ
        self.userStatus = json['userStatus']             # Статус со стороны клиента (1 - отмена клиента, 2 - доставлен, 3 - возврат, 4 - ожидает, 5 - брак)
        self.storeId = json['storeId']             # Идентификатор склада WB, на который заказ должен быть доставлен
        self.totalPrice = json['totalPrice']             # Стоимость товара с учетом скидок в копейках!
        self.convertedPrice = json['convertedPrice']             # Цена продажи с учетом скидок, сконвертированная в рубли по курсу на момент создания заказа
        self.deliveryType = json['deliveryType']             # Тип доставки (1 - обычная доставка, 2 - доставка силами поставщика)
        self.currencyCode = json['currencyCode']             # Код валюты (51 - Армянский драм, 398 - Казахский тенге, 417 - Киргизский сом, 643 - Российский рубль, 840 - Доллар США, 933 - Белорусский рубль, 974 - Белорусский рубль)
        self.status = json['status']             # Статус заказа (0 - новый заказ, 1 - принятый заказ, 2 - сборочное задание завершено, 3 - сборочное задание отклонено, 5 - На доставке курьером, 6 - Курьер довез и клиент принял товар, 7 - Клиент не принял товар, 8 - Товар для самовывоза из магазина принят к работе, 9 - Товар для самовывоза из магазина готов к выдаче)
        self.officeAddress = json['officeAddress']             # Адрес ПВЗ/магазина, куда необходимо доставить заказ
        self.deliveryAddress = json['deliveryAddress']             # Адрес клиента для доставки
        self.province = json['deliveryAddressDetails']['province']             # Область (example: Челябинская область)
        self.area = json['deliveryAddressDetails']['area']             # Район (example: Челябинск)
        self.city = json['deliveryAddressDetails']['city']             # Город (example: Челябинск)
        self.street = json['deliveryAddressDetails']['street']             # Улица (example: 51-я улица Арабкира)
        self.home = json['deliveryAddressDetails']['home']             # Номер дома (example: 10А)
        self.flat = json['deliveryAddressDetails']['flat']             # Номер квартиры (example: 42)
        self.entrance = json['deliveryAddressDetails']['entrance']             # Подъезд (example: 3)
        self.longitude = json['deliveryAddressDetails']['longitude']             # Координата долготы (example: 44.519068)
        self.latitude = json['deliveryAddressDetails']['latitude']             # Координата широты (example: 40.20192)
        self.userInfoFio = json['userInfo']['fio']                            # ФИО
        self.userInfoEmail = json['userInfo']['email']                            #
        self.userInfoPhone = json['userInfo']['phone']                            #



class StockModel:
    def __init__(self, json) -> None:
        self.subject = json['subject']          # Категория
        self.brand = json['brand']              # Бренд
        self.name = json['name']                # Наименование
        self.size= json['size']                 # Размер
        self.barcode = json['barcode']          # Штрихкод
        self.article = json['article']          # Артикул поставщика
        self.stock = json['stock']              # Остаток
        self.warehouseId = json['warehouseId']  # ID склада
        self.id = json['id']                    # Идентификатор товара
        self.chrtId = json['chrtId']            # Идентификатор артикула
        self.nmId = json['nmId']                # номенклатура



class InfoModel:
    def __init__(self, json) -> None:
        self.nmId = json['nmId']                    # номенклатура
        self.price = json['price']                  # Цена за единицу
        self.discount = json['discount']            # Скидка
        self.promoCode = json['promoCode']          # Промокод


class WarehousesModel:
    def __init__(self, json) -> None:
        self.name = json['name']  # Наименование склада
        self.id = json['id']     # ID склада

