# QUESTION NO 1


class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

# Main program
def main():
    my_car = Car("ABC-123", 142)

    print("Car Information:")
    print("Registration Number:", my_car.registration_number)
    print("Maximum Speed:", my_car.maximum_speed, "km/h")
    print("Current Speed:", my_car.current_speed, "km/h")
    print("Travelled Distance:", my_car.travelled_distance, "km")

main()

# QUESTION NO 2

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change

        if self.current_speed < 0:
            self.current_speed = 0

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed


# Main program
def main():
    my_car = Car("ABC-123", 142)

    # Accelerations
    my_car.accelerate(30)   # +30 km/h
    my_car.accelerate(70)   # +70 km/h
    my_car.accelerate(50)   # +50 km/h

    print("Current speed after accelerations:", my_car.current_speed, "km/h")

    my_car.accelerate(-200)

    print("Final speed after emergency brake:", my_car.current_speed, "km/h")


main()

# QUESTION NO 3

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change

        if self.current_speed < 0:
            self.current_speed = 0

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def drive(self, hours):
        # Distance = speed * time
        self.travelled_distance += self.current_speed * hours


# Main program
def main():
    my_car = Car("ABC-123", 142)

    # Speed changes
    my_car.accelerate(30)
    my_car.accelerate(70)
    my_car.accelerate(50)

    print("Current speed:", my_car.current_speed, "km/h")

    my_car.accelerate(-200)
    print("Speed after emergency brake:", my_car.current_speed, "km/h")

    # Example drive
    my_car.current_speed = 60   # Set a constant speed for demonstration
    my_car.travelled_distance = 2000

    my_car.drive(1.5)  # Drive for 1.5 hours

    print("Travelled distance after driving:", my_car.travelled_distance, "km")


main()

# QUESTION NO 4

import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change

        if self.current_speed < 0:
            self.current_speed = 0

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


def main():
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        reg_number = f"ABC-{i}"
        cars.append(Car(reg_number, max_speed))

    race_over = False

    while not race_over:
        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)

            car.drive(1)

            if car.travelled_distance >= 10000:
                race_over = True

    print("\n=== FINAL RESULTS ===")
    print(f"{'Reg.Nr':<10} {'MaxSpeed':<10} {'CurSpeed':<10} {'Distance (km)':<15}")
    print("-" * 50)

    for car in cars:
        print(f"{car.registration_number:<10} "
              f"{car.maximum_speed:<10} "
              f"{car.current_speed:<10} "
              f"{car.travelled_distance:<15.2f}")


main()
