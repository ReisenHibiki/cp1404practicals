from prac_09.silver_service_taxi import SilverServiceTaxi

test_car = SilverServiceTaxi("Silver", 100, 2)

print(test_car)
test_car.drive(18)
print(f"{test_car.get_fare():.2f}")
print(test_car)
