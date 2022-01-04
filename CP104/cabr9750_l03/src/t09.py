"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-09-25"
------------------------------------------------------------------------
"""
PI = 3.14
container_diameter = float(input("Diameter of container base (cm): "))
container_radious = container_diameter/2
container_height = float(input("Height of container (cm): "))
material_cost = float(input("Cost of material ($/cm^2): "))
number_of_containers = int(input("Number of containers: "))

area_container = (2 * PI * container_radious * container_height) + (PI * (container_radious**2))
unit_price = area_container * material_cost
total_price = unit_price * number_of_containers

print("The cost of one container is: ${:,.2f}".format(unit_price))
print("The total cost of all containers is ${:,.2f}".format(total_price))

