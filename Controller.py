from View import View
import random, time
from multiprocessing import Process, Value


class Controller(Process):
    """
    The brain of the application, all the functionality is defined here
    """
    def __init__(self):
        super().__init__()

        self.view = View()
        self.view.show()

        #does something the the given button ist clicked
        self.view.new.clicked.connect(self.makePoint)
        self.view.remove.clicked.connect(self.removePoint)

    def makePoint(self):
        """
        Creates random coordinates, creates a new Point with them and adds the to the point list
        :return:
        """
        x = random.randint(self.view.radius, self.view.width - self.view.radius)
        y = random.randint(self.view.radius, self.view.height / 100 * 86 - self.view.b_height / 2)

        #new Point
        p = Point(x,y)
        #starts the point (it is a process)
        p.start()

        #adds the new point to the list
        self.view.points.append(p)

    def removePoint(self):
        """
        Removes the last point from the list
        :return:
        """
        if len(self.view.points) > 0:
            self.view.points[len(self.view.points)-1].join()
            #pop() deletes the last item from a list
            self.view.points.pop()


class Point(Process):
    """
    The class where Points are made
    """
    def __init__(self, x, y):
        """
        Constructor
        :param x: x-coordinate
        :param y: y-coordinate
        """
        super().__init__()

        #direction of x and y
        self.dirx = random.randint(0, 1)
        self.diry = random.randint(0, 1)

        #velocity of the points
        self.speed = random.randint(1, 10)

        #x and y as values
        self.x = Value("i", x)
        self.y = Value("i", y)

        #boolean that is True when windows is closed (helps alot)
        self.closing = Value("b", False)

    def run(self):
        """
        Method that is called when the associated thread/process is started with .start()
        :return:
        """
        while not self.closing.value:

            #when the direction of x ist 0 then x has a negative velocity, it is going to the left
            #otherwise x has a positive velocity, it is going to the right
            if self.dirx == 0:
                self.x.value += -1 * self.speed
            else:
                self.x.value += 1 * self.speed

            #when the direction of Y ist 0 then Y has a negative velocity, it is going up
            #otherwise y has a positive velocity, it is going down
            if self.diry == 0:
                self.y.value += -1 * self.speed
            else:
                self.y.value += 1 * self.speed

            #when the value of x is equal or greater than the maximal width of the window
            #its velocity is reverted
            if self.x.value >= View.width - (View.radius + 3):
                self.dirx = 0

            #when the value of x is equal or less than the radius of the point/circle (close to the min. width)
            #its velocity is reverted
            if self.x.value <= View.radius:
                self.dirx = 1

            #when the value of y is equal or less than the the radius of the point/circle (close to the min. height)
            #its velocity is reverted
            if self.y.value <= View.radius:
                self.diry = 1

            #when the value of y ist equal or greater than the location of the buttons minus its radius
            #its velocity is reverted
            if self.y.value >= View.height - (50 + View.radius):
                self.diry = 0

            time.sleep(0.01)

    def join(self, timeout=None):
        """
        Overriding the join method so the closing variable is set to True so the points are stopped properly
        :param timeout:
        :return:
        """
        self.closing.value = True
