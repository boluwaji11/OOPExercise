# Import the CarClass class

import CarClass as cc

# Define the main function
def main():
    # Initialize the year and make of the car
    year = "1994"
    make = "Audi"

    # Create an object of the Car class
    car = cc.Car(year, make)

    print("Car Speedometer")
    print("-------------")

    # Accelerate the car 5 times
    for speed in range(5):
        # Call the accelerate() method
        car.accelerate()

        # Display the current speed as car accelerates
        print("Car Speed at:", car.get_speed(), "miles/hr")

    # Display the total speed reached
    print("-----------------------------")
    print("The total speed reached is:", car.get_speed(), "miles/hr")
    print("-----------------------------")

    print("Car decelerating.......... ")
    print()

    # Decelerate the car 5 times
    for speed in range(5):
        # Call the brake() method
        car.brake()

        # Display the current speed as car decelerates
        print("Car decelerated to:", car.get_speed(), "miles/hr")


# Call the main function
main()