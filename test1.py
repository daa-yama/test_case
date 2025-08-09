# 「こんにちは！」と表示する関数 `say_hello` を定義し、それを呼び出してください。
# 前提条件
# 1ファイルにて完結するようにしてください
 
def say_hello():   #defは関数の定義　ここではsay_helloという名前の関数の箱を作る。（）は実行するボタン。：コロンはここから関数の中身が始まりますよという合図。  
    print("こんにちは！")   #printは画面に文字を表示するする関数。（）は実行するスイッチ  ””はただの文字列ですよという意味。これがないと関数として定義されてしまう。
say_hello() # ()で関数を実行させている。もし () をつけずに say_helloとだけ書くと関数扱いで実行できない。

#    * ()：関数の宣言や実行で使うアクションのしるし。
#    * :ここからコードの中身が始まりますよ、という合図。コロンの後はインデント（字下げ）をする。
#    * ""これはプログラムではなくただの文字列ですよ、という囲い。

# 応用問題① 「おやすみなさい」と表示する関数 say_good_night を定義し、それを呼び出してください。
def say_good_night():
    print("おやすみなさい")
say_good_night()

# 応用問題② あなたの名前（もしくはニックネーム）を使って、「（あなたの名前）です。よろしくお願いします！」と表示する関数 introduce_selfを定義し、それを呼び出してください。

def introduce_self(name):
    print(f"{name}です。よろしくお願いします！")
introduce_self("だーやま")

#  応用問題③「処理が完了しました。」と表示する関数 show_completion_message を定義し、それを呼び出してください。
def  show_completion_message():
    print("処理が完了しました")
show_completion_message()

# 応用問題④ good_morning という名前の関数を定義し、呼び出すと 「おはよう！」 と表示されるようにしてください。1ファイルにまとめて実行してください。
def good_morning():
    print("おはよう！")
good_morning()

# 応用問題⑤ greet という名前の関数を定義し、引数に名前を渡すと 「こんにちは、〇〇さん！」 と表示されるようにしてください。
def greet(name):
    print(f"こんにちは、{name}さん！")
greet("だーやま")

# 応用問題⑥ repeat_hello という名前の関数を定義し、呼び出すと 「こんにちは！」 を3回表示してください。※ 同じ関数を3回呼ぶ方法でも、ループを使ってもOK。
def repeat_hello():
    print("こんにちは！")
repeat_hello()
repeat_hello()
repeat_hello()

# ループを使った場合
def repeat_hello():
    print("こんにちは！")
for i in range(3):# iはindexの略アンダーバーや好きな文字列でもOK
    repeat_hello()