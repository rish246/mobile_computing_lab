import  math

class Terminal:
    def __init__(self, name, center_x, center_y, radius):
        self.name = name
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def are_areas_intercepting(self, other_terminal):
        dist_between_centers = math.sqrt((self.center_x - other_terminal.center_x) ** 2 + (self.center_y - other_terminal.center_y)**2)

        return dist_between_centers <= self.radius


    def __str__(self):
        return f'Terminal {self.name} : [Center : ({self.center_x}, {self.center_y})\tRadius : {self.radius}]'


def main():
    terminal_A = Terminal("A", 1, 0, 3)
    terminal_B = Terminal("B", 3, 0, 3)
    terminal_C = Terminal("C", 5, 0, 3)

    terminals = [terminal_A, terminal_B, terminal_C]


    n_collisions = {}

    print('-----------------------------------Our Terminals-------------------------------------------------')
    for terminal in terminals:
        print(terminal)
        n_collisions[terminal.name] = []

    print('-------------------------------------------------------------------------------------------------')


    for terminal in terminals:
        for i in range(len(terminals)):
            if terminal.are_areas_intercepting(terminals[i]) and (terminal.name != terminals[i].name):
                print(f'Terminal {terminals[i].name} colliding with {terminal.name}')
                n_collisions[terminals[i].name].append(terminal.name)


    for term in n_collisions:
        collision_terms = n_collisions[term]
        
        if len(collision_terms) >= 2:
            print(f'{term} can cause hidden terminal problem with terminals : {collision_terms}')

    


if __name__ == "__main__":
    main()
