products = []
while True:
    product_class = input('請輸入商品類別：')
    if product_class == 'q':
        break
    name = input('請輸入商品名稱：')
    price = input('請輸入商品價格：')
    products.append([product_class, name, price])
print(products)
print(products[0][0])
print(products[0][1])
print(products[1][0])
print(products[1][1])
print(products[2][0])
print(products[2][1])
