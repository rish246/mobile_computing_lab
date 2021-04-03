from Terminal import *

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
            if terminal.in_coverage_range(terminals[i]) and (terminal.name != terminals[i].name):
                print(f'Terminal {terminals[i].name} is in coverage range of {terminal.name}')
                n_collisions[terminals[i].name].append(terminal.name)


    for term in n_collisions:
        collision_terms = n_collisions[term]
        
        if len(collision_terms) >= 2:
            print(f'{term} can cause hidden terminal problem with terminals : {collision_terms}')

    


if __name__ == "__main__":
    main()
