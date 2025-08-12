products = ["Ao", "Quan", "Giay"]
prices = [250000,300000,500000]
x = zip(products,prices)
for i in range(len(products)):
    print(f"({products[i]}, {prices[i]})",sep ="/n")