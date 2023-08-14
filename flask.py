from flask import Flask, request
import requests
import json
app = Flask(__name__)

client_id = "1122064123564408892"
client_secret = "TGdD1WQs0xnbG1OROCMkS_BRmLa7bv0K"
redirect_uri = "https://bot.yakeigai.com"
scopes = ["guilds.join","identify","guilds"]  # スコープ


@app.route("/bot.yakeigai.com")
def callback():


    # アクセストークンの取得
    token_endpoint = "https://discord.com/api/oauth2/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "scope": scopes,
        "code": request.args.get("code")
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(token_endpoint, data=data, headers=headers)
    if response.status_code == 200:
        # アクセストークンの取得に成功した場合
        access_token = response.json()["access_token"]
        with open("data/data.json", "r") as json_file:
            data = json.load(json_file)

        # 辞書にaccesstokenキーと値を追加
        data["accesstoken"] = access_token

        # 更新した辞書をJSONファイルに書き込み
        with open("data/data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        # 取得したアクセストークンを使用してDiscordのAPIを呼び出し、サーバーに参加させるリクエストを送信う
        print("Access token:", access_token)
    else:
        print("Error")
        return f"{response.text}"
    return f"Code: {access_token}, Token: {response.text}"
if __name__ == "__main__":
    app.run()
