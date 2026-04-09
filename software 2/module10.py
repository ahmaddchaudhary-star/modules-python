import random


class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moved up to floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moved down to floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print(f"Floor {target_floor} is out of range.")
            return

        while self.current_floor < target_floor:
            self.floor_up()

        while self.current_floor > target_floor:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []

        for _ in range(number_of_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"\nRunning elevator {elevator_number} to floor {destination_floor}")
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print("Invalid elevator number.")

    def fire_alarm(self):
        print("\nFIRE ALARM! All elevators are going to the bottom floor.")
        for i, elevator in enumerate(self.elevators):
            print(f"Returning elevator {i} to bottom floor:")
            elevator.go_to_floor(self.bottom_floor)


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_travelled = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed

        if self.current_speed < 0:
            self.current_speed = 0
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        self.distance_travelled += self.current_speed * hours


class Race:
    def __init__(self, name, distance_km, car_list):
        self.name = name
        self.distance_km = distance_km
        self.cars = car_list

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print(f"{'Car':<12}{'Max Speed':<12}{'Current Speed':<15}{'Distance Travelled'}")
        print("-" * 55)
        for car in self.cars:
            print(f"{car.registration_number:<12}{car.max_speed:<12}{car.current_speed:<15}{car.distance_travelled:.1f}")

    def race_finished(self):
        for car in self.cars:
            if car.distance_travelled >= self.distance_km:
                return True
        return False


# Main program
if __name__ == "__main__":
    print("=== Elevator Test ===")
    h = Elevator(1, 10)
    h.go_to_floor(5)
    h.go_to_floor(1)

    print("\n=== Building Test ===")
    building = Building(1, 10, 3)
    building.run_elevator(0, 7)
    building.run_elevator(1, 5)
    building.run_elevator(2, 9)

    building.fire_alarm()

    print("\n=== Race Simulation ===")
    cars = []
    for i in range(1, 11):
        reg_number = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        cars.append(Car(reg_number, max_speed))

    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0
    while not race.race_finished():
        hours += 1
        race.hour_passes()

        if hours % 10 == 0:
            print(f"\n--- Status after {hours} hours ---")
            race.print_status()

    print(f"\n--- Final status after {hours} hours ---")
    race.print_status()