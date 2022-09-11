#Programmer name: Susan Li
#Program creation date: August 17, 2022

#Hotel costs

#define the variables
#ask the customer how many nights they will be staying at the hotel
nights = int(input("How many nights are you staying at the hotel? "))
#ask the customer how many guests are going to be staying at the hotel
guests = int(input("How many guests there going to be? "))
#single occupancy room calculation
if guests == 1:
    print("${}".format(nights * 100.00))
#double occupancy room calculation
elif guests == 2:
    print("${}".format(nights * 150.00))
#deluxe suite/penthouse suite
elif guests > 2:
    #ask if customer wants a deluxe suite or a penthouse suite
    room = input("Do you want a deluxe suite or a penthouse suite? ")
    #deluxe suite calculation
    if room == "deluxe suite" or room == "Deluxe suite" or room == "Deluxe Suite":
        print("${}".format(nights * 275.00))
    #penthouse suite calculation
    elif room == "penthouse suite" or room == "Penthouse suite" or room == "Penthouse Suite":
        print("${}".format(nights * 500.00))
