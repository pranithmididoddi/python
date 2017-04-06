class cars(object):

    def __init__(self,make,cost):
        self.make=make
        self.cost=cost

sonata=cars("hyundai",8000)
scion=cars("toyota",24000)

print sonata.make," price is: ",sonata.cost," make is: ",sonata.make

