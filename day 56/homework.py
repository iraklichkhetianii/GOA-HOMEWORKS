#1
def max_multiple(divisor, bound):
    return bound - (bound % divisor)


#2
def get_issuer(number):
    number = str(number)
    
    if (len(number) == 13 and number[0] == "4") or (number[0] == "4" and len(number) == 16): return "VISA"
    if len(number) == 15 and number[0:2] in ['34', '37']: return "AMEX"
    if number[0:2] in ['51', '52', '53', '54', '55']: return "Mastercard"
    if number[0:4] == "6011": return "Discover"

    return 'Unknown'

#3
def switcheroo(string):
    return ''.join({'a':'b', 'b':'a'}.get(c, c) for c in string)

#4
def number(bus_stops):
    return sum(x - y for x,y in bus_stops)

#5