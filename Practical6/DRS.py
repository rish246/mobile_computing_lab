class Packet:
    def __init__(self, type, id, nodes, source, dest):
        self.type = type
        self.id = id
        self.nodes = nodes
        self.source = source
        self.dest = dest

    
    def get_path(self):
        path = [str(node) for node in self.nodes]

        return ' --> '.join(path)
        
        


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbours = []
        self.recieved_packets = []

    def add_neighbour(self, node):
        self.neighbours.append(node)
        node.neighbours.append(self)

    def is_packet_already_recieved(self, packet):
        return (packet.id in self.recieved_packets)

    def recieve_RREP(self, packet : Packet):
        print(f'Node {self.name} recieved RREP packet from {packet.source}')
        print(f'Path is : {packet.get_path()}')
        print(f'Sending Data to {packet.source}')

    def send_RREQ(self, packet):
        for node in self.neighbours:
            node.recieve_RREQ(packet)

    def recieve_RREQ(self, packet : Packet):
        print(f'Node {self} recieved RREQ packet')

        # check if the dest is not current node
        if packet.dest == self:
            print(f"Found Destination node... {self}")
            print(f'Node {self} is sending an RREP packet to {packet.source}')
            packet.nodes.append(self)
            packet.source.recieve_RREP(Packet(2, packet.id, packet.nodes, self, packet.source))
            return

        
        if self.is_packet_already_recieved(packet):
            return

        self.recieved_packets.append(packet.id)

        packet.nodes.append(self)

        self.send_RREQ(packet)
    


    def __str__(self) -> str:
        return f'{self.name}'




def main():
    S = Node("S")
    A = Node("A")
    C = Node("C")
    D = Node("D")
    F = Node("F")

    S.add_neighbour(A)
    A.add_neighbour(C)
    C.add_neighbour(D)
    S.add_neighbour(D)
    D.add_neighbour(F)

    print('----------------------------------')
    print('---------  DRS PROTOCOL  ---------')

    print('----------------------------------')
    print('Sending Data from S to F')

    unique_id = 1
    S.recieved_packets.append(1)
    s_RREQ = Packet(1, unique_id, [S], S, F)
    S.send_RREQ(s_RREQ)


if __name__ == "__main__":
    main()
