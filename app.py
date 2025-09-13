from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "kN0<@K0}dG3{s>9B@7nCs/=;UyQ"

# topic.htmlと連動
topics = [
    ["りんご", "みかん"],
    ["犬", "猫"],
    ["学校", "図書館"],
    ["電車", "バス"],
    ["ピザ", "ハンバーガー"],
    ["海", "川"],
    ["サッカー", "バスケ"],
    ["春", "秋"],
    ["コーヒー", "紅茶"],
    ["車", "バイク"],
    ["パン", "ご飯"],
    ["ピアノ", "ギター"],
    ["スイカ", "メロン"],
    ["ねこ", "ねずみ"],
    ["犬小屋", "猫ハウス"],
    ["鉛筆", "ペン"],
    ["リンゴジュース", "オレンジジュース"],
    ["自転車", "キックボード"],
    ["映画館", "カラオケ"],
    ["タクシー", "電車"],
    ["チョコレート", "キャンディ"],
    ["砂浜", "山"],
    ["春巻き", "餃子"],
    ["テレビ", "ラジオ"],
    ["ケーキ", "クッキー"],
    ["トマト", "きゅうり"],
    ["橋", "トンネル"],
    ["机", "椅子"],
    ["パソコン", "スマホ"],
    ["山登り", "ハイキング"],
    ["ビール", "ワイン"],
    ["ネクタイ", "スカーフ"],
    ["かばん", "リュック"],
    ["青空", "夕焼け"],
    ["雨", "雪"],
    ["時計", "カレンダー"],
    ["飛行機", "船"],
    ["サングラス", "メガネ"],
    ["筆箱", "教科書"],
    ["犬の散歩", "猫の餌やり"],
    ["バナナ", "オレンジ"],
    ["ラーメン", "うどん"],
    ["自動販売機", "コンビニ"]
]

# 名前入力画面
@app.route("/")
def index():
    session.clear()
    return render_template("index.html")

# お題表示画面
@app.route("/topic")
def topic():
    return render_template("topic.html")

# ゲーム画面
@app.route("/game")
def game():
    index, topic_index = request.args.get("member_index"), int(request.args.get("topic_index"))
    session["index"], session["normal_topic"], session["wolf_topic"] = index, topics[topic_index][0], topics[topic_index][1]
    return render_template("game.html")

# 名前処理
@app.route("/member", methods=["POST"])
def member():
    members = request.form.getlist("name")
    session["members"] = members
    return render_template("topic.html", members=members)

# 投票画面
@app.route("/result")
def vote():
    index = int(session.get("index"))
    who_wolf = session.get("members")[index]
    normal, wolf = session.get("normal_topic"), session.get("wolf_topic")
    return render_template("result.html", who_wolf=who_wolf, normal=normal, wolf=wolf)

if __name__ == "__main__":
    app.run(debug=True)
