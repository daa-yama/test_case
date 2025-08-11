# 【問題】
# 3つの文字列を引数として受け取り、それらをスペースでつなげた文字列を戻り値として返す関数を作ってください。
# 関数名は combine_words とし、引数に "Hello", "Python", "World" を与えて呼び出してください。
# 戻り値を出力してください。

# 【条件】
# ・関数定義は3行で記述してください。
# ・処理を実施する際には必ず変数を用いてください。変数名は「joint_words」とする
# ・呼び出しの際には2行で記述してください。
def combine_words(w1, w2, w3):#w１w２w３は文章を入れる入れ物 
        joint_words =w1 + " " + w2 + " " +w3#変数名joint_wordsを定義。スペースで繋げる””の間にスペース、スペースの間にも＋を入れる。 
        return joint_words#変数を呼び出し元に戻す 
result = combine_words("Hello", "Python", "World" )#result（結果）という変数を作り引数の文字を入れる 
print(result)# 結果を出力する


#応用問題 1：フルネーム生成
#姓（last name）と名（first name）を引数として受け取り、間にスペースを入れたフルネームの文字列を返す関数 create_full_name を作ってください。
#引数: last_name, first_name
#戻り値: last_name と first_name をスペースでつないだ文字列 (例: "山田 太郎")
#制約:
#関数定義は3行で記述してください。
#関数内では full_name という変数を使ってください。
#呼び出しと結果の表示は2行で記述してください。
#呼び出し例: create_full_name("山田", "太郎") で呼び出す。

def create_full_name(last_name , first_name):
    full_name = last_name + " " + first_name
    return full_name
result = create_full_name("山田" ,"太郎")
print(result)    

#応用問題 2：長方形の面積計算
#長方形の幅（width）と高さ（height）を引数として受け取り、その面積を計算して返す関数 calculate_area を作ってください。
#引数: width, height
#戻り値: width と height を掛け算した結果の数値
#制約:
#関数定義は3行で記述してください。
#関数内では area という変数を使ってください。
#呼び出しと結果の表示は2行で記述してください。
#呼び出し例: calculate_area(10, 5) で呼び出す。

def calculate_area(width , height):
    area = width * height
    return area
result = calculate_area(10 , 5)
print(result)
#補足   変数名の有効範囲（スコープ）について
#   今回の問題では、2種類の変数が登場しました。
#    1. 関数の中で使われる変数 (`area`)
#        * これは問題の制約で area という名前にする必要がありました。
#        * この area 変数は、calculate_area 関数の中だけで生きている変数です。関数が終わると消えてしまいます。
#    2. 関数の外で、戻り値を受け取る変数 (`result`)
#        * こちらは問題に制約がなかったので、あなたが自由に名前を決められます。
#        * result（結果）は、中身が分かりやすいとても良い名前です。
#        * calculation_result や sankaku_no_menseki など、ルールに沿っていればどんな名前でも構いません。
#   例え：
#   calculate_area が「面積計算工場」だとします。
#    * 工場の中では、部品を area という名前の箱に入れています（これは工場のルール）。
#    * 工場から製品（計算結果）が出荷された後、あなたはそれを受け取って result
#      という名前の自分の箱に入れます。この自分の箱の名前は、あなたが自由に決めて良い、ということです。


#   応用問題 3：メールアドレス生成
#   ユーザー名（username）とドメイン名（domain）を引数として受け取り、それらを @ でつないだ完全なメールアドレスを返す関数 generate_emailを作ってください。
#引数: username, domain
#戻り値: username と domain を @ でつないだ文字列 (例: "taro.yamada@example.com")
#制約:
#関数定義は3行で記述してください。
#関数内では email_address という変数を使ってください。
#呼び出しと結果の表示は2行で記述してください。
#呼び出し例: generate_email("taro.yamada", "example.com") で呼び出す。

def generate_email(username , domain):
    email_address = username + "@" + domain
    return email_address
address = generate_email("taro.yamada" , "example.com")
print(address)
address_hanako = generate_email("hanako" , "google.com")
print(address_hanako)

# 応用問題4：reverse_words
# 3つの文字列を引数として受け取り、それらの順番を逆にしてスペースでつなげた文字列を戻り値として返す関数 reverse_words を作ってください。
# 引数には "Python", "is", "fun" を渡し、戻り値を変数に入れて出力してください。

def reverse_words(w1 ,w2, w3):
    rwords = w3 + " " + w2 + " " +w1
    return rwords
result =reverse_words("Python", "is", "fun")
print(result)


#応用問題５：add_numbers
# 2つの数値を引数として受け取り、それらの合計を計算して戻り値として返す関数 add_numbers を作ってください。
# 戻り値を変数に保存し "合計は <合計値> です。"という文章を表示してください。
#条件
#関数定義は3行（def → 計算して変数に保存 → return）
#呼び出しは2行（変数に入れる → print）
#足す数値は 15 と 27
def add_numbers(x , y):
    add = x + y
    return add
result = add_numbers(15 , 27)
print(f"合計は<{result}>です。")

#応用問題６：word_count
# 1つの文字列を引数として受け取り、その文字列の単語数を数えて戻り値として返す関数 word_count を作ってください。
# 呼び出し時に "I love learning Python programming" を渡し、戻り値を変数に保存して「単語数: ○個」と表示してください。
# （ヒント：split() を使うとスペース区切りで単語に分けられます）
def word_count(text):
    words = text.split()
    return len(words)
result = word_count("I love learning Python programming")
print(f"単語数：{result}個")
