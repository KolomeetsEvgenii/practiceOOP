# class Phone:
#     line_type: str = 'проводной'

#     def __init__(self, dual_type_value: str | None = None) -> None:
#         self.dual_type_value = dual_type_value

#     def ring(self):
#         print('Дзынь!!!')

#     def call(self, phone_number: str):
#         print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')

#     def get_missed_calls(self):
#         print('Запрос количества пропущенных вызовов.')

#     def dial_type_upgrade(self, new_dual_type_value):
#         self.dual_type_value = new_dual_type_value


# rotary_phone = Phone('дисковый')
# rotary_phone.get_missed_calls()
# rotary_phone.dial_type_upgrade('кнопочный')
# print(rotary_phone)


# class Employee:
#     vacation_days: int = 28

#     def __init__(self, first_name: str, second_name: str, gender: str):
#         self.first_name = first_name
#         self.second_name = second_name
#         self.gender = gender
#         self.remaining_vacation_days = Employee.vacation_days

#     def consume_vacation(self, wasted_vacation_days: int):
#         self.remaining_vacation_days = self.remaining_vacation_days - wasted_vacation_days

#     def get_vacation_details(self):
#         return f'Остаток отпускных дней: {self.remaining_vacation_days}.'

# # employee1 = Employee('Роберт', 'Крузо', 'м')
# # employee2 = Employee('Крузо', 'Роберт', 'м')
# # print(f'Имя: {employee1.first_name}, Фамилия: {employee1.second_name}, Пол: {employee1.gender}, Отпускных дней в году: {employee1.vacation_days}.')
# # print(f'Имя: {employee2.first_name}, Фамилия: {employee2.second_name}, Пол: {employee2.gender}, Отпускных дней в году: {employee2.vacation_days}.')


# employee = Employee('Роберт', 'Крузо', 'м')
# employee.consume_vacation(7)
# print(employee.get_vacation_details())
class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        self.text = text
        self.shift = shift
        self.is_encrypt = is_encrypt
        result = []
        for letter in self.text:
            if letter.lower() not in self.alphabet:
                result.append(letter)
            else:
                if self.is_encrypt:
                    index = self.alphabet.find(letter.lower()) + self.shift
                else:
                    index = self.alphabet.find(letter.lower()) - self.shift
                if index > 32:
                    result.append(self.alphabet[index % 33])
                else:
                    result.append(self.alphabet[index])
            ...  # здесь ваш код
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))




# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


# def cipher(original_text, shift):
#     # Метод должен возвращать зашифрованный текст
#     # с учетом переданного смещения shift.
        
#     result = []
#     for letter in original_text:
#         if letter.lower() not in alphabet:
#             result.append(letter)
#         else:
#             index = alphabet.find(letter.lower()) + shift
#             if index > 32:
#                 result.append(alphabet[index % 33])
#             else:
#                 result.append(alphabet[index])
#     ...  # здесь ваш код
#     return print(''.join(result))

#     # def decipher(self, cipher_text, shift):
#     #     # Метод должен возвращать исходный текст
#     #     # с учётом переданного смещения shift.
#     #     result = []
#     #     for letter in cipher_text:
#     #         ...  # здесь ваш код
#     #     return ''.join(result)


# print(cipher(
#     original_text='сткънр тждюа д ъкцтрдвппро дкёж. мвижфуб, пву твуумтэнк!',
#     shift=-2
# ))
# # print(cipher_master.decipher(
# #     cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
# #     shift=-3
# # ))