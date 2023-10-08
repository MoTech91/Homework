# <<<<<<<<<<<<<<<<<<<<<<<<<unsing loops<<<<<<<<<<<<<<<<<<<<<<<
# import datetime 

# # prompting the user for inputs
# start_date= input("Enter STARTING date as YYYY-MM-DD': ")
# end_date= input("Enter END date as YYYY-MM-DD: ")

# #converting strings using strptime method 
# s_date= datetime.datetime.strptime(start_date, '%Y-%m-%d')
# e_date= datetime.datetime.strptime(end_date, '%Y-%m-%d')

# # calculating delta
# delta= e_date - s_date

# print("The difference between", s_date, "and", e_date, "is", delta)

#tempreture convertor

#prompt user for type of coversion (Temp/Measurement)

# calc = input('Select (T) for temp_calc or (L) for length_calc:  ')
# unit = input('Enter the appropriate unit from the following (degrees F, degrees C, Inches, cm ):  ')


# if calc == 'T':
#     temp_calc = round(float(input('Enter input number: ')))
#     if unit == 'degrees C':
#         result= (round(temp_calc) * (9/5)+32)
#     elif unit == 'degrees F':
#         result=round((temp_calc - 32) * (5/9))
#     else:
#         print("Invalid input. Please try again.")
#         exit()
#     calc= ' '
# elif calc == 'L':
#   length_calc = float(input('Enter input number: '))
#   if unit == 'Inches':
#     result = round(length_calc * 2.54)
#   elif unit == 'cm':
#     result = round(length_calc % 2.54)
#   else:
#     print('Invalid unit.')
#     exit()
#   calc= ' '
# else:
#   print('Invalid conversion type.')
#   exit()

# print(f'The converted value is {result} in {unit}.')

#>>>>>>>>>>>Unsing OOP>>>>>>>>>>>>
# class Converter:
#     def __init__(self, value, unit):
#         self.value = value
#         self.unit = unit

#     def convert_temperature(self):
#         if self.unit == 'degrees C':
#             return (self.value * (9/5)) + 32
#         elif self.unit == 'degrees F':
#             return (self.value - 32) * (5/9)
#         else:
#             return "Invalid temperature unit."

#     def convert_length(self):
#         if self.unit == 'Inches':
#             return self.value * 2.54
#         elif self.unit == 'cm':
#             return self.value / 2.54
#         else:
#             return "Invalid length unit."

#     def convert(self, conversion_type):
#         if conversion_type == 'T':
#             return self.convert_temperature()
#         elif conversion_type == 'L':
#             return self.convert_length()
#         else:
#             return "Invalid conversion type."

# calc = input('Select (T) for temp_calc or (L) for length_calc:  ')
# unit = input('Enter the appropriate unit from the following (degrees F, degrees C, Inches, cm):  ')
# value = float(input('Enter input number: '))

# converter = Converter(value, unit)
# result = converter.convert(calc)

# print(f'The converted value is {result} in {unit}.')


#>>>>>>>>>>>>>>>>>Using functional programing<<<<<<<<<

# def convert_temperature(value, unit):
#     if unit == 'degrees C':
#         return value * (9/5) + 32
#     elif unit == 'degrees F':
#         return (value - 32) * (5/9)
#     else:
#         return "Invalid temperature unit."

# def convert_length(value, unit):
#     if unit == 'Inches':
#         return value * 2.54
#     elif unit == 'cm':
#         return value / 2.54
#     else:
#         return "Invalid length unit."

# def convert(value, unit, conversion_type):
#     if conversion_type == 'T':
#         return convert_temperature(value, unit)
#     elif conversion_type == 'L':
#         return convert_length(value, unit)
#     else:
#         return "Invalid conversion type."

# calc = input('Select (T) for temp_calc or (L) for length_calc:  ')
# unit = input('Enter the appropriate unit from the following (degrees F, degrees C, Inches, cm):  ')
# value = float(input('Enter input number: '))

# result = convert(value, unit, calc)

# print(f'The converted value is {result} in {unit}.')