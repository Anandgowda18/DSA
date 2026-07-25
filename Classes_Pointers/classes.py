class Cookie:
    def __init__(self,color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self,color):
        self.color = color

cookie_one = Cookie('blue') #Only init method is called, self is cookie_one itself. So self.color(cookie_one.color) is set as blue
cookie_two = Cookie('green') #Only init method is called, self is cookie_two itself. So self.color(cookie_two.color) is set as green

print("cookie_one color is",cookie_one.get_color()) #output is cookie_one color is blue
print("cookie_two color is",cookie_two.get_color()) #output is cookie_two color is green

cookie_one.set_color('yellow') #We call set_color method which have self.color = color, so we set cookie_one.setcolor = green

print("cookie_one color is",cookie_one.get_color()) #output is cookie_one color is yellow
print("cookie_two color is",cookie_two.get_color()) #output is cookie_one color is green
