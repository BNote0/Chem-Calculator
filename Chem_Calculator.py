#starting off with a PV=nRT calculator then moving on to add more chem calculators
import math
import sys

class ChemCalculator:
    def __init__(self):
        self.calculators = {
            "Ideal Gas Law": self.ideal_gas_law,
            "Pressure Conversion": self.ideal_gas_law,  # Placeholder for pressure conversion
            # Add more calculators here as methods
        }

    def run(self):
        print("Welcome to the Chemistry Calculator!")
        print("Available calculators:")
        for name in self.calculators.keys():
            print(f"- {name}")
        
        choice = input("Select a calculator: ")
        if choice in self.calculators:
            self.calculators[choice]()
        else:
            print("Invalid choice. Exiting.")
            sys.exit(1)

    def ideal_gas_law(self):
        print("Ideal Gas Law Calculator (PV = nRT)")
        try:
            P = float(input("Enter pressure (P) in atm: "))
            V = float(input("Enter volume (V) in liters: "))
            n = float(input("Enter number of moles (n): "))
            R = 0.0821  # Ideal gas constant in L·atm/(K·mol)
            T = float(input("Enter temperature (T) in Kelvin: "))
            result = P * V / (n * R * T)
            print(f"The result of PV/nRT is: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    
    def pressure_conversion(self):
        print("Pressure Conversion Calculator")
        try:
            pressure = float(input("Enter pressure in atm: "))
            conversion_factor = 101.325  # atm to kPa
            converted_pressure = pressure * conversion_factor
            print(f"Pressure in kPa: {converted_pressure}")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")