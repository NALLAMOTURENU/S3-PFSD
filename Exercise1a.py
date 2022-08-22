class Ticket:
    firstclass=20
    secondclass=30
    thirdclass=40
    def input(self, name, id, nooftickets):
        self.name = input("Enter your name")
        self.id = id
        self.nooftickets = nooftickets

        clas= input("which class of tickets would u you like to book")
        n=int(input("How many tickets you want to book"))
        if clas == "FirstClass":
            while(Ticket.firstclass>0):
                 Ticket.firstclass-n










