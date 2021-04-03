import  math


class Terminal:
    def __init__(self, name, center_x, center_y, radius):
        self.name = name
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def in_coverage_range(self, other_terminal):
        dist_between_centers = math.sqrt((self.center_x - other_terminal.center_x) ** 2 + (self.center_y - other_terminal.center_y)**2)

        return dist_between_centers <= self.radius


    def __str__(self):
        return f'Terminal {self.name} : [Center : ({self.center_x}, {self.center_y})\tRadius : {self.radius}]'