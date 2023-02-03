# create an main function
def main():
    
    try:    
        network = []
        result = []
        test = {}
        infile = open("Network.txt", "r")
        line = infile.readline()
        while line:
            network.append(line.rstrip("\n").split(",") )
            line = infile.readline()
        infile.close()
        
    except FileNotFoundError :
        network = []    
    
    choice = 0
    while choice !=4:
        
        choice = int(input())
        
        if choice == 1:
            # Note : add only computer and repeaters
            print("Addig a Device....")
            device_1 = input("Enter the name of the Device-1 >>>")
            # check condition for computers and repeaters
            if device_1[0] == 'A':
                network.append([device_1])
            else:
                print("Add only computers and repeaters")
        
        elif choice == 2:
            print("Setting up device strength ..")
            device = input("Enter device : ")
            strength = int(input("Enter Strength"))
            if device in network:
                if strength == 0:
                    strength = 5
                test.add(device, strength)
            else:
                print("Strenght not added some issues")

        elif choice == 3:
            print("Displaying all Devices(Computers and Repeaters)...")
            for i in range(len(network)):
                print(network[i])

        elif choice == 4:
            data = set()
            devices = input("Enter the devive : ")        
            data.add(devices)
            result.append(data)
            print(result)
            
        
        elif choice == 5:
            print("Quitting Program")
    print("Program Terminated!")
    
    # Saving to external TXT file
    outfile = open("Network.txt", "w")
    for net in network:
        outfile.write(",".join(net) + "\n")
    outfile.close()
                    


if __name__ == "__main__":
    main()