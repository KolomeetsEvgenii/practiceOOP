from datetime import datetime


class Store:
    def __init__(self, address):
        self.address: str = address

    def __is_open(self, date) -> bool:
        # Метод __is_open() в родительском классе всегда возвращает False,
        # это "код-заглушка", метод, предназначенный для переопределения
        # в дочерних классах.
        # Не переопределяйте содержимое этого метода.
        return False

    def get_info(self, text_date) -> str:
        # С помощью шаблона даты преобразуйте строку date_str в объект даты:
        date_object = datetime.strptime(text_date, "%d.%m.%Y").date()

        # Передайте в метод __is_open() объект даты date_object и определите,
        # работает ли магазин в указанную дату.
        # В зависимости от результата будет выбрано значение
        # для переменной info.
        if self.__is_open(date_object):
            info = 'работает'
        else:
            info = 'не работает'
        return f'Магазин по адресу {self.address} {text_date} {info}'


class MiniStore(Store):
    # Переопределите метод __is_open().
    # Обратите внимание на имя метода/name mangling
    def _Store__is_open(self, date: datetime) -> bool:
        if (date.weekday() == 5) or (date.weekday() == 6):
            return False
        else:
            return True


class WeekendStore(Store):
    # Переопределите метод __is_open().
    # Обратите внимание на имя метода/name mangling
    def _Store__is_open(self, date: datetime) -> bool:
        if (date.weekday() == 5) or (date.weekday() == 6):
            return True
        else:
            return True


class NonStopStore(Store):
    # Переопределите метод __is_open().
    # Обратите внимание на имя метода/name mangling
    def _Store__is_open(self, date: datetime) -> bool:
        return True


mini_store = MiniStore('Улица Немига, 57')
print(mini_store.get_info('29.03.2024'))
print(mini_store.get_info('30.03.2024'))

weekend_store = WeekendStore('Улица Толе би, 321')
print(weekend_store.get_info('29.03.2024'))
print(weekend_store.get_info('30.03.2024'))

non_stop_store = NonStopStore('Улица Арбат, 60')
print(non_stop_store.get_info('29.03.2024'))
print(non_stop_store.get_info('30.03.2024'))




















# class Product:
#     # Опишите инициализатор класса.
#     # Инициализатор должен принять на вход
#     # название (name) и количество (quantity) товара.
#     # В теле инициализатора задайте соответствующие атрибуты экземпляра класса.
#     def __init__(self, name, quantity):
#         self.name = name
#         self.quantity = quantity

#     def get_basic_info(self):
#         return f'{self.name} (в наличии: {self.quantity})'

#     def get_full_info(self):
#         pass


# class Kettlebell(Product):

#     def __init__(self, name, quantity, weight):
#         super().__init__(name, quantity)
#         self.weight = weight

#     def get_full_info(self):
#         return f'{super().get_basic_info()}. Вес: {self.weight} кг'


# class Clothing(Product):
#     def __init__(self, name, quantity, size):
#         super().__init__(name, quantity)
#         self.size = size

#     def get_full_info(self):
#         return f'{super().get_basic_info()}. Размер: {self.size} кг'


# # Для проверки вашего кода создадим пару объектов...
# small_kettlebell = Kettlebell('Гиря малая', 15, 2)
# shirt = Clothing('Футболка', 5, 'L')

# # ...и вызовем их методы:
# print(small_kettlebell.get_full_info())
# print(shirt.get_full_info())


# # class Phone:
# #     line_type: str = 'проводной'

# #     def __init__(self, dual_type_value: str | None = None) -> None:
# #         self.dual_type_value = dual_type_value
# #         self._serial_number = id(dual_type_value)

# #     def ring(self):
# #         print('Дзынь!!!')

# #     def call(self, phone_number: str):
# #         print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')

# #     def get_missed_calls(self):
# #         print('Запрос количества пропущенных вызовов.')

# #     def dial_type_upgrade(self, new_dual_type_value):
# #         self.dual_type_value = new_dual_type_value


# # class MobilePhone(Phone):
# #     line_type = 'беспроводной'
# #     battery_type = 'Li-ion'

# #     def __init__(self, dual_type_value, network_type) -> None:
# #         super().__init__(dual_type_value)
# #         self.__network_type = network_type

# #     def ring(self):
# #         print('Дзынь!!!-Дзынь!!!')

# #     def start_game(self):
# #         print('Игра запущена!')

# #     def get_info(self):
# #         print(f'Serial No: {self._serial_number}, Type network: {self.__network_type}')


# # mobile_phone = MobilePhone('сенсорный', 'LTE')
# # rotary_phone = Phone('дисковый')
# # mobile_phone_1 = Phone('дисковый')
# # mobile_phone_2 = MobilePhone('сенсорный', 'LTE')

# # mobile_phone_2.get_info()
# # print(mobile_phone_2.__network_type)


# # class Employee:
# #     vacation_days: int = 28

# #     def __init__(self, first_name: str, second_name: str, gender: str):
# #         self.first_name = first_name
# #         self.second_name = second_name
# #         self.gender = gender
# #         self.remaining_vacation_days = Employee.vacation_days

# #     def consume_vacation(self, wasted_vacation_days: int):
# #         self.remaining_vacation_days = self.remaining_vacation_days - wasted_vacation_days

# #     def get_vacation_details(self):
# #         return f'Остаток отпускных дней: {self.remaining_vacation_days}.'
    
# #     def __generate_employee_id(self):
# #         self._employee_id = hash(self.first_name + self.second_name + self.gender)

# class Employee:
#     vacation_days: int = 28

#     def __init__(
#         self,
#         first_name: str,
#         last_name: str,
#         gender: str,
#     ):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.gender = gender
#         self.remaining_vacation_days = self.vacation_days
#         self._employee_id = self.__generate_employee_id()

#     def consume_vacation(self, days: int):
#         self.remaining_vacation_days -= days

#     def get_remaining_vacation_days(self) -> int:
#         return self.remaining_vacation_days

#     def __generate_employee_id(self):
#         return hash(self.first_name + self.last_name + self.gender)
    
    


# class OfficeEmployee(Employee):
#     def __init__(
#         self,
#         first_name: str,
#         last_name: str,
#         gender: str,
#         worker_class: int,
#         salary
#     ):
#         super().__init__(first_name, last_name, gender)
#         self.worker_class = worker_class
#         self.__salary = salary
#         self.remaining_vacation_days = self.vacation_days + self.worker_class * 2

#     def consume_vacation(self, days: int):
#         self.remaining_vacation_days -= days

#     def get_vacation_payment(self, vacation_days):
#         return int(self.__salary/60 * vacation_days)
    

# office_employee = OfficeEmployee(
#     first_name='Иван',
#     last_name='Иванов',
#     gender='м',
#     worker_class=2,
#     salary=45000
# )


# vacation_days = 10

# office_employee.consume_vacation(vacation_days)

# remaining_days = office_employee.get_remaining_vacation_days()
# print(f'У сотрудника осталось {remaining_days} дн. отпуска.')

# vacation_payment = office_employee.get_vacation_payment(vacation_days)
# print(f'За {vacation_days} дн. отпуска сотрудник получит {vacation_payment} руб.')

# print(office_employee.employee_id)
# # class FullTimeEmployee(Employee):

# #     def get_unpaid_vacation(self, data_start, days):
# #         self.data_start = data_start
# #         self.days = days
# #         return f'Начало неоплачиваемого отпуска: {self.data_start}, продолжительность: {self.days} дней.'


# # class PartTimeEmployee(Employee):
# #     vacation_days: int = 14








# # class CipherMaster:
# #     # Не изменяйте и не перемещайте эту переменную
# #     alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# #     def process_text(self, text, shift, is_encrypt):
# #         # Метод должен возвращать зашифрованный текст
# #         # с учетом переданного смещения shift.
# #         self.text = text
# #         self.shift = shift
# #         self.is_encrypt = is_encrypt
# #         result = []
# #         for letter in self.text:
# #             if letter.lower() not in self.alphabet:
# #                 result.append(letter)
# #             else:
# #                 if self.is_encrypt:
# #                     index = self.alphabet.find(letter.lower()) + self.shift
# #                 else:
# #                     index = self.alphabet.find(letter.lower()) - self.shift
# #                 if index > 32:
# #                     result.append(self.alphabet[index % 33])
# #                 else:
# #                     result.append(self.alphabet[index])
# #             ...  # здесь ваш код
# #         return ''.join(result)


# # cipher_master = CipherMaster()
# # print(cipher_master.process_text(
# #     text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
# #     shift=2,
# #     is_encrypt=True
# # ))
# # print(cipher_master.process_text(
# #     text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
# #     shift=-3,
# #     is_encrypt=False
# # ))
