arr = []
for i in range(3):
    ele = float(input("Enter a price : "))
    arr.append(ele)
    print(arr)
pr = []
for price in arr:
    price_r = int(price)
    price_k = int((price - price_r) * 100)
    #не понимаю почему, некоторые сотые меньше на 1 вывдит
    #print(price_k)
    pr.append(f'{price_r}руб {price_k}коп')
pr = " ,".join(pr)

print(pr)
