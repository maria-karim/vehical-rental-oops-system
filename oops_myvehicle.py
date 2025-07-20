# final python project 1
# maria's rental vehical system OOPS 
#  Parent class: Vehicle (ye sab vehicles ka base hai) Inheritance ka use ho raha hai
class Vehicle:
    def __init__(self, name, number, model, owner):
        self.name = name
        self.number = number
        self.model = model
        self.owner = owner

    def show_details(self):
        #  Polymorphism ke liye ye method sab child override karein ge
        return f"Name: {self.name}, Number: {self.number}, Model: {self.model}, Owner: {self.owner}"


#  Child class: Car ➤ Inheritance ho rahi hai Vehicle se
class Car(Vehicle):
    def show_details(self):
        #  Polymorphism ka example: same method name, different behavior
        return f"[CAR] {super().show_details()}"


#  Child class: Bike
class Bike(Vehicle):
    def show_details(self):
        return f"[BIKE] {super().show_details()}"


#  Child class: Truck
class Truck(Vehicle):
    def show_details(self):
        return f"[TRUCK] {super().show_details()}"


#  VehicleManager ➤ Encapsulation ka example (private list)
class VehicleManager:
    def __init__(self):
        self.__vehicles = []  # private list

    def add_vehicle(self, vehicle):
        self.__vehicles.append(vehicle)  # object ko list mein store

    def get_all_vehicles(self):
        return self.__vehicles
# ✅ File: oops_vehicle.py (Backend logic using OOP and JSON)

from abc import ABC, abstractmethod
import json
import os

# Abstract Class for Vehicle (Abstraction yahan use ho rahi hai)
class Vehicle(ABC):
    def __init__(self, vehicle_id, brand, model, price):
        self._vehicle_id = vehicle_id  # Encapsulation: private attributes
        self._brand = brand
        self._model = model
        self._price = price
        self._is_booked = False

    @abstractmethod
    def vehicle_type(self):
        pass

    def book(self):
        self._is_booked = True

    def cancel_booking(self):
        self._is_booked = False

    def to_dict(self):
        return {
            "vehicle_id": self._vehicle_id,
            "brand": self._brand,
            "model": self._model,
            "price": self._price,
            "is_booked": self._is_booked,
            "type": self.vehicle_type()
        }

    def is_booked(self):
        return self._is_booked


# Child Classes (Inheritance yahan ho rahi hai)
class Car(Vehicle):
    def vehicle_type(self):
        return "Car"

class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"

class Truck(Vehicle):
    def vehicle_type(self):
        return "Truck"

# Vehicle Manager (Polymorphism: multiple vehicle types handled)
class VehicleManager:
    def __init__(self):
        self.vehicles = []
        self.load_data()

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        self.save_data()

    def get_available_vehicles(self):
        return [v for v in self.vehicles if not v.is_booked()]

    def get_booked_vehicles(self):
        return [v for v in self.vehicles if v.is_booked()]

    def book_vehicle(self, vehicle_id):
        for v in self.vehicles:
            if v._vehicle_id == vehicle_id and not v.is_booked():
                v.book()
                self.save_data()
                return True
        return False

    def cancel_booking(self, vehicle_id):
        for v in self.vehicles:
            if v._vehicle_id == vehicle_id and v.is_booked():
                v.cancel_booking()
                self.save_data()
                return True
        return False

    def save_data(self):
        data = [v.to_dict() for v in self.vehicles]
        with open("vehicles.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if os.path.exists("vehicles.json"):
            with open("vehicles.json", "r") as f:
                data = json.load(f)
                for v in data:
                    v_type = v["type"]
                    if v_type == "Car":
                        vehicle = Car(v["vehicle_id"], v["brand"], v["model"], v["price"])
                    elif v_type == "Bike":
                        vehicle = Bike(v["vehicle_id"], v["brand"], v["model"], v["price"])
                    elif v_type == "Truck":
                        vehicle = Truck(v["vehicle_id"], v["brand"], v["model"], v["price"])
                    else:
                        continue
                    if v["is_booked"]:
                        vehicle.book()
                    self.vehicles.append(vehicle)
















# import json
# import os

# # ---------------------- Base Class ----------------------
# class Vehicle:
#     def __init__(self, vehicle_id, model, brand, rent):
#         self.vehicle_id = vehicle_id
#         self.model = model
#         self.brand = brand
#         self.rent = rent
#         self.available = True

#     def get_details(self):
#         return {
#             "ID": self.vehicle_id,
#             "Model": self.model,
#             "Brand": self.brand,
#             "Rent": self.rent,
#             "Available": self.available
#         }

# # ---------------------- Inherited Class - Car ----------------------
# class Car(Vehicle):
#     def __init__(self, vehicle_id, model, brand, rent):
#         super().__init__(vehicle_id, model, brand, rent)

# # ---------------------- Inherited Class - Truck ----------------------
# class Truck(Vehicle):
#     def __init__(self, vehicle_id, model, brand, rent, capacity):
#         super().__init__(vehicle_id, model, brand, rent)
#         self.capacity = capacity

#     def get_details(self):
#         data = super().get_details()
#         data["Capacity (tons)"] = self.capacity
#         return data

# # ---------------------- Inherited Class - Bike ----------------------
# class Bike(Vehicle):
#     def __init__(self, vehicle_id, model, brand, rent, cc):
#         super().__init__(vehicle_id, model, brand, rent)
#         self.cc = cc

#     def get_details(self):
#         data = super().get_details()
#         data["CC"] = self.cc
#         return data

# # ---------------------- Car Rental System (Manager) ----------------------
# class CarRentalSystem:
#     def __init__(self):
#         self.vehicles = []
#         self.file = "vehicle_data.json"
#         self.load_data()

#     # 🔄 Load from JSON
#     def load_data(self):
#         if os.path.exists(self.file):
#             with open(self.file, "r") as f:
#                 data = json.load(f)
#                 for item in data:
#                     type_ = item.get("type")
#                     if type_ == "Car":
#                         obj = Car(item["ID"], item["Model"], item["Brand"], item["Rent"])
#                     elif type_ == "Truck":
#                         obj = Truck(item["ID"], item["Model"], item["Brand"], item["Rent"], item["Capacity (tons)"])
#                     elif type_ == "Bike":
#                         obj = Bike(item["ID"], item["Model"], item["Brand"], item["Rent"], item["CC"])
#                     obj.available = item["Available"]
#                     self.vehicles.append(obj)

#     # 💾 Save to JSON
#     def save_data(self):
#         data = []
#         for v in self.vehicles:
#             d = v.get_details()
#             if isinstance(v, Car):
#                 d["type"] = "Car"
#             elif isinstance(v, Truck):
#                 d["type"] = "Truck"
#             elif isinstance(v, Bike):
#                 d["type"] = "Bike"
#             data.append(d)
#         with open(self.file, "w") as f:
#             json.dump(data, f, indent=4)

#     def add_vehicle(self, vehicle):
#         self.vehicles.append(vehicle)
#         self.save_data()

#     def show_all_vehicles(self):
#         return [v.get_details() for v in self.vehicles]

#     def rent_vehicle(self, vehicle_id):
#         for v in self.vehicles:
#             if v.vehicle_id == vehicle_id and v.available:
#                 v.available = False
#                 self.save_data()
#                 return True
#         return False

#     def return_vehicle(self, vehicle_id):
#         for v in self.vehicles:
#             if v.vehicle_id == vehicle_id and not v.available:
#                 v.available = True
#                 self.save_data()
#                 return True
#         return False


