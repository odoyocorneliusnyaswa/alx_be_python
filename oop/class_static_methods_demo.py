class Calculator:
    """A calculator class demonstrating class and static methods"""
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Static method to add two numbers
        Args:
            a (float): First number
            b (float): Second number
        Returns:
            float: Sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """
        Class method to multiply two numbers
        Args:
            cls: Reference to the class
            a (float): First number
            b (float): Second number
        Returns:
            float: Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
    
    @classmethod
    def change_calculation_type(cls, new_type: str):
        """
        Class method to modify the class attribute
        Args:
            cls: Reference to the class
            new_type (str): New value for calculation_type
        """
        cls.calculation_type = new_type
