#starting off with a PV=nRT calculator then moving on to add more chem calculators
import math
import sys
        
#TempF = float(input("What is the temp in fahrenheit: "))
#TempC = ((TempF - 32)*5)/9
#print(TempC)


print("\n--- Ideal Gas Law Calculator ---")
print("Formula: PV = nRT")
print("R = 0.08206 L·atm/(mol·K)")
print("Leave one field empty to solve for it.")

pressure_input = input("What is the Pressure(atm): ")
pressure = float(pressure_input) if pressure_input else None
volume_input = input("What is the Volume(L): ")
volume = float(volume_input) if volume_input else None
moles_input = input("What is the Moles(mol): ")
moles = float(moles_input) if moles_input else None
temp_input = input("What is the Temp(K): ")
temp = float(temp_input) if temp_input else None
R = .0821

if pressure is None:
    pressure = (moles * R * temp) / volume
    print(f"Result: {pressure:.4f} atm")
elif volume is None:
    volume = (moles * R * temp) / pressure
    print(f"Result: {volume:.4f} L")
elif moles is None:
    moles = (pressure * volume) / (R * temp)
    print(f"Result: {moles:.4f} mol")
elif temp is None:
    temp = (pressure * volume) / (moles * R)
    print(f"Result: {temp:.4f} K")