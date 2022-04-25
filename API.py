####提供使用者API,輸入http://127.0.0.1:10000/<集團名稱>/<品牌名稱>,就可以查詢到餐廳的資料####

# !pip install flask
# !pip install flask-restful
# !pip install pymongo

import pymongo
import flask
from flask_restful import Api  
from flask_restful import Resource

### 設置API可使用的功能
class GetInfo(Resource):
    def get(self,company,restaurant):
        myclient = pymongo.MongoClient("mongodb://admin:test1234@34.125.239.225:27017/")
        db = myclient["foodpage"]
        col = db["ifoodie"]
        cursor = col.find({'集團': company ,'品牌': restaurant })

        list =[]
        for x in cursor:
            list.append(x)
        return list

### 建立FLASK架構
app = flask.Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)
api.add_resource(GetInfo, "/<company>/<restaurant>") 
app.config.update ( RESTFUL_JSON = dict ( ensure_ascii = False ))  # 解決傳輸到網頁上中文呈現亂碼的問題

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

