# 次のリストがあります。
# names = ["たろう", "はなこ", "じろう"]
# 新しい名前を引数として受け取り、リストに追加する関数 add_name(new_name) を作ってください。
# 関数を使って "さぶろう" を追加した後、リストの中身をすべて表示してください。

names = ["たろう", "はなこ", "じろう"]#グローバル変数で関数の外からでも変更できるようにする。 
def add_name(new_name):
    names.append(new_name)#グローバル変数に追加する.append関数を入れている。 
add_name("さぶろう")
add_name("しろう")
print(names)
    
    
#     【応用問題１：条件に合う要素だけを集めた新しいリストを作る】
#   filter_short_strings() という関数を定義してください。
#   この関数は、文字列のリストと、許容する最大文字数を受け取り、指定された文字数以下の要素だけを含む新しいリストを返します。
#   満たすべき要件:
#    * 関数の名前は filter_short_strings とする。
#    * 引数として、文字列のリスト string_list と、整数の max_length を受け取る。
#    * 関数の中で新しい空のリストを準備する。
#    * string_list をループで確認し、文字数が max_length 以下の文字列だけを、新しいリストに追加していく。
#    * 元の string_list は変更しない。
#    * 最後に、新しく作ったリストを return で返す。
#   実行例:
#    1 words = ["Python", "is", "a", "programming", "language"]
#    2 short_words = filter_short_strings(words, 6) # 6文字以下の単語を抽出
#    3 
#    4 print(f"短い単語のリスト: {short_words}")
#    5 print(f"元のリスト: {words}")
#   期待される出力:
#    1 短い単語のリスト: ['Python', 'is', 'a']
#    2 元のリスト: ['Python', 'is', 'a', 'programming', 'language']
#   (ヒント: 文字列の長さを調べるには `len()` 関数が使えます。例: `len("Python")` は `6` を返します)
#    * 引数として、文字列のリスト string_list と、整数の max_length を受け取る。
words = ["Python", "is", "a", "programming", "language"] 
def filter_short_strings(string_list, max_length):
    empty_list =[]
    for word in string_list:
        if len(word) <= max_length:
            empty_list.append(word)
    return empty_list
short_words = filter_short_strings(words, 6)
print(f"短い単語のリスト: {short_words}")
print(f"元のリスト: {words}")

# 応用問題２（計算あり）
# クラスの生徒のテスト点数を記録するプログラムを作ってください。
# 	•	最初に以下のリストがあります：
# scores = [80, 90, 75]
# 	•	新しい点数を引数として受け取り、scores に追加する関数 add_score(new_score) を作ってください。
# 	•	その後、scores の平均点を計算して表示してください。
# 	•	実行例：
# 平均点: 83.75

scores = [80, 90, 75]
def add_score(new_score):
    scores.append(new_score)
    total = sum(scores)/len(scores)
    return total
result = add_score(77)
print(f"平均点：{result}")

# 応用問題3（文字列加工）
# ユーザーが好きな食べ物を登録できるプログラムを作ってください。
# 	•	最初に以下のリストがあります：
# foods = ["りんご", "カレー"]
# 	•	新しい食べ物を引数として受け取り、foods に追加する関数 add_food(new_food) を作ってください。
# 	•	追加する前に、引数の文字列から全角スペース・半角スペースを取り除く処理をしてください（例： " カレー " → "カレー"）。
# 	•	最終的に foods の中身をすべて表示してください。
foods = ["りんご", "カレー"]
def add_food(new_food):
    foods.append(new_food.strip())
add_food("                シチュー    ")
add_food("　　みかん　　") 
print(foods)   

# 【応用問題４】クラスのテスト結果から**合格率（80点以上の割合）**を表示するプログラムを作ってください。
# 前提リスト
# scores = [60, 72, 85, 90]
# やること
# 	1.	新しい点数を引数として受け取り、scores に追加する関数 add_score(new_score) を作る。
# 	2.	関数を使って 88 を追加する。
# 	3.	追加後の scores について、80点以上の人数と全体人数から
# 	•	合格率（%）＝ 80点以上の人数 / 全体人数 * 100を求め、小数点1桁で表示する。
# 	4.	形式は次のようにすること：
# 	•	合格率行：合格率: 60.0% (3/5人) のように 割合と (合格者/全体) を併記
# 	•	確認用に scores の中身も最後に表示する
# 期待される出力（例）
# 合格率: 60.0% (3/5人)
# [60, 72, 85, 90, 88]
scores = [60, 72, 85, 90]
def add_score(new_score):
    scores.append(new_score)
    total = len([score for score in scores if score  >= 80])
    rate = total/len(scores)*100
    return total ,rate
total , rate = add_score(88)
print(f"合格率：{rate:.1f}% ({total}/{len(scores)}人)")
print(scores)


#   【応用問題５：計算結果を新しいリストにして返す】
#   create_doubled_list() という関数を定義してください。
#   この関数は、数値のリストを受け取り、各要素を2倍にした結果を含む新しいリストを返します。
#   満たすべき要件:
#    * 関数の名前は create_doubled_list とする。
#    * 引数として、数値のリスト number_list を受け取る。
#    * 関数の中で新しい空のリストを準備する。
#    * number_list をループで確認し、各数値を2倍した結果を、新しいリストに追加していく。
#    * 元の number_list は変更しない。
#    * 最後に、新しく作ったリストを return で返す。

#   実行例:

#    1 numbers = [1, 2, 3, 4, 5]
#    2 doubled_numbers = create_doubled_list(numbers)
#    3 
#    4 print(f"2倍にしたリスト: {doubled_numbers}")
#    5 print(f"元のリスト: {numbers}")
#   期待される出力:
#    1 2倍にしたリスト: [2, 4, 6, 8, 10]
#    2 元のリスト: [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 5]
def  create_doubled_list(number_list):
    empty_list = []
    for n in number_list:
        doubled_value = n *2
        empty_list.append(doubled_value)
    return empty_list
doubled_numbers = create_doubled_list(numbers)

print(f"2倍にしたリスト: {doubled_numbers}")
print(f"元のリスト: {numbers}")