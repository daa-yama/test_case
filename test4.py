def check_price_category(price):
    if price >= 1000:
        print("高価な商品です")
    elif price >= 500:
        print("普通の商品です")
    else:
        print("お買い得です")
        
check_price_category(200)