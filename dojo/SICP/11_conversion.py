def make_money(money, currency):
    return (money, currency)

def amount(money_obj):
    (money, currency) = money_obj # money_obj[0]
    return money

def currency(money_obj):
    (money, currency) = money_obj
    return currency

def convert_to(money_obj, currency, exchange_rate):
    money = amount(money_obj) # Return the money amount with the constructor
    return make_money(money * exchange_rate, currency) # Create a new money obj

def add_money(money1_obj, money2_obj):
    (money1, currency1) = money1_obj
    (money2, currency2) = money2_obj
    if currency1 == currency2:
        return (money1+money2, currency1)
    else:
        return "Currencies should be equal"

money = make_money(100, "USD")
print(f"Make money $100 USD: {money}")
print(amount(money))
print(currency(money))

usd = make_money(1, "USD")
print(convert_to(usd, "EUR", 0.91))

m1 = make_money(100, "USD")
m2 = make_money(200, "USD")
m3 = make_money(200, "MX")

print(add_money(m1, m2))
print(add_money(m1, m3))
