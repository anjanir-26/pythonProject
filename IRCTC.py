class IRCTC:
    def book(self):
            while True:
                ch = input("enter source")
                ds = input("enter destination")
                if(source=="hyderabad" && destination=="bza"):
                    print("The available trains are \n SC Intercity\n SNSI Express \n Krishna express")
                    choi=input("enter your choice")
                    if choi==1:
                        n = int(input("enter no of tickets"))
                        print("1.sleeper\n 2.sitter")
                        p = int(input("enter your choice"))
                        if p==1:
                            cost=190*n
                            print(cost)
                        else:
                            cost=120*n
                            print(cost)

                    elif choi==2:
                        n = int(input("enter no of tickets"))
                        print("1.AC \n 2.chair seating")
                        p = int(input("enter your choice"))
                        if p == 1:
                            cost = 330 * n
                            print(cost)
                        else:
                            cost = 90 * n
                            print(cost)
                    n = int(input("enter no of tickets"))
                    print("1.general\n 2.sleeper")
                    p = int(input("enter your choice"))
                    if p == 1:
                        cost = 110 * n
                        print(cost)
                    else:
                        cost = 187 * n
                        print(cost)



                elif(source=="delhi" && destination=="hyd"):
                    print("The available trains are \n Rajadhani Express\n Telangana Express")
                else:
                    print("go and pick a flight")


                if p == 1:

                    cost=130*n
                    print("cost is rupees",cost)

                else:
                    cost=90*n
                    print(cost)


o=IRCTC()
o.book()




