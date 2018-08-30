import os
import json
from flask import Flask, request, jsonify
import random
 


app = Flask(__name__)

@app.route('/')
def hello():
    return '    챗봇페이지 입니다!!!!'
    
@app.route('/keyboard')
def keyboard():

    #keyboard 딕셔너리 생성
    keyboard = {
      "type" : "buttons",
      "buttons" : ["메뉴", "로또", "고양이", "영화","진주"]
    }
    
    #딕셔너리를 json으로 바꿔서 리턴해주기 위한 코드
    json_keyboard = json.dumps(keyboard)
    return json_keyboard
    
@app.route('/message', methods=['POST'])
def message():
    
    #content라는 ket의 value를 msg의 저장
    msg = request.json['content']

    
    if msg == "메뉴" :
        menu = ["A코스", "B코스"]
        return_msg = random.choice(menu)
    elif msg == "로또" :
        # 1~ 45 리스트
        numbers = list(range(1,46))
        #6개 샘플링
        pick = random.sample(numbers,6)
        # 정렬 후 스트링으로 변환하여 출력
        return_msg = str(sorted(pick))
    
    else:
        return_msg = "현재메뉴만 지원합니다."
        
    

        
    
    json_return = {
        "message" : {
            "text" : return_msg
        },
        "keyboard" : {
            "type" : "buttons",
            "buttons" : ["메뉴", "로또", "고양이", "영화","뿡뿡"]
        }
    }
    
    return jsonify(json_return)
    
    

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))