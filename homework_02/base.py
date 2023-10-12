from abc import ABC
import exceptions


class Vehicle(ABC):
    weight=0
    started=False
    fuel=0
    fuel_consumption=0
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        
    def start(self):
        if self.fuel > 0:
            self.started = True
            print('Engine is started')
        else:
            self.started = False
            raise exceptions.LowFuelError('Fuel level is not enough')
        
    def move(self, distance):
        self.distance = distance
        fuel_needed = self.distance/self.fuel_consumption
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
            return fuel_needed
        else:
            raise exceptions.NotEnoughFuel('Not enough fuel for transmitted distance')
        
            

        
        
        
            
    
                    
                
                    
