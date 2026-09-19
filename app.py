from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

# 把引号里的内容换成你自己的 API Key
API_KEY = "566c3c5d9c054118aecef21c4861978b.paa6CDYD5KqzLeRU"

API_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

SYSTEM_PROMPT = """你是一个鸿蒙技术知识助手，专门回答关于开源鸿蒙（OpenHarmony）和 HarmonyOS 的技术问题。
你的回答要准确、通俗易懂，适合初学者理解。
如果用户问的不是鸿蒙相关问题，你也可以正常回答，但可以适当引导到鸿蒙方向。
回答时尽量简洁，不要太长。"""

chat_history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    chat_history.append({"role": "user", "content": user_message})
    
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + chat_history
    
    headers = {
        "Authorization": "Bearer " + API_KEY,
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "glm-4-flash",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 500
    }
    
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    result = response.json()
    
    ai_reply = result["choices"][0]["message"]["content"]
    chat_history.append({"role": "assistant", "content": ai_reply})
    
    return jsonify({"reply": ai_reply})

@app.route('/clear', methods=['POST'])
def clear():
    global chat_history
    chat_history = []
    return jsonify({"status": "cleared"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
