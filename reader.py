import robin_stocks as r

login = r.login("apetrolino1990@gmail.com", "Poopdick1!")

my_stocks = r.build_holdings()

for key,value in my_stocks.items():
    print(key,value)