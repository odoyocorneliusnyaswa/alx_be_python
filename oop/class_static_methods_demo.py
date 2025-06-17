from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

    # Demonstrating class attribute modification
    print("\nChanging calculation type...")
    Calculator.change_calculation_type("Basic Math Operations")
    
    # Showing the change affects all instances
    product_result2 = Calculator.multiply(3, 4)
    print(f"The new product is: {product_result2}")

if __name__ == "__main__":
    main()
