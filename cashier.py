'''
Steps of the project:
1- Accept the name of the product purchased by the consumer and the quantity of the purchased product.
2- The step one must be done repeatedly until all the products are entered.
3- After step one and step two are completed, the cashier must accept the consumer's supermarket membership. Depending on the type of membership a discount will be given.
4- There will be three types of memberships, Gold, Silver and Bronze with a discount of 20%, 10% and 5% respectively.
5- For the final step, it's going to be calculated the total bill amount depending upon the price of the products and print the detailed bill to the output screen.
'''

def welcome_function(): # Function 1
    supermarket_items = {
        'Biscuit': 3.50,
        'Coke': 2.50,
        'Chicken': 5.49,
        'Meat': 8.00,
        'Fish': 3.25,
        'Salad': 3.99,
        'Apple': 3.00,
        'Onion': 3.75
    }
    print('Welcome, this is the Supermarket Cashier Project!')
    return supermarket_items

def enter_products(supermarket_items): # Function 2
    buying_data = {}
    enter_details = True
    while enter_details:
        details = input('Press A to add product, C to check the the available products and Q to quit: ')
        if details.lower() == 'a':
            product = input('Enter product: ')
            quantity = int(input('Enter quantity: '))
            buying_data.update({product: quantity})
        elif details.lower() == 'c':
            print('Available items:')
            for item, price in supermarket_items.items():
                print(f'{item} - ${price:.2f}')
        elif details.lower() == 'q':
            enter_details = False
        else:
            print('Please select a correct option')
    return buying_data
    
def get_price(supermarket_items, product, quantity): # Function 3
    subtotal = supermarket_items[product] * quantity 
    rounded_subtotal = round(subtotal, 2)
    print(f'{product}:${str(supermarket_items[product])} x {str(quantity)} = {str(rounded_subtotal)}')
    return rounded_subtotal

def get_discount(bill_amount, membership): # Function 4
    discount = 0
    if bill_amount >= 25:
        if membership.lower() == 'gold':
            bill_amount = bill_amount * 0.80
            discount = 20
        elif membership.lower() == 'silver':
            bill_amount = bill_amount * 0.90
            discount = 10
        elif membership.lower() == 'bronze':
            bill_amount = bill_amount * 0.95
            discount = 5
        print(f'{str(discount)}% off for {membership} membership on total amount: ${str(bill_amount)}')
    else:
        print('No discount on amount less than $25')
    return bill_amount

def make_bill(supermarket_items, buying_data, membership): # Function 5
    bill_amount = 0
    for key, value in buying_data.items():
        bill_amount += get_price(supermarket_items, key, value)
    bill_amount = get_discount(bill_amount, membership)
    print(f'The total amount is ${str(bill_amount)}')

supermarket_items = welcome_function() # It makes a call to the Function 1
buying_data = enter_products(supermarket_items) # It makes a call to the Function 2
membership = input('Enter customer membership(Gold/Silver/Bronze): ')
make_bill(supermarket_items, buying_data, membership) # It makes a call to the Function 5

'''
Explanation of each function.
    Function 1: the main reason for this function is to welcome the user and the predefined dictionary.
    Function 2: it has the utility to make the Cashier to input all the products bought one by one and store them in a dictionary called "buying_data" and return it back.
    Function 3: the functionality of this function is to give the subtotal of a single product as per its price and quantity mentioned.
    Function 4: here, as per the total bill amount will be decided if the discount is applicable or not.
    Function 5: 
    loop starts:
        Call Function 3 until subtotal is added for all products within buying_data
    loop ends.
        Call Function 4 to calculate discounted amount.
'''