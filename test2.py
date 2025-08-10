# 名前を受け取ってあいさつをする関数 `greet` を作ってください。
# 名前が指定されなかったら「こんにちは、ゲストさん！」と表示されるようにしてください。
# 例）greet() → 「こんにちは、ゲストさん！」
#     greet("さくら") → 「こんにちは、さくらさん！」　呼び出し時は引数はキーワードを使って定義してください。

def greet(name="ゲスト"):#greetを定義。名前が指定されなかった場合の引数nameにゲストを入れる。 
    print(f"こんにちは、{name}さん！")# f文字列で出力される言葉を作っている。{}内に引数を入れる。
greet()#引数がないのでゲストさんの表示 
greet(name="さくら")#キーワード引数さくらを指定している


# =　の意味。大きく分けて３つある。
# ①関数定義の = → 「指定がない場合これを使う（保険）　例：name="ゲスト"」
# ②関数呼び出しの = → 「この名前にこの値をあげる（指定）　例：name="さくら"」
# ③普通のコードの = → 「右の値を左に入れる（箱に物を入れるイメージ）例：x=5」




# 練習問題 1
# 飲み物を注文する関数 order_drink を作ってください。
# * 条件：
# * 引数で飲み物の名前 name を受け取ります。
# * 名前が指定されなかった場合は、デフォルトで「コーヒー」を注文するようにしてください。
# * 呼び出すときはキーワード引数を使ってください。
# * 実行例：
# * order_drink() → 「コーヒーをください。」 と表示される。
# * order_drink(name="紅茶") → 「紅茶をください。」 と表示される。
def order_drink(name="コーヒー"):
    print(f"「{name}をください」")
order_drink()
order_drink(name="紅茶")
    
    
# 練習問題 2
# ゲームの難易度を設定する関数 set_difficulty を作ってください。
# * 条件：
# * 引数で難易度 level を受け取ります。
# * 難易度が指定されなかった場合は、デフォルトで「ノーマル」になるようにしてください。
# * 呼び出すときはキーワード引数を使ってください。
# * 実行例：
# * set_difficulty() → 「難易度をノーマルに設定しました。」 と表示される。
# * set_difficulty(level="ハード") → 「難易度をハードに設定しました。」 と表示される。

def set_difficulty(level="ノーマル"):
    print(f"「難易度を{level}に設定しました。」")
set_difficulty()
set_difficulty(level="ハード")

# 
# 練習問題 3
# ログインメッセージを表示する関数 show_login_message を作ってください。
# * 条件：
#        * 引数で user_name を受け取ります。
#        * ユーザー名が指定されなかった場合は、デフォルトで「管理者」としてログインするようにしてください。
#        * 呼び出すときはキーワード引数を使ってください。
#    * 実行例：
#        * show_login_message() → 「ようこそ、管理者さん。」 と表示される。
#        * show_login_message(user_name="はなこ") → 「ようこそ、はなこさん。」 と表示される。

def show_login_message(user_name="管理者"):
    print(f"「ようこそ、{user_name}さん。」")
show_login_message()
show_login_message(user_name="はなこ")


# 練習問題④
# 関数名： introduce
# 	•	引数 name（デフォルト値 "不明"）と age（デフォルト値 "秘密"）を受け取る
# 	•	実行時に
# 	•	introduce() → 「名前: 不明 / 年齢: 秘密」
# 	•	introduce(name="太郎") → 「名前: 太郎 / 年齢: 秘密」
# 	•	introduce(age=20) → 「名前: 不明 / 年齢: 20」
# 	•	introduce(name="花子", age=25) → 「名前: 花子 / 年齢: 25」になるように作ってください。

def introduce(name = "不明", age = "秘密"):
    print(f"「名前：{name} / 年齢：{age}」")
introduce()
introduce(name="太郎")
introduce(age=20)
introduce(name= "花子", age=25)

# 練習問題⑤

# 関数名： order
# 	•	引数 item（デフォルト値 "コーヒー"）と size（デフォルト値 "M"）を受け取る
# 	•	出力例：
# 	•	order() → 「ご注文は M サイズのコーヒーですね」
# 	•	order(item="紅茶") → 「ご注文は M サイズの紅茶ですね」
# 	•	order(size="L") → 「ご注文は L サイズのコーヒーですね」
# 	•	order(item="抹茶", size="S") → 「ご注文は S サイズの抹茶ですね」

def order(item="コーヒー", size="M"):
    print(f"「ご注文は {size} サイズの{item}ですね」")
order()
order(item="紅茶")
order(size="L")
order(item="抹茶", size="S")

# 練習問題6

# 関数名： calculate_price
# 	•	引数 price（必須）と tax（デフォルト値 0.1）を受け取り、税込価格を計算して表示する
# 	•	出力例（税率は小数で指定、デフォルトは 0.1 = 10%）：
# 	•	calculate_price(price=1000) → 「税込価格は 1100 円です」
# 	•	calculate_price(price=2000, tax=0.08) → 「税込価格は 2160 円です」 

def calculate_price(price, tax=0.1):
    print(f"税込価格は {price * (1 + tax):,.0f} 円です")
calculate_price(price=1000)
calculate_price(price=2000, tax=0.08)