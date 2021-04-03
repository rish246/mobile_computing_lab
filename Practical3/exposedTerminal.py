from Terminal import *

def main():
    terminal_A = Terminal("A", 6, 0, 2)
    terminal_B = Terminal('B', 7, 0, 2)
    terminal_C = Terminal('C', 4, 0, 1)
    terminal_D = Terminal('D', 9, 0, 1)

    terminals = [terminal_A, terminal_B, terminal_C, terminal_D]

    n_collision = {}
    print('-----------------------------------Our Terminals-------------------------------------------------')

    for terminal in terminals:
        print(terminal)
        n_collision[terminal.name] = []

    print('-------------------------------------------------------------------------------------------------')

    #################### for the algo ############3
    n_terms = len(terminals)

    for i in range(n_terms):
        for j in range(n_terms):

            if i != j:
                if terminals[i].in_coverage_range(terminals[j]):
                    n_collision[terminals[i].name].append(terminals[j].name)

    for term in n_collision:

        terms_in_coverage_range = n_collision[term]
        if len(terms_in_coverage_range) >= 2:
            print(f'Terminals : {terms_in_coverage_range} are in coverage range of {term}')
            print(f'May result in exposed terminal problem\n')

if __name__ == "__main__":
    main()
