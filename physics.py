def calculate_force(mass):
    acceleration = 9.8
    force = mass * acceleration
    return force

print(calculate_force(float(input("enter mass:\n\n"))))