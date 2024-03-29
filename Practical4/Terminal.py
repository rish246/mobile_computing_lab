import  math


class Terminal:
    def __init__(self, name, center_x, center_y, radius):
        self.name = name
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.nodes_in_coverage_range = []

    def in_coverage_range(self, other_terminal):
        dist_between_centers = math.sqrt((self.center_x - other_terminal.center_x) ** 2 + (self.center_y - other_terminal.center_y)**2)

        return dist_between_centers <= self.radius

    def send_rts(self, intedended_terminal):
        successfully_sent_rts = False
        print(f'Terminal {self.name} sending rts to Terminal {intedended_terminal}')

        for node in self.nodes_in_coverage_range:

            node.recieve_rts(self.name, intedended_terminal)
            if node.name == intedended_terminal:
                successfully_sent_rts = True

            
        if not successfully_sent_rts:
            print(f'Inteded node not in coverage range of Terminal {self.name}')


        
    def recieve_rts(self, sender_name, intedended_terminal):
        print(f'Terminal {self.name} received rts from {sender_name}')

        if(self.name == intedended_terminal):
            self.send_cts(self.name, sender_name)


    def send_cts(self, source_terminal, dest_terminal):
        successfully_send_cts = False

        for node in self.nodes_in_coverage_range:
            node.recieve_cts(source_terminal, dest_terminal)
            if dest_terminal == node.name:
                successfully_send_cts = True

        
        if not successfully_send_cts:
            print(f'Terminal {dest_terminal} is not in coverage range of terminal {source_terminal}... couldnt send cts')


    def recieve_cts(self, source_terminal, dest_terminal):
        print(f'Terminal {self.name} received cts from {source_terminal}')

        if(dest_terminal == self.name):
            print('-----------------------------------------------------------------------------------------------------------------------')
            print(f'Terminal {dest_terminal} successfully recieved CTS from terminal {source_terminal}... sending data to {source_terminal}')
            print('-----------------------------------------------------------------------------------------------------------------------')

    def __str__(self):
        return f'Terminal {self.name} : [Center : ({self.center_x}, {self.center_y})\tRadius : {self.radius}]'
