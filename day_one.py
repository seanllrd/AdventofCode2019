# Functions to calculate fuel requirements
def calculate_fuel(mass: int) -> int:
    return (mass // 3) - 2


def sum_fuel(fuel: list) -> int:
    return sum(fuel)


def part_one():
    # Grab values from csv file and run calculations
    with open('module_masses.txt') as massfile:
        masses = massfile.read()
        module_masses = [int(mass) for mass in masses.split()]

    module_fuel_requirements = []
    for mass in module_masses:
        module_fuel_requirements.append(calculate_fuel(mass))

    total_fuel = sum_fuel(module_fuel_requirements)
    print(f"Total fuel for all modules: {total_fuel}")


def part_two():
    # Grab values from csv file
    with open('module_masses.txt') as massfile:
        masses = massfile.read()
        module_masses = [int(mass) for mass in masses.split()]

    # Calculate fuel requirements
    module_fuel_requirements = []
    for mass in module_masses:
        total = 0
        # Calculate fuel requirements for the module
        initial_fuel = calculate_fuel(mass)
        # Calculate fuel requirement for the fuel until no more fuel is needed
        total += initial_fuel
        while initial_fuel > 0:
            extra_fuel = calculate_fuel(initial_fuel)
            if extra_fuel > 0:
                total += extra_fuel
            initial_fuel = extra_fuel
        module_fuel_requirements.append(total)

    # Calculate total fuel
    total_fuel = sum_fuel(module_fuel_requirements)
    print(f"Total fuel for all modules and fuel requirements: {total_fuel}")


part_one()
part_two()
