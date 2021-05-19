class Swift:
    def start(self):
        print("swift car starts. ")
    def accelarate(self):
        print("swif car is accelarating. ")
    def breaking(self):
        print("swift car is breaking. ")
    def stop(self):
        print("swift car is stopping. ")
class S_cross:
    def start(self):
        print("s_cross car starts. ")
    def accelarate(self):
        print("s_cross car is accelarating. ")
    def breaking(self):
        print("s_cross is breaking. ")
    def stop(self):
        print("s_cross is stopping. ")
class Person:
    def drive(self,car):
        car.start()
        car.accelarate()
        car.breaking()
        car.stop()
per=Person()

#sw=Swift()
#per.drive(sw)

sc=S_cross()
per.drive(sc)
