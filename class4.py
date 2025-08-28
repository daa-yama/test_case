# 【問題文】
# Product クラスを作ってください。
# ・コンストラクタ（__init__）で name（商品名）と stock（在庫数）を受け取り、インスタンス変数に保存する
# ・add_stock(amount) メソッドで在庫を amount 増やす
# ・show_stock() メソッドで 「〇〇の在庫は△△個です」と表示する
# インスタンスを作成し、在庫を追加して表示してください。
class Product:
    def __init__(self, name, stock):
        # コンストラクタ　インスタンス初期化メソッド
        
        self.name = name
        self.stock = stock
    
    def add_stock(self, amount):
        self.stock += amount #複合代入演算子 	+= は「いまの値に加える」 self.stock = self.stock + amountと同じ
        # •	+= は 「足してから、同じ変数に戻す」•	=+ は 「プラスをつけた値をそのまま入れ替える」  
    
    def show_stock(self):
        print(f"{self.name}の在庫は{self.stock}個です")

my_product = Product("りんご", 8)
my_product.add_stock(3)
my_product.show_stock()
#returnで返すものがないのでこの入力でOK



# ## 📝 練習問題1：`Book` クラス
# ### 問題文
# `Book` クラスを作ってください。
# -   コンストラクタ（`__init__`）で `title`（本のタイトル）と `price`（価格）と `stock`（在庫数）を受け取り、インスタンス変数に保存する。
# -   `sell(amount)` メソッドで本を `amount` 冊販売する。在庫数が足りない場合は、「在庫が足りません」と表示する。
# -   `get_revenue()` メソッドで、**販売した冊数**に応じた総売上を計算して返す。
# -   `show_status()` メソッドで、「〇〇の在庫は△△冊で、現在の売上は××円です」と表示する。
# インスタンスを作成し、本を販売し、売上と在庫の状況を表示してください。
# （ヒント：`get_revenue()`メソッドは、インスタンス変数として販売数を記録しておく必要があります。
class Book:
    def __init__(self, title, price, stock):
        self.title = title
        self.price = price
        self.stock = stock
        self.sold_count = 0

    def sell(self, amount):
        if self.stock < amount:
            print("在庫が足りません")
        else:
            self.stock -= amount
            self.sold_count += amount

    def get_revenue(self):        
        revenue = self.price * self.sold_count  
        return revenue
    
    def show_status(self):
        revenue = self.get_revenue()
        print(f"「{self.title}の在庫は{self.stock}冊で、現在の売上は{revenue}円です」")
        
my_book = Book("python入門", 2200, 10)

my_book.sell(8)
my_book.show_status()

# ## 📝 練習問題2：`Customer` クラス
# **目的：** 顧客情報を管理し、ポイントの計算を行うクラスを作成します。
# ### 問題文
# `Customer` クラスを作ってください。
# -   コンストラクタ（`__init__`）で `name`（顧客名）と `points`（現在のポイント）を受け取り、インスタンス変数に保存する。初期ポイントは`0`とする。
# -   `add_points(amount)` メソッドで、`amount`分のポイントを加算する。
# -   `show_points()` メソッドで、「〇〇さんの現在のポイントは△△です」と表示する。
# インスタンスを作成し、ポイントを加算して表示してください。
class Customer:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def add_points(self, amount):
        self.points += amount
    
    def show_points(self):
        print(f"「{self.name}さんの現在のポイントは{self.points}です」")
        
my_customer = Customer("たろう", 0)
my_customer.add_points(100)
my_customer.show_points()


# 練習問題3（在庫管理の発展）
# 問題文
# Book クラスを作ってください。
# 	•	コンストラクタ（__init__）で title（本のタイトル）と pages（ページ数）を受け取り、インスタンス変数に保存する。
# 	•	add_pages(amount) メソッドでページ数を増やせるようにする。
# 	•	show_pages() メソッドで「〇〇は△△ページです」と表示する。
# やること
# 	•	インスタンスを1つ作ってページ数を追加し、結果を表示してください。
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        
    def add_pages(self, amount):
        self.pages += amount
        
    def show_pages(self):
        print(f"「{self.title}は{self.pages}ページです」")
        
my_book = Book("python入門", 58)
my_book.add_pages(2)
my_book.show_pages()


# 練習問題4（計算を含む）
# 問題文
# BankAccount クラスを作ってください。
# 	•	コンストラクタ（__init__）で owner（口座名義人）と balance（残高、初期値は数値）を受け取り、インスタンス変数に保存する。
# 	•	deposit(amount) メソッドで残高を増やす。
# 	•	withdraw(amount) メソッドで残高を減らす。ただし残高が不足している場合は「残高不足です」と表示して減らさない。
# 	•	show_balance() メソッドで「〇〇さんの残高は△△円です」と表示する。
# やること
# 	•	残高1000円で口座を作る。
# 	•	500円入金する。
# 	•	2000円引き出そうとする。
# 	•	最後に残高を表示する。
