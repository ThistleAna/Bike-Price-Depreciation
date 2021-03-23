#As an extension to the motorbike task that costs £2000 and
#loses 10% of its value every year. Using a loop, print the
#value of the bike every following year until it falls below
#£1000 by using a function and passing in parameters


def bike_value(bike_price, year):
    while bike_price > 1000:
        print("The bike in " + str(year) + " is = £" + str(bike_price))
        bike_price *= 0.9
        year -= 1


bike_value(2000, 2020)
