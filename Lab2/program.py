import math


def sales_prediction():
    sales = float(input())
    money = sales * 1.19
    print(money)
    pass


def yard_to_meter():
    yards = float(input())
    meters = yards * 0.914
    milimeters = meters * 1000
    kilometers = meters / 1000
    print(milimeters)
    print(meters)
    print(kilometers)
    pass


def cashier():
    one = float(input())
    two = float(input())
    three = float(input())
    four = float(input())
    five = float(input())
    sum = one + two + three + four + five
    print(sum)
    print(sum * 0.14)
    print(sum * 0.86)
    pass


def odometer():
    speed_0 = float(input())
    boost = float(input())
    time_boosted = float(input())
    time_not_boosted = float(input())
    
    speed = speed_0 + boost * time_boosted
    road_boosted = abs(speed * time_not_boosted + ((boost * (time_boosted ** 2)) / 2))
    road_not_boosted = speed * time_not_boosted
    
    print(road_boosted)
    print(road_not_boosted)
    
    pass


def payment_instalments():
    sum = float(input())
    times = float(input())
    sum *= 1.05
    
    print(sum)
    print(sum / times)
    pass


def miles_per_galon():
    miles = float(input())
    gas = float(input())
    
    mpg = miles / gas
    print(mpg)
    pass


def cookie():
    amount_c = float(input())
    x = amount_c / 48
    
    print(1.5 * x)
    print(1 * x)
    print(2.75 * x)
    pass


def vineyard():
    length = float(input())
    length_foot = float(input())
    spaaced = float(input())
    
    amount = (length - 2 * length_foot) / spaaced
    
    print(math.floor(amount))
    
    pass


def compound_interest():
    sum = float(input())
    year_percent = float(input())
    per_year = float(input())
    years = float(input())
    
    rich_money = sum * ((1 + (year_percent / 100) / per_year)) ** (per_year * years)
    
    print(rich_money)
    pass


if __name__ == "__main__":
     eval(input() + "()")
     
     
