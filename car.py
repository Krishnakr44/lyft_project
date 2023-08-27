from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass
    
class Battery(CarPart):
    def needs_service(self):
        # Implement logic to determine if battery needs service
        pass

class Engine(CarPart):
    def needs_service(self):
        # Implement logic to determine if engine needs service
        pass
class CarModel:
    def __init__(self):
        self.car_parts = []

    def add_part(self, part):
        self.car_parts.append(part)

    def needs_service(self, criteria):
        # Implement logic to check if the car needs service based on criteria
        pass
class ServiceCriteria(ABC):
    @abstractmethod
    def check(self, car):
        pass
class MileageCriteria(ServiceCriteria):
    def check(self, car):
        # Implement logic to check if mileage criteria is met
        pass

class DateCriteria(ServiceCriteria):
    def check(self, car):
        # Implement logic to check if date criteria is met
        pass
class CarService:
    def evaluate_service(self, car_model, criteria_list):
        # Implement logic to evaluate service based on provided criteria
        pass
