# 【問題文】以下の要件を満たすクラス Calculator を作成してください。

# 要件
# ・次の2つのメソッドを定義すること：
# 1. add()：x + y の結果を返すメソッド
# 2. double_x()：x * 2 の結果を返すメソッド
# ・init（コンストラクタ）は記述しない。
# ・インスタンスを作成し、それぞれのメソッドを呼び出して結果を出力する

class Calculator:# クラスの名前はパスカルケース形式で書く。= 単語ごとに先頭を大文字•クラス名はPascalCaseが慣例（公式スタイルガイドPEP8で推奨）
    def add_number(self, x ,y):# 第1引数の self は超重要：呼び出した“そのインスタンス自身”が自動で渡される。self の名前自体は慣習で、this のイメージ。“自分の本体”と思ってOK。
        add = x + y
        return add#add変数で　x + yを足したものをリターン。add変数はなくreturn x + y　でもOK。今回は理解を深めるために変数を入れている 
    def double_number(self, x):
        double_x = x * 2
        return double_x#上記add_numberと一緒。double_x()：x * 2 の結果を返すメソッド 

my_calc = Calculator()# ここがインスタンス化。設計図Calculatorから実体（オブジェクト）を生成しています。
# Calculator【だけ】だと“設計図そのもの”。Calculator() と括弧をつけることで「作る」。
# my_calc は“私専用の電卓オブジェクト”という意味の変数。複数台作りたいなら Calculator() を何度でも呼べる（各インスタンスは独立）。

add_result = my_calc.add_number(5 ,3)
double_result = my_calc.double_number(6)#インスタンスメソッド呼び出し。 
print(f"足し算の結果{add_result}")
print(f"2倍の結果{double_result}")  #結果を出力   


# 練習問題①（計算あり）
# 以下の要件を満たすクラス Rectangle を作成してください。
# 	•	area(width, height)：長方形の面積（幅×高さ）を返すメソッド
# 	•	perimeter(width, height)：長方形の周の長さ（幅×2 + 高さ×2）を返すメソッド
# 	•	__init__ は使わない（今回も省略）
# 	•	インスタンスを作成し、それぞれのメソッドを呼び出して結果を出力する
# 👉 ポイント：Calculator と同じ形だけど「加算」から「図形の計算」に発展。

class Rectangle:
    def area(self , width , height):
        area_multi = width * height
        return area_multi
    def perimeter(self ,width , height):
        perimeter_multi = width * 2 + height *2
        return perimeter_multi
my_rect = Rectangle()
area_result = my_rect.area(12 , 25)
perimeter_result = my_rect.perimeter(30 ,45) 
print(f"長方形の面積{area_result}")
print(f"長方形の周の長さ{perimeter_result}")       

#   【練習問題２：文章分析ツールを作る】
#   問題:
#   文章を分析するための、様々なツール（メソッド）をまとめた TextAnalyzer というクラスを作成してください。
#   満たすべき要件:
#    1. クラスの名前は TextAnalyzer とする。
#    2. __init__ は記述しない。
#    3. 次の2つのメソッドを定義すること：
#        * count_characters(self, text): 文字列 text を受け取り、その文字数（スペースも含む）を return で返す。
#        * count_words(self, text): 文字列 text を受け取り、その文章に含まれる単語の数を return で返す。
#    4. TextAnalyzerクラスのインスタンスを一つ作成する。
#    5. 作成したインスタンスを使って、任意の文章の「文字数」と「単語数」をそれぞれ計算し、その結果を print() で表示する。
# 1 analyzer = TextAnalyzer()
#    2 my_sentence = "Python is a fun language"
#    3 
#    4 char_count = analyzer.count_characters(my_sentence)
#    5 word_count = analyzer.count_words(my_sentence)
#    6 
#    7 print(f"文章: '{my_sentence}'")
#    8 print(f"文字数: {char_count}")
#    9 print(f"単語数: {word_count}")

#   期待される出力:
#    1 文章: 'Python is a fun language'
#    2 文字数: 25
#    3 単語数: 5

class TextAnalyzer:
    def count_characters(self, text):
        characters = len(text)
        return characters
    def count_words(self, text):
        words = len(text.split())
        return words
analyzer = TextAnalyzer()
my_sentence = "Python is a fun language"
char_count = analyzer.count_characters(my_sentence)
word_count = analyzer.count_words(my_sentence)

print(f"文章: '{my_sentence}'")
print(f"文字数: {char_count}")
print(f"単語数: {word_count}")


# 練習３
# 以下の要件を満たすクラス Greeter を作成してください。
# 	•	hello(name)："こんにちは、◯◯さん！" の文字列を返すメソッド（◯◯は引数の値）
# 	•	goodbye(name)："さようなら、◯◯さん！" の文字列を返すメソッド
# 	•	__init__ は使わない
# 	•	インスタンスを作成し、それぞれのメソッドを呼び出して結果を出力する
# 👉 ポイント：数値計算ではなく「文字列を返す」パターン。return の役割に慣れるのが狙いです。
class Greeter:
    def hello(self, name):
        greet = f"こんにちは、{name}さん！"
        return greet
    def goodbye(self, name):
        wave_hand = f"さようなら、{name}さん！"
        return wave_hand
greeting = Greeter()
name = "太郎"
name2 = "しろう"
hello_message = greeting.hello(name)
bye_message = greeting.goodbye(name2)
print(hello_message)
print(bye_message) 

#   【応用問題４：文字列加工ツールを作る】
#   問題:
#   文字列を加工するための、様々なツール（メソッド）をまとめた StringTool というクラスを作成してください。
#   満たすべき要件:
#    1. クラスの名前は StringTool とする。
#    2. __init__ は記述しない。
#    3. 次の2つのメソッドを定義すること：
#        * add_quotes(self, text): 文字列 text を受け取り、その文字列をダブルクォーテーション（"）で囲んだ新しい文字列を return で返す。（例:
#          "hello" → "\"hello\""）
#        * to_uppercase(self, text): 文字列 text を受け取り、その文字列をすべて大文字に変換した新しい文字列を return で返す。
#    4. StringToolクラスのインスタンスを一つ作成する。
#    5. 作成したインスタンスを使って、上記2つのメソッドをそれぞれ呼び出し、その結果を print() で表示する。

#   期待される出力のイメージ:

#    1 クォート追加結果: "こんにちは"
#    2 大文字変換結果: HELLO WORLD
#   (ヒント: 文字列を大文字に変換するには、文字列変数の末尾に `.upper()` を付けて呼び出します。これはリストの `.append()` 
#   と同じ「メソッド」の一種です。 例: `my_string = "abc"; upper_string = my_string.upper()` )
class StringTool:
    def add_quotes(self, text):
        result = f'"{text}"'
        return result
    def to_uppercase(self, text):
        result = text.upper()
        return result
my_string = StringTool()

quotes_message = my_string.add_quotes("こんにちは")
uppercase_message = my_string.to_uppercase("hello world")
print(quotes_message)
print(uppercase_message)

#   問題５
#   様々な図形の面積を計算するメソッドをまとめた AreaCalculator というクラスを作成してください。
#   満たすべき要件:
#    1. クラスの名前は AreaCalculator とする。
#    2. __init__ は記述しない。
#    3. 次の2つのメソッドを定義すること：
#        * rectangle(self, width, height): 長方形の幅 width と高さ height を受け取り、その面積 (width * height) を return で返す。
#        * triangle(self, base, height): 三角形の底辺 base と高さ height を受け取り、その面積 (base * height / 2) を return で返す。
#    4. AreaCalculatorクラスのインスタンスを一つ作成する。
#    5. 作成したインスタンスを使って、長方形と三角形の面積をそれぞれ計算し、その結果を print() で表示する。
#   期待される出力のイメージ:
#    1 長方形の面積: 50
#    2 三角形の面積: 15.0
class AreaCalculator:
    def rectangle(self, width, height):
        result = width * height
        return result
    def triangle(self, base, height): 
        result = base * height / 2
        return result
my_calc = AreaCalculator()
rectangle_result = my_calc.rectangle(2, 2)
triangle_result = my_calc.triangle(3, 3)
print(rectangle_result)
print(triangle_result)
