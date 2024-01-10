# python 3: sal's shipping
# basic functions, control flow

weight = 100
ground_premium_shipping = 125

# ground shipping
def ground_shipping(weight):
    if weight <= 2:
        price = weight*1.5
    elif weight <= 6:
        price = weight*3
    elif weight <= 10:
        price = weight*4
    else:
        price = weight*4.75
    price += 20
    return f'Ground shipping will cost ${price}'

def drone_shipping(weight):
    if weight <= 2:
        price = weight*4.5
    elif weight <= 6:
        price = weight*9
    elif weight <= 10:
        price = weight*12
    else:
        price = weight*14.25
    return f'Drone shipping will cost ${price}'


# testing
print(ground_shipping(8.4))
print(drone_shipping(1.5))

print(ground_shipping(4.8))
print(drone_shipping(4.8))

print(ground_shipping(41.5))
print(drone_shipping(41.5))