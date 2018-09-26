toplimit = 15
middlelimit = 15
bottomlimit = 15
TOP = []
MIDDLE = []
BOTTOM = []
status = True
while True:
    print("Do you want to take out/put an item? Y/N")
    answer = input()
    if answer == "Y":
        print("Choose an action: PUT/TAKE")
        action = input()
        if action == "PUT":
            print("Pick Space TOP/MIDDLE/BOTTOM:")
            space = input()
            if space == "TOP":
                print("What Do You Want to Put In?")
                item = input()
                print("Volume of Item")
                volume = int(input())
                if volume >= toplimit:
                    print("Volume of Item Exceeds Volume of Fridge")
                else:
                    print(item + " is in fridge")
                    print("Available Space in the Top is " + str((toplimit - volume)))
                    TOP.append({item: volume})
            if space == "MIDDLE":
                print("What Do You Want to Put In?")
                item = input()
                print("Volume of Item")
                volume = int(input())
                if volume >= middlelimit:
                    print("Volume of Item Exceeds Volume of Fridge")
                else:
                    print(item + " is in fridge")
                    print("Available Space in the Middle is " + str((middlelimit - volume)))
                    MIDDLE.append({item: volume})
            if space == "BOTTOM":
                print("What Do You Want to Put In?")
                item = input()
                print("Volume of Item")
                volume = int(input())
                if volume >= bottomlimit:
                    print("Volume of Item Exceeds Volume of Fridge")
                else:
                    print(item + " is in fridge")
                    print("Available Space in the Bottom is " + str((bottomlimit - volume)))
                    TOP.append({item: volume})
        if action == "TAKE":
            print("Pick Space TOP/MIDDLE/BOTTOM:")
            space = input()
            if space == "TOP":
                print("What Do You Want to Take Out?")
                item = input()
                if volume <= toplimit:
                    print(item + " is out of the fridge")
                    print("Available Space in the Top is " + str((toplimit - volume)))
                    TOP.remove({item: volume})
                else:
                    print("Error")

            if space == "MIDDLE":
                print("What Do You Want to Take Out?")
                item = input()
                if volume <= middlelimit:
                    print(item + " is out of the fridge")
                    print("Available Space in the Middle is " + str((middlelimit - volume)))
                    MIDDLE.remove({item: volume})
                else:
                    print("Error")

            if space == "BOTTOM":
                print("What Do You Want to Take Out?")
                item = input()
                if volume <= bottomlimit:
                    print(item + " is out of the fridge")
                    print("Available Space in the Bottom is " + str((bottomlimit - volume)))
                    BOTTOM.remove({item: volume})
                else:
                    print("Error")
    else:
        print("Thank You For Using the Refrigerator")
        break
