# 以下のリストを使って、すべての名前を1つずつ表示する print_names() 関数を作ってください。
#  names = ["たろう", "はなこ", "じろう"]
def print_names():
    names = ["たろう", "はなこ", "じろう"]#リスト内だけで動くローカル変数 
    for person in names:#for 変数　in ローカル変数　という形で使う。 
        print(person)# 変数personを出力
print_names()#上の段で関数を定義したのでこれを実行する

# 応用問題１：挨拶とf-string
#   greet() という関数を定義してください。
#   この関数は、名前のリスト users を受け取り、リストの各名前に対して 「〇〇さん、こんにちは！」 という挨拶を表示するものとします。
# 満たすべき要件:
#    * 関数の名前は greet とする。
#    * users = ["たなか", "すずき", "さと"] というリストを引数として関数に渡せるようにする。
#    * forループとf-stringを使って、指定のフォーマットで挨拶を表示する。
#   実行例:
#    1 users = ["たなか", "すずき", "さと"]
#    2 greet(users)
#   期待される出力:
#    1 たなかさん、こんにちは！
#    2 すずきさん、こんにちは！
#    3 さとさん、こんにちは！
users = ["たなか", "すずき", "さと"]
admins = ["管理者A", "管理者B"]

def greet(users_list):
    for hello in users_list:
        print(f"{hello}さん、こんにちは！")
greet(users)
greet(admins)

# 応用問題２　
# 以下のリストの全ての果物を「好きです」と一緒に表示する print_fruits() 関数を作ってください。
# りんごが好きです
# みかんが好きです
# ぶどうが好きです
# fruits = ["りんご", "みかん", "ぶどう"]
# ヒントなしで「for文」を使って書いてください。
def print_fruits():
    fruits = ["りんご", "みかん", "ぶどう"]
    for like in fruits:
        print(f"{like}が好きです。")
print_fruits()

# fruits = ["りんご", "みかん", "ぶどう"]
# salads =["レタス" , "きゅうり" , "セロリ"]
# def print_fruits(yasai):
#     for like in yasai:
#         print(f"{like}が好きです。")
# print_fruits(fruits)
# print_fruits(salads) 関数の外にリストを作る場合の書き方

#応用問題３
# 以下のリストの点数を使って、各人の名前と合計点を表示する print_scores() 関数を作ってください。
# scores = [["たろう", 80, 90, 75],["はなこ", 95, 85, 100],["じろう", 70, 60, 65]]
# 出力例：
# たろうの合計点は245点です
# はなこの合計点は280点です
# じろうの合計点は195点です
# ポイント
# for 文で1人ずつ処理する　sum() 関数を使うと計算が簡単になる
def print_scores():
    scores = [["たろう", 80, 90, 75],["はなこ", 95, 85, 100],["じろう", 70, 60, 65]]
    for total in scores:
        print(f"{total[0]}の合計点は{sum(total [1:])}点です")
print_scores()

# 応用問題４ 
# sum_prices() という関数を定義してください。この関数は、価格のリスト prices を受け取り、すべての価格を合計して、最終的な合計金額を表示するものとします。
#  満たすべき要件:
#    * 関数の名前は sum_prices とする。
#    * prices = [100, 250, 300] というリストを引数として関数に渡せるようにする。
#    * ループの中で、合計金額を保持する変数に、リストの価格を一つずつ足していく。
#    * 最終的に、合計金額を指定のフォーマットで表示する。
#   実行例:
#    1 prices = [100, 250, 300]
#    2 sum_prices(prices)
#   期待される出力:
#    1 合計金額は650円です。
prices = [100, 250, 300]
def sum_prices(price_list):
    total_price = 0
    for i in price_list:
        total_price = total_price + i
    print(f"合計金額は{total_price}です。")
sum_prices(prices)    

# 【応用問題５：最大値を探す】#   find_max_number() という関数を定義してください。
#   この関数は、数値のリスト numbers を受け取り、その中で最も大きい数字を見つけ出して表示します。
#   重要： この問題では、練習のため、Pythonに組み込まれている便利な max()
#   関数は使わないでください。forループを使って、自分で最大値を見つけ出すロジックを組み立てるのが目的です。
#   満たすべき要件:
#    * 関数の名前は find_max_number とする。
#    * numbers = [34, 12, 58, 9, 77, 54] のようなリストを引数として関数に渡せるようにする。
#    * 「今まで見た中で一番大きい数」を一時的に保存しておく変数を一つ使う。
#    * ループの中で、その変数とリストの新しい値を比較し、もし新しい値の方が大きければ、変数を更新する。
#    * 最終的に、見つけ出した最大値を指定のフォーマットで表示する。
#   実行例:
#    1 scores = [65, 92, 78, 85, 95, 43]
#    2 find_max_number(scores)
#   期待される出力:
#  リストの中で最も大きい数字は95です。
numbers = [34, 12, 58, 9, 77, 54]
def find_max_numbers(scores):
    max_number = scores[0]
    for i in scores:
        if i > max_number:
            max_number = i
    print(f"リストの中で最も大きい数字は{max_number}です。")
find_max_numbers(numbers)
        