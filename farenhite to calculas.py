# Prompt the user to enter a temperature in Fahrenheit
degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert the temperature to Celsius using the given formula
degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

# Print the result with the conversion
print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")
