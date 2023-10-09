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

# unit = input('Enter the appropriate unit from the following (degrees F, degrees C, Inches, cm):  ')
# value = float(input('Enter input number: '))

# converter = Converter(value, unit)
# conversion_type = input('Select (T) for temperature or (L) for length:  ')
# result = converter.convert(conversion_type)

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

# # <<<<<<<<<<<<<<Email Slicer<<<<<<<<<<<<<

# import re
# #promopt user for input
# email = input("Enter your email: ")
# #expression matching
# pattern = r"([\w]+)@([\w]+\.[\w]+)"
# #pattern matching for username and domain name
# match = re.match(pattern,email)
# #extraction
# username  =  match.group(1)
# domain_name = match.group(2)
# #displaying the results
# print("Username: ", username)
# print("Domain name: ",domain_name)


from forex_python.converter import CurrencyRates

# #Converts a currency from one currency to another
# def convert_currency(from_currency, to_currency, amount):
#     c = CurrencyRates()
#     conversion_rate = c.get_rate(from_currency, to_currency)
#     converted_amount = amount * conversion_rate
#     return converted_amount, to_currency

# # Prompting user for input
# amount = float(input('Enter the amount: '))
# from_currency  = input("From Currency: ").upper
# to_currency = input("To Currency: ").upper()

# # Checking for invalid currency codes
# if from_currency not in CurrencyRates.currencies:
#     raise ValueError(f"Invalid currency code: {from_currency}")
# if to_currency not in CurrencyRates.currencies:
#     raise ValueError(f"Invalid currency code: {to_currency}")
# result = convert_currency(from_currency, to_currency, amount)
# print(f"From {from_currency}, To {to_currency}, Amount {amount}")
# print(f"Converted amount: {converted_amount} {to_currency}")
from forex_python.converter import CurrencyRates

from forex_python.converter import CurrencyRates

# Define conversion function
def convert_currency(from_currency, to_currency, amount):
  """Converts a currency from one currency to another.

  Args:
    from_currency: The currency code of the source currency.
    to_currency: The currency code of the target currency.
    amount: The amount to be converted.

  Returns:
    A tuple containing the converted amount and the currency code of the target currency, or an error string.
  """
  c = CurrencyRates()

  # Checking for invalid currency codes
  if from_currency not in c.get_rates('USD'):
    return (f"Invalid currency code: {from_currency}",)
  if to_currency not in c.get_rates('USD'):
    return (f"Invalid currency code: {to_currency}",)

  conversion_rate = c.get_rate(from_currency, to_currency)
  converted_amount = amount * conversion_rate
  return converted_amount, to_currency

# Prompting user for input
amount = float(input('Enter the amount: '))
from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()

# Converting the currency
result = convert_currency(from_currency, to_currency, amount)

# Check if the conversion was successful
if len(result) == 1:
  # An error occurred
  print(result[0])
else:
  # Conversion was successful
  converted_amount, to_currency = result

  # Printing the result
  print(f"From {from_currency}, To {to_currency}, Amount {amount}")
  print(f"Converted amount: {converted_amount} {to_currency}")

