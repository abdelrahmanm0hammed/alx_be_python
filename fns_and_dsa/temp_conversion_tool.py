FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature = input("Enter the temperature to convert: ")

def convert_to_celsius(fahrenheit):
    celsius= (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print (f"{fahrenheit}F is {celsius}C")



def convert_to_fahrenheit(celsius):
    
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{temperature}C is {fahrenheit}F")


if temperature.isnumeric():
    temperature = int(temperature)
    tem_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

    if tem_type == "c":
        convert_to_fahrenheit(temperature)
    elif tem_type == "f":
        convert_to_celsius(temperature)
    else:
        print("invalid input")
else:
    print("Invalid temperature. Please enter a numeric value.")

