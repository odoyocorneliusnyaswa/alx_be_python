# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
CONVERSION_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius using global conversion factor"""
    celsius = (fahrenheit - CONVERSION_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit using global conversion factor"""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + CONVERSION_OFFSET
    return fahrenheit

def main():
    print("Temperature Conversion Tool")
    print("--------------------------")
    
    try:
        # Get user input
        temp_input = input("Enter temperature (e.g., '32 C' or '89.5 F'): ").strip().upper()
        
        if not temp_input:
            raise ValueError("No input provided.")
        
        # Split into value and unit
        parts = temp_input.split()
        if len(parts) != 2:
            raise ValueError("Invalid format. Please enter temperature and unit (e.g., '32 C' or '89.5 F').")
        
        temp_value, temp_unit = parts
        temp_value = float(temp_value)
        
        # Perform conversion based on unit
        if temp_unit == 'C':
            converted_temp = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {converted_temp:.2f}°F")
        elif temp_unit == 'F':
            converted_temp = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {converted_temp:.2f}°C")
        else:
            raise ValueError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
