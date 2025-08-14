# 【問題】# ある年齢をもとに、以下のように表示する関数check_stageを作ってください。
# ・13歳未満 → 「子どもです」
# ・13歳以上 18歳未満 → 「中高生です」
# ・18歳以上 → 「大人です」
# 【条件】
# ・関数の処理部分:6行で記述
def check_stage(age):
    if age < 13:#< は「より小さい」の比較演算子。ここでは１３未満になるので＜。１３歳も含める場合は<=
        print("子どもです")
    elif age < 18:# elifは "else if" の略で、1つ目のif条件が成り立たず、かつ、こちらの条件が成り立つならば」という意味。 
        # age >= 13 and age < 18 という書き方もできるが今回の方がシンプルな見た目になる。
        print("中高生です")
    else:#ifにもelifにも当てはまらない場合。今回の場合は１８歳位以上  
        print("大人です") 
check_stage(17)

#  練習問題１：成績評価
#   テストの点数 (score) を引数として受け取り、成績を評価して表示する関数 check_grade(score) を作ってください。
#    * 評価ルール:
#        * 90点以上 → 「優」
#        * 80点以上 90点未満 → 「良」
#        * 60点以上 80点未満 → 「可」
#        * 60点未満 → 「不可」
#    * 条件:
#        * 関数の処理部分は8行で記述してください。
def check_grade(score):
    if score >= 90:
        print("優")
    elif score >= 80:
        print("良") 
    elif score >= 60:
        print("可")
    else:
        print("不可")
check_grade(59)

#   練習問題２：遊園地の料金計算
#   ある遊園地の入場料を計算する関数 check_ticket_price(age) を作ります。
#   基本料金は 2000円 です。年齢 (age) に応じて、以下の料金を計算し、指定されたフォーマットで表示してください。
#    * 料金ルール:
#        * 6歳未満: 無料
#        * 6歳以上 18歳未満: 50%割引
#        * 65歳以上: 30%割引
#        * それ以外 (18歳以上 65歳未満): 通常料金（割引なし）
#    * 表示フォーマット:
#        * 割引がある場合は、割引後の料金と、いくら割引されたのかを表示してください。
#        * 呼び出し例:
#            * check_ticket_price(5) → 「入場料は無料です。」
#            * check_ticket_price(10) → 「入場料は1000円です。(1000円の割引が適用されました)」
#            * check_ticket_price(30) → 「入場料は2000円です。」
#            * check_ticket_price(70) → 「入場料は1400円です。(600円の割引が適用されました)」
def check_ticket_price(age):
    base_price = 2000
    price =0
    discount = 0
    
    if age < 6:
        print("入場料は無料です")
        return
    elif 6 <= age < 18:
        discount = base_price * 0.5
        price = base_price - discount
    elif age >= 65:
        discount = base_price *0.3
        price = base_price - discount
    else:
        price = base_price
    if discount > 0:
        print(f"入場料は{int(price)}円です。({int(discount)}円の割引が適用されました)")
    else:
        print(f"入場料は{int(price)}円です。")

check_ticket_price(5)
check_ticket_price(20)
check_ticket_price(66)
check_ticket_price(17)
        
        
# 練習問題３：宅配便の料金計算
#   ある宅配サービスの送料を計算する関数 calculate_delivery_fee(weight, is_express) を作ります。
# 荷物の重さ weight (kg) と、速達かどうか is_express (True または False)の2つの情報をもとに、以下のルールで料金を計算し、指定されたフォーマットで表示してください。
#   料金ルール: 1. 基本料金
#        * 荷物の重さによって、まず基本となる料金が決まります。
#            * 2kg 以下: 500円
#            * 2kg を超え 5kg 以下: 800円
#            * 5kg を超え 10kg 以下: 1100円
#    2. 速達金
#        * もし is_express が True の場合、上記で計算した基本料金に、追加で 400円 が加算されます。
#    3. 特別ルール
#        * 重さが 10kg を超える荷物は、配送することができません。
#   表示フォーマット:
#    * 速達ではない場合:
#        * 「送料は〇〇円です。」
#    * 速達の場合:
#        * 「送料は〇〇円です。(速達料金400円を含みます)」
#    * 配送できない場合:
#        * 「10kgを超える荷物は配送できません。」
#   呼び出し例:
#    * calculate_delivery_fee(1.5, False) → 「送料は500円です。」
#    * calculate_delivery_fee(4, False) → 「送料は800円です。」
#    * calculate_delivery_fee(7, True) → 「送料は1500円です。(速達料金400円を含みます)」 (1100円 + 400円)
#    * calculate_delivery_fee(1, True) → 「送料は900円です。(速達料金400円を含みます)」 (500円 + 400円)
#    * calculate_delivery_fee(12, False) → 「10kgを超える荷物は配送できません。」

def calculate_delivery_fee(weight, is_express) :
    if weight > 10:
        print("10kgを超える荷物は配送できません。")
        return
    base_fee = 0
    
    if weight <= 2:
        base_fee = 500
    elif 2 < weight <= 5:
        base_fee = 800
    elif 5 < weight <= 10:
        base_fee = 1100
    express_fee = 0
    if is_express == True:
        express_fee = 400
    total_fee = base_fee + express_fee
    
    if is_express == True:
        print(f"送料は{total_fee}円です。速達料金{express_fee}円を含みます。")
    else:
        print(f"送料は{total_fee}円です。")    
calculate_delivery_fee(3 ,True)
calculate_delivery_fee(10 ,False)
calculate_delivery_fee(1 ,False)
calculate_delivery_fee(1 , True)
calculate_delivery_fee(11 , True)

#練習問題４ お天気メッセージ関数 check_weather を作ってください。
# 引数として天気（文字列 "晴れ" / "くもり" / "雨"）を受け取り、以下のように表示してください。
# •	"晴れ" → 「今日はピクニック日和です」
# •	"くもり" → 「今日は読書日和です」
# •	"雨" → 「今日は映画日和です」
# •	上記以外 → 「天気がよくわかりません」
# 	•	関数の処理部分は6行で書く
# 	•	if / elif / else を使う

def check_weather(weather):
    if weather == "晴れ": message = "今日はピクニック日和です。"
    elif weather == "くもり": message = "今日は読書日和です。"
    elif weather == "雨": message = "今日は映画日和です。"
    else: message = "天気がよく分かりません"
    print(message)
    
check_weather("雪")

# 練習問題５　BMIを判定する関数 check_bmi を作ってください。
# 引数として 身長（cm） と 体重（kg） を受け取り、BMIを計算して以下のように表示してください。
# BMIの計算式：
# BMI = 体重(kg) / (身長(m) の2乗)
# （注意：身長はmに変換して計算すること）
# 判定基準：
# 	•	BMI 18.5未満 → 「やせ型です」
# 	•	BMI 18.5以上 25未満 → 「標準体型です」
# 	•	BMI 25以上 → 「肥満です」
# 条件
# 	•	関数の処理部分は7行以内
# 	•	小数点1桁でBMIを表示してから判定結果を出す
def check_bmi(cm , kg):
    height_m = cm/100
    BMI = kg / (height_m**2)
    if BMI < 18.5: message = "やせ型です"
    elif 18.5 <= BMI < 25: message = "標準体型です"
    else: message = "肥満です"
    print(f"BMIは {BMI:.1f} です")
    print(message)

check_bmi(173 , 73)