class Circle:
    pi=3.14

    def area(self,radius):
        return Circle.pi*radius**2

circle=Circle()
pizza_area=circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area=circle.area(11460/2)


class Store:
    pass
alternative_rocks=Store()
isabelles_ices=Store()


alternative_rocks.store_name="Alternative Rocks"
isabelles_ices.store_name="isabelle's Ices"


class Circle:
    pi=3.14

    #Se agrega un constructor 

    def __init__(self,diameter):
        print('New circle with diameter:{}'.format(diameter))

teaching_table=Circle(36)


class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter / 2
  def circumference(self):
    return 2*self.pi*self.radius
  
medium_pizza=Circle(12)
teaching_table=Circle(36)
round_room=Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())
