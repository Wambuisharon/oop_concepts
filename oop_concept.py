class Vehicle():
    seats = 0
     #implementing encapsulation
    __location = ""
    def __init__(self, make,model,year):
        self.make = make
        self.model= model
        self.year=year
    def description():
        pass
    def number_of_seats():
        return seats
    def number_of_wheels():
        return number_of_wheels
    def cost():
        pass
    def location_tracker(self,location):    
        pass

  #implementing inheritance,car is inheriting from vehicle

class Car(Vehicle):
        number_of_wheels =4
        seats =4
  #implementing polymorphism 
        def description(self):
            return "A "  + str(self.year) + " Car model: "+ self.model + " make:" + self.make + " Price: " + str(self.cost()) 
        def cost(self):
            price = self.number_of_wheels*self.number_of_wheels * int(self.year) * 1000
            return price

class Truck(Vehicle):
        number_of_wheels =8
        seats =3
        def description(self):
            return "A "  + str(self.year) + " Truck model: "+ self.model + " make:" + self.make + " Price: " + str(self.cost())
        def cost(self):
            price = int(self.year)/.986 * 100000 
            return price

if __name__ == '__main__':
    vehicle = Car("Mark X", "Toyota", "2013")
    print vehicle.description()

    vehicle = Truck("u200", "Mercedees", "2015")
    print vehicle.description()

