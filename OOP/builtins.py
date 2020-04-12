class kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = kettle("Kenwood", 8.99)
print(kenwood.price)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

print("*" * 80)

kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power)

print("Switch to atomic power")
kettle.power_source = "atomic"

print(kettle.power_source)

print("Switch kenwood to gas")
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)
print(kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)