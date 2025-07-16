"""Use Einstein’s formula
E = mc²
Where:
E = energy in joules
m = mass in kilograms (user input)
c = speed of light ≈ 300,000,000 m/s"""
# Define a function to calculate energy using Einstein's formula
def energy():
    #in this function, I want it to calc E(energy):
    #m = mass
    m = int(input("Enter mass in kilograms:"))
    #c = speed of light
    c = 300000000 # speed of light in m/s
    # Calculate energy using the formula E = mc^2
    E = m*c**2
    print(E)
energy()
# This function calculates the energy based on user input for mass
# and uses the speed of light as a constant.
