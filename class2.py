# TextEditor クラスを作ってください。
# 下記の内容を反映させた次の2つのメソッドを定義して
# インスタンスを作成し、それぞれのメソッドを呼び出して結果を出力してください。
# ・to_upper(text)：文字列 text を大文字に変換して返すメソッド
# ・reverse_text(text)：文字列 text を逆順にして返すメソッド
# ・init（コンストラクタ）は記述しない。
class TextEditor:
    def to_upper(self, text):
        upper_text = text.upper()
        return upper_text
    def reverse_text(self, text):
        reversed_text = text[::-1]
        return reversed_text
my_text = TextEditor()
words = "hello python"
upper_result = my_text.to_upper(words)
reverse_result = my_text.reverse_text(words)
print(upper_result)
print(reverse_result)

# スライスについて詳細  ##### reverse_text = text[::-1]
#  技術的解説（最重要）： この一行が、今回の問題の核心となる新しいテクニックです。これは拡張スライス（extended slicing）構文を利用しています。
# 1. Pythonのシーケンス型（文字列、リスト、タプルなど）は、[]を使って要素にアクセスできます。この[]の中にコロン:を入れることで、一部分を切り
#           出す「スライス」操作ができます。
# 2. スライスの完全な構文は [start:stop:step] です。
#            * start: スライスを開始するインデックス（省略すると最初から）。
#            * stop: スライスを終了するインデックス（このインデックスの手前まで）。
#            * step: スライスする際の増分（何個おきに進むか）。
# 3. [::-1]という指定は、この構文を巧みに利用したものです。
#            * startが省略されているため、「シーケンスの端から」を意味します。
#            * stopが省略されているため、「シーケンスのもう一方の端まで」を意味します。
#            * stepに-1が指定されています。これが最も重要で、「1つずつ、逆方向に進む」ことを指示します。
# 4. これらを総合すると、[::-1]は「シーケンスの末尾から先頭に向かって、1文字ずつすべての要素を取り出す」という操作になります。この操作の結果
#           、元の文字列とは逆順の文字で構成された、新しい文字列オブジェクトが生成されます。
# 5. この新しく生成された逆順の文字列オブジェクトへの参照が、ローカル変数reverse_textに代入されます。



#  練習問題1（文字列操作系）
# 問題文：
# StringTools クラスを作ってください。
# 以下の2つのメソッドを定義し、インスタンスを作成して呼び出し、結果を出力してください。
# 	1.	count_vowels(text)
# 	•	引数の文字列 text に含まれる母音（a, i, u, e, o）の数を数えて返すメソッド。
# 	•	大文字・小文字の区別はしない。
# 	2.	repeat_text(text, n)
# 	•	文字列 text を n 回繰り返して返すメソッド
class StringTools:
    def count_vowels(self, text):
        vowels = "aiueo"
        text_lower = text.lower()
        count = 0   
        for ch in text_lower:
            if ch in vowels:
                count += 1   
        return count
    def repeat_text(self, text, n):
        repeat_word = text * n
        return repeat_word
my_tools = StringTools()
text = "Hello Python"
vowels_result = my_tools.count_vowels(text)
repeat_result = my_tools.repeat_text(text, 3)
print(vowels_result)
print(repeat_result)
        

#  練習問題2（計算が入る系）
# 問題文：
# Calculator クラスを作ってください。
# 以下の2つのメソッドを定義し、インスタンスを作成して呼び出し、結果を出力してください。
# 	1.	square(number)
# 	•	引数の数値 number を2乗にして返すメソッド。
# 	2.	average(numbers)
# 	•	引数としてリスト numbers を受け取り、その平均値を返すメソッド。
# 	•	ヒント：平均は「合計 ÷ 要素数」
class Calculator:
    def square(self, number):
        value = number ** 2
        return value
    def average(self, numbers):
        total = sum(numbers)/len(numbers)
        return total
my_cal = Calculator()
number = 8
numbers = [8, 10 ,12, 16]
square_value = my_cal.square(number)
average_total = my_cal.average(numbers)
print(square_value)
print(average_total)
#   ##### total = sum(numbers) / len(numbers)
#    * 技術的解説: この一行は、Pythonの強力な組み込み関数を活用した、非常に効率的な処理です。
#        1. `sum(numbers)`: 組み込み関数sum()が、引数numbers（今回はタプル）と共に呼び出されます。sum()は、リストやタプルのようなイテラブル（反復可
#           能）なオブジェクトを受け取り、その中の全要素の合計値を計算して返します。sum((5, 8, 12))は、25という整数を返します。
#        2. `len(numbers)`: 組み込み関数len()が、同じく引数numbersと共に呼び出されます。len()もまた、イテラブルなオブジェクトを受け取り、その要素数
#           を返します。len((5, 8, 12))は、3という整数を返します。
#        3. `/`: 最後に、除算演算子/が、sum()の返り値25をlen()の返り値3で割ります。Python
#           3では、除算の結果は常に浮動小数点数（float）になるため、8.333...というfloatオブジェクトが生成されます。
#        4. この最終的な計算結果（floatオブジェクト）への参照が、ローカル変数totalに代入されます。


#応用問題3：リスト加工ツールを作る】
#   問題:
#   リストデータを加工するための、様々なツール（メソッド）をまとめた ListProcessor というクラスを作成してください。
#   満たすべき要件:
#    1. クラスの名前は ListProcessor とする。
#    2. __init__ は記述しない。
#    3. 次の2つのメソッドを定義すること：
#        * get_sum(self, num_list): 数値のリスト num_list を受け取り、その要素の合計値を return で返す。
#        * remove_duplicates(self, item_list): 様々な要素（数値や文字列）が入ったリスト item_list
#          を受け取り、そこから重複する要素をすべて取り除いた新しいリストを return で返す。（注意：返されるリストの要素の順序は問わない）
#    4. ListProcessorクラスのインスタンスを一つ作成する。
#    5. 作成したインスタンスを使って、上記2つのメソッドをそれぞれ呼び出し、その結果を print() で表示する。
#   期待される出力のイメージ:
#    1 リストの合計値: 30
#    2 重複を除いたリスト: [1, 2, 3, 4, 5]  (または [1, 2, 3, 4, 5] 以外の順序でも可)
#   (ヒント１: リスト内のすべての数値を合計するには、便利な組み込み関数 `sum()` が使えます。例: `sum([10, 20])` は `30` を返します。)
#   (ヒント２: リストから重複をなくす最も簡単な方法は、一度リストを `set` という別のデータ型に変換し、それを再び `list` に戻すことです。`set` 
#   は重複を許さない性質を持っています。例: `my_list = [1, 2, 2, 3]; unique_list = list(set(my_list))`)
class ListProcessor:
    def get_sum(self, num_list):
        number = sum(num_list)
        return number
    def remove_duplicates(self, item_list):
        unique_list = list(set(item_list))
        return unique_list
my_list = ListProcessor()
get_sum_result = my_list.get_sum([10, 10, 20])
remove_duplicates_result = my_list.remove_duplicates([1, 2, 2, 3, 3, 4, 4, 5])
print(get_sum_result)
print(remove_duplicates_result)


# 【応用問題４：簡単な利息計算ツールを作る】
#   問題:
#   簡単な銀行の計算を行う SimpleBank というクラスを作成してください。
#   満たすべき要件:
#    1. クラスの名前は SimpleBank とする。
#    2. __init__ は記述しない。
#    3. 次の2つのメソッドを定義すること：
#        * calculate_interest(self, principal, rate, years): 元本 principal、年利 rate（例: 5%なら0.05）、年数 years
#          の3つを受け取り、得られる利息の額（単利）を return で返す。計算式: 利息 = 元本 * 年利 * 年数
#        * get_final_balance(self, principal, rate, years): 同じ3つの引数を受け取り、最終的な残高（元本 + 利息）を return で返す。
# 計算式: 最終残高 = 元本 + (元本 * 年利 * 年数)
#    4. SimpleBankクラスのインスタンスを一つ作成する。
#    5. 作成したインスタンスを使って、「100,000円を年利3%で5年間預けた」場合の「利息」と「最終残高」をそれぞれ計算し、print() で表示する。
#   期待される出力のイメージ:
#    1 得られる利息: 15000.0
#    2 5年後の最終残高: 115000.0
class SimpleBank:
    def calculate_interest(self, principal, rate, years):
        total = principal * rate * years
        return total
    def get_final_balance(self, principal, rate, years):
        final_total = principal + (principal * rate * years)
        return final_total
my_bank = SimpleBank()
principal = 100000
rate = 0.03
years = 5
calculate_interest_result = my_bank.calculate_interest(principal, rate, years)
get_final_balance_result = my_bank.get_final_balance(principal, rate, years)
print(calculate_interest_result)
print(get_final_balance_result)