class Dog:
    def __init__(self):
        self.size = 0.5
        self.tail = 1
        self.is_running = True

    def talk(self):
        print("ГАВ!")

# Создаем три объекта класса Dog
dog1 = Dog()
dog2 = Dog()
dog3 = Dog()

class Video:
    def __init__(self):
        self.views = 0
        self.likes = 100
        self.subscribers = []
        self.is_published = True

    def subscribe(self):
        print("Вы успешно подписаны")
