class Vehicle():
	seats = 0
    def __init__(self, make,model,year):
        self.make = make
        self.model= model
        self.year=year
    def description()
    	pass
    def number_of_seats():
    	return seats
    def number_of_wheels():
    	return number_of_wheels
    def cost():
    	pass


  #implementing inheritance,car is inheriting from vehicle

   class Car(Vehicle):
   		number_of_wheels =4
   		seats =4
   		def description(self):
   			return "A "  + str(self.year) + " Car model: "+ self.model + " make:" + self.make 
   		def cost():
   			price = self.number_of_wheels*self.number_of_wheels * self.year * 1000
   			return price