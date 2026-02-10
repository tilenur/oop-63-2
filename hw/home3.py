# Часть 1. Инкапсуляция

import random

class UserAccount:
    def __init__(self, username, score, pin):
        self.username = username
        self._score = score
        self.__pin = pin

    def access_check(self, username, pin):
        if self.username == username and self.__pin == pin:
            return True
        else:
            return False

    def __random_pin(self):
        return random.randint(1,10)

    def reset_pin(self, username, old_pin):
        if self.access_check(username, old_pin):
            self.__pin = self.__random_pin()
            print("PIN successfully reset")
        else:
            print("Access denied")

    def get_score(self):
        return self._score

tilenur = UserAccount("tilenur", 9999, "25121993")

# правильная проверка
if tilenur.access_check("tilenur", "25121993"):
    print("Login successful")
else:
    print("Login failed")

# попытка прямого доступа (должна упасть)
try:
    print(tilenur.__pin)
except AttributeError:
    print("Cannot access private attribute directly")

# смена PIN через метод
tilenur.reset_pin("tilenur", "25121993")

print(tilenur._UserAccount__pin)

# Часть 2. Абстракция

import random
from abc import ABC, abstractmethod

class SendMessage(ABC):

    def random_pass(self):
        return random.randint(1, 100)

    @abstractmethod
    def send_to_phone(self):
        pass

    @abstractmethod
    def send_to_email(self):
        pass


class KGSendMessage(SendMessage):

    def send_to_phone(self):
        temporary_pass = self.random_pass()
        send = f'''
        <Phone>+996779280699</Phone>
        <Text>Your temporary password {temporary_pass}</Text>
        '''
        print(send)

    def send_to_email(self):
        print("sending otp by email")


class RUSendMessage(SendMessage):

    def send_to_phone(self):
        temporary_pass = self.random_pass()
        send = {
            "phone": "+79652101537",
            "text": f"Your temporary password {temporary_pass}"
        }
        print(send)

    def send_to_email(self):
        print("sending otp by email")


message_kg = KGSendMessage()
message_ru = RUSendMessage()

message_kg.send_to_phone()
message_ru.send_to_phone()
