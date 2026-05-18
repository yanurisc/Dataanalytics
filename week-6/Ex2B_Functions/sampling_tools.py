import random
# Import the random module to use random selection functions


products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']
# A list of products a data analyst might work with


product_of_the_day = random.choice(products)
print(f"Product of the Day: {product_of_the_day}")
# Part A - Pick one random product as the Product of the Day
# random.choice() selects one item randomly each time it runs


survey_products = random.sample(products, 3)
print(f"Usability Survey Products: {survey_products}")
# Part b - Select 3 products for a usability survey
# random.sample() selects items without repeating the same product twice

random.shuffle(products)
print(f"Shuffled Products: {products}")
# Part c - Shuffle the products list into a random order for presentation
# random.shuffle() changes the list directly so we print products after shuffling

