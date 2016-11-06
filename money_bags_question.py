# Ben Woodfield
# Money Bags Program

'''
Write an application that will:

Allow the user to Input the type of coin
Allow the user to Input the weight of a bag of coins

Calculate the difference between the users bag weight-
and the correct bag weight
'''

# Possible user entries
1p = one_pence
2p = two_pence
5p = five_pence
10p = ten_pence
20p = twenty_pence
50p = fifty_pence
£1 = one_pound
£2 = two_pound

# Individual coin weights (in Grams)
one_pence = 3.56
two_pence = 7.12
five_pence = 3.25
ten_pence = 6.50
twenty_pence = 5.00
fifty_pence = 8.00
one_pound = 9.50
two_pound = 12.00

# Correct bag weights in (Grams)
one_pence_bag = 356
two_pence_bag = 356
five_pence_bag = 325
ten_pence_bag = 325
twenty_pence_bag = 250
fifty_pence_bag = 160
one_pound_bag = 190
two_pound_bag = 120

# Individual calculation functions for each possible coin and bag types
def calculate_one_pence():
    if answer_bag > one_pence_bag:
        print("You need to remove:", answer_bag - one_pence_bag. "pence - or:", )
        else:
            print("You need to add: ", one_pence_bag - answer_bag)

def calculate_two_pence():
    if answer_bag > two_pence_bag:
        print("You need to remove:", answer_bag - two_pence_bag)
        else:
            print("You need to add: ", two_pence_bag - answer_bag)
    
def calculate_five_pence():
    if answer_bag > five_pence_bag:
        print("You need to remove:", answer_bag - five_pence_bag)
        else:
            print("You need to add: ", five_pence_bag - answer_bag)

def calculate_ten_pence():
    if answer_bag > ten_pence_bag:
        print("You need to remove:", answer_bag - ten_pence_bag)
        else:
            print("You need to add: ", ten_pence_bag - answer_bag)

def calculate_twenty_pence():
    if answer_bag > twenty_pence_bag:
        print("You need to remove:", answer_bag - twenty_pence_bag)
        else:
            print("You need to add: ", twenty_pence_bag - answer_bag)

def calculate_fifty_pence():
    if answer_bag > fifty_pence_bag:
        print("You need to remove:", answer_bag - fifty_pence_bag)
        else:
            print("You need to add: ", fifty_pence_bag - answer_bag)

def calculate_one_pound():
    if answer_bag > one_pound_bag:
        print("You need to remove:", answer_bag - one_pound_bag)
        else:
            print("You need to add: ", one_pound_bag - answer_bag)

def calculate_two_pound():
    if answer_bag > two_pound_bag:
        print("You need to remove:", answer_bag - two_pound_bag)
        else:
            print("You need to add: ", two_pound_bag - answer_bag)

# Collect the data from the user
answer_coin = int(input("Enter the value of the coin: (eg: 1p, 2p, 5p, 10p, 20p, 50p, £1 £2)"))
answer_bag = int(input("Enter the current weight of the bag: "))

# Display the correct results (how much to add or remove from the bag of coins)
if answer_coin = 1p:
    print("The correct weight of a £1 bag-full of 1-Pence coins is: ", one_pence_bag, "pence")

calculate_one_pence()
