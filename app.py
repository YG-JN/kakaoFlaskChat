import os
import json
from flask import Flask, request, jsonify
import requests
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
      "buttons" : ["메뉴", "로또", "강아지", "영화","진주"]
    }
    
    #딕셔너리를 json으로 바꿔서 리턴해주기 위한 코드
    json_keyboard = json.dumps(keyboard)
    return json_keyboard
    
@app.route('/message', methods=['POST'])
def message():
    
    #content라는 ket의 value를 msg의 저장
    msg = request.json['content']

    img_bool = False
    if msg == "메뉴" :
        menu = ["진꼬", "진뿡"]
        return_msg = random.choice(menu)
    elif msg == "로또" :
        # 1~ 45 리스트
        numbers = list(range(1,46))
        #6개 샘플링
        pick = random.sample(numbers,6)
        # 정렬 후 스트링으로 변환하여 출력
        return_msg = str(sorted(pick)) + "만큼 진꼬 당첨!"
    elif msg =="강아지":
        img_bool = True
        url = "https://api.thedogapi.com/v1/images/search?mime_types=jpg"
        req = requests.get(url).json()
        dog_url=req[0]['url']
        
    else:
        return_msg = "현재메뉴만 지원합니다."
        
    

        
    if img_bool == True:
        json_return = {
            "message" : {
                "text" : "나만 강아지 없어 :(",
                "photo" : {
                    "url" : dog_url,
                    "width" :720,
                    "height" : 640
                }
            },
            "keyboard" : {
                "type" : "buttons",
                "buttons" : ["메뉴", "로또", "강아지", "영화","뿡뿡"]
            }
        }
    else:
        json_return = {
            "message" : {
                "text" : return_msg
            },
            "keyboard" : {
                "type" : "buttons",
                "buttons" : ["메뉴", "로또", "강아지", "영화","뿡뿡"]
            }
        }
        
    return jsonify(json_return)
    
    

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))