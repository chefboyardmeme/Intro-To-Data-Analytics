
import random
from datetime import date
from Lab_2_Morrison import CreditCard

products = ['Aztex Coin Medallion Necklace', 'Pirate Life Graphic T-shirt', 'Treasure Map Tapestry', 'Pirates of Carribean Wall Poster', 'Davy Jones Music Box' ]

customers = ['Jack Sparrow', 'Frederick Barbossa', 'Will Turner', 'Elizabeth Swann', 'Joshamee Gibbs']

for x, prod in enumerate(products):
    print('\n ----------------------')
    print("Welcome to the Data Analytics Store!!!")
    print("Order Placed: " + date.today().strftime('%B %d, %Y'))
    print("Tortuga Pirate Shop Order Number: " + str(random.randint(500, 5000)))
    price = random.randrange(1, 100)
    print("Order Total: ${:.2f}".format(price))

    cardnum = str(random.randint(1000, 9999)) + " " + str(x) + str(random.randint(100, 999)) + " " + str(random.randint(1000, 9999)) + " " + str(random.randint(1000, 9999))
    ccard = CreditCard(cardnum, customers[x], '10/25')

    if ccard.processOrder(price):
        print('Order successfully processed.')
        print('Thank you, {} for ordering the {}. Your {} credit card will be charged for ${:.2f}.'.format(ccard.get_cardOwner(), prod, ccard.get_cardType(), price))
    elif ccard.get_cardType() == 'Not Supported Card Type':
        print('Your credit card is not accepted by the store. Please provide a different type of credit card.')
    else:
        print('Your credit card did not have sufficient amount. Order was not successfully processed.')
    
    print('\n --- Credit Card Information ----\n')
    print(ccard)

