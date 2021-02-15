class Car:

    # Initialize the required arguments
    def __init__(self, modelYear, carMake):
        self.__modelYear = modelYear
        self.__carMake = carMake
        self.__carSpeed = 0
    
    # Run the car acceleration
    def accelerate(self):
        self.__carSpeed += 5

    # Decelerates the car
    def brake(self):
        self.__carSpeed -= 5

    # Displays the current car speed
    def get_speed(self):
        return self.__carSpeed
