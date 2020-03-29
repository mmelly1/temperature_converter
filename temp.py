#convert Celsius to Farenheit : farenheit = (celsius * 9/5) + 32
def converter(celsius):
    farenheit = (float(celsius) * 9/5) + 32
    message = str(celsius) + " degrees Celsius are " + str(farenheit) + " degrees Farenheit."
    return message

celsius = input("Enter a temperature in degrees Celsius: ")
print(converter(celsius))
