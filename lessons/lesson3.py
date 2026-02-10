# # Encapsulation
#
# import random
#
# class BankAccount:
#     def __init__(self, login, balance, password):
#         self.login = login
#         self._balance = balance
#         self.__password = password
#
#     def m_login(self, login, password):
#         if self.login == login and self.__password == password:
#             return print('Ok!!')
#         else:
#             return print('Incorrect login or password')
#
#     def __random_pass(self):
#         return random.randint(1, 10)
#
#     def reset_pass(self, login):
#         if login == self.login:
#             self.__password = self.__random_pass()
#         else:
#             print("Error!!")
#
#     def get_balance(self):
#         return self._balance
#
# ardager = BankAccount("Ardager", 1000, "123321")
# # ardager.m_login("Ardager", "123321")
#
# print(ardager.get_balance())
#
# print(ardager._BankAccount__password)
# ardager.reset_pass("Ardager")
# print(ardager._BankAccount__password)

# Abstraction

from abc import ABC, abstractmethod

# otp - one time password
# Abstract class
class SendOTP(ABC):

    @abstractmethod
    def send_otp_to_phone(self):
        pass

    @abstractmethod
    def send_otp_to_email(self):
        pass

class SendOTPKG(SendOTP):
    def send_otp_to_phone(self):
        send = ''''
        <Phone>+996779280699</Phone>
        <Text>Your temporary password 5555</Text>
        '''
        print(send)

    def send_otp_to_email(self):
        print("sending otp by email")

class SendOTPRU(SendOTP):
    def send_otp_to_phone(self):
        send = {
            "phone": "+79652101537",
            "text": "Your temporary password 5555"
        }
        print(send)

    def send_otp_to_email(self):
        print("sending otp by email")


otp_kg = SendOTPKG()
otp_ru = SendOTPRU()

