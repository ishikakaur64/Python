class Vehicle:
    def __init__(self, fare_per_km):
        self.fare_per_km = fare_per_km


class Bus(Vehicle):
    def calculate_fare(self, distance):
        return self.fare_per_km * distance


bus = Bus(5)
print(bus.calculate_fare(10))