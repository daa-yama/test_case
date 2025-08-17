# 空のリスト numbers を用意してください。
# for 文を使って 1 から 5 までの数字を順に取得し、1つずつリストに追加してください。
# 最後にリストの中身を表示してください。
numbers =[]# 空のリストナンバーズを用意。今回定義defはしない。
for num in range(1, 6):# range関数で連続した数字を自動で表示（）の中は必ず入れる。終了値の６は表示されない。for文でループ
    numbers.append(num)# ナンバーズに変数numをappendで追加。
print(numbers)#numbers変数の中身を出力 


# 応用１
# 1から10までの偶数だけをリストに追加し、最後に表示してください。
# 	•	ヒント：偶数は「2で割った余りが0」になる数字。
# 	•	ゴール：[2, 4, 6, 8, 10] が表示されるように。
even_number_list = []
for num in range(1, 11):
    if num % 2 == 0:
        even_number_list.append(num)    
print(even_number_list)

#応用2（計算入り編）
# 1から5までの数字を順に取り出して、それぞれを「2倍した値」をリストに追加し、最後に表示してください。
# 	•	例：1 → 2, 2 → 4, 3 → 6, 4 → 8, 5 → 10
# 	•	ゴール：[2, 4, 6, 8, 10] が表示されるように。
number_list = []
for num in range(1, 6):
    number_list.append(num * 2)
print(number_list)

#  【応用３：Fizz-Listを作る】
#   問題:
#   1から15までの数字を順番に見ていき、次のようなルールで新しいリスト fizz_list を作ってください。
#    * もし、その数字が3で割り切れるなら、数字の代わりに文字列の "fizz" をリストに追加します。
#    * もし、3で割り切れないなら、その数字自体をリストに追加します。
#   満たすべき要件:
#    1. 最初に、fizz_list という名前の空のリストを準備する。
#    2. for文とrange()を使って、1から15までの数字を順番に作り出す。
#    3. ループの中で、if/else文を使って、その数字が3で割り切れるかどうかを判定する。
#    4. 条件に応じて、"fizz" または 数字自体 を fizz_list に .append() で追加する。
#    5. ループがすべて終わったら、最後に fizz_list の中身を print() で表示する。
#   期待される最終的な出力:
#    1 [1, 2, 'fizz', 4, 5, 'fizz', 7, 8, 'fizz', 10, 11, 'fizz', 13, 14, 'fizz']
#   (ヒント: ある数字が3で割り切れるかどうかは、その数字を3で割った余りが0かどうかで判定できます。余りを計算する `%` 記号を使いましょう。 例: `6 
#   % 3` は `0` を返します。)
fizz_list = []
for num in range(1 ,16):
    if num % 3 ==0: 
        fizz_list.append("fizz")
    else: 
        fizz_list.append(num)    
print(fizz_list)

#   【応用問題４：計算結果をリストに格納する（二乗リスト）】
#   問題:
#   1から10までの各数字を、それぞれ二乗した値（同じ数字を2回掛け算した値）を格納したリスト squared_numbers を作ってください。
#   満たすべき要件:
#    1. 最初に、squared_numbers という名前の空のリストを準備する。
#    2. for文とrange()を使って、1から10までの数字を順番に作り出す。
#    3. ループの中で、取り出した数字を二乗する計算を行う。
#    4. 計算結果を、squared_numbers リストに .append() で追加する。
#    5. ループがすべて終わったら、最後に squared_numbers リストの中身を print() で表示する。

#   期待される最終的な出力:
#    1 [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

squared_numbers = []
for num in range(1, 11):
    squared = num ** 2
    squared_numbers.append(squared)
print(squared_numbers)