# from typing import 


# class Phone:
#     line_type:str = 'проводной'

#     def __init__(self, dual_type_value: str|None = None) -> None:
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
# print(rotary_phone.dual_type_value)



class Employee:
    vacation_days:int = 28


    def __init__(self, first_name: str, second_name:str, gender:str) -> None:
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days

    def consume_vacation(self, wasted_vacation_days):
        self.remaining_vacation_days = self.vacation_days - wasted_vacation_days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'

# employee1 = Employee('Роберт', 'Крузо', 'м')
# employee2 = Employee('Крузо', 'Роберт', 'м')
# print(f'Имя: {employee1.first_name}, Фамилия: {employee1.second_name}, Пол: {employee1.gender}, Отпускных дней в году: {employee1.vacation_days}.')
# print(f'Имя: {employee2.first_name}, Фамилия: {employee2.second_name}, Пол: {employee2.gender}, Отпускных дней в году: {employee2.vacation_days}.')

employee = Employee('Роберт', 'Крузо', 'м')
employee.consume_vacation(7)
print(employee.get_vacation_details())
# employee.consume_vacation(7)
# print(employee.get_vacation_details())
print(employee.remaining_vacation_days)
employee.consume_vacation(3)
print(employee.remaining_vacation_days)
print(employee.get_vacation_details())
