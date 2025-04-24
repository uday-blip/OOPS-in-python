#write program to create different classes with objects by using the concept of OOPS
#program 1
class Bike:
    bike_name='z900'
    bike_topspeed='299kmph'
    def name(this):
        return f'this is a bike named {this.bike_name}'
    def topspeed(this):
        return f'this bikes topspeed is {this.bike_topspeed}'
bike=Bike()
print(bike.name())
print(bike.topspeed())

# program 2
class Train:
    it_travels='rjy to vizag'
    it_starts_at='mrng 7:30'
    its_name='godavari express'
    def about(self):
        return f'this train name is {self.its_name}'
    def travel_details(self):
        return f'this train starts at {self.it_starts_at} '
    def timings(self):
        return f'it travels from {self.it_travels}'
railway=Train()
print(railway.about())
print(railway.travel_details())
print(railway.timings())

#program 3
class School:
    strength_of_school='850people'
    school_name='bhashyam'
    place='rajamundry'
    def name(this):
        return f'the school name is {this.school_name}'
    def description(self):
        return f'the total of school is{self.strength_of_school}, the place is {self.place}'
badi=School()
print(badi.name())
print(badi.description())