
class Phone:
    def call(self):
        print("Дзвінок")

class Camera:
    def photo(self):
        print("Фото зроблено")

class GPS:
    def location(self):
        print("Ваша геолокація")

class Smartphone(Phone, Camera, GPS):
    pass

phone = Smartphone()
phone.call()
phone.photo()
phone.location()
