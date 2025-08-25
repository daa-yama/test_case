# 【問題文】
# StringHandler クラスを作成してください。
# ・upper_text(text)：引数 text を大文字に変換して返すメソッド
# ・repeat_text(text)：引数 text を2回繰り返して返すメソッド
# ・init（コンストラクタ）は記述しない。
# ・インスタンスを作成し、それぞれのメソッドを呼び出して結果を出力してください。
class StringHandler:
    def upper_text(self, text):
        upper_case = text.upper() 
        return upper_case
    def repeat_text(self, text):
        repetition = text * 2
        return repetition
my_string = StringHandler()
text = "hello python"
upper_text_result = my_string.upper_text(text)
repeat_text_result = my_string.repeat_text(text)
print(upper_text_result)
print(repeat_text_result)


    