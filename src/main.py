import os
import sys

cur_path = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, cur_path + "/..")

from flask import Flask
from src.web.web import web_pb
from src.upload.upload import upload_pb
from src.upload.search import search_pb

app = Flask("myapp")
blueprints = [web_pb, upload_pb, search_pb]
# 注册蓝图
for bp in blueprints:
    app.register_blueprint(bp)


def debug_info():
    pwd = os.getcwd()
    print("==> pwd: ", pwd)
    print("==> app.name: ", app.name)


# curl -X GET http://127.0.0.1:8081/say_hello
@app.route('/say_hello')
def say_hello():
    return "hello world"


def run_app():
    app.run(debug=True, host='0.0.0.0', port=8081)


# python .\src\main.py
# linux : gunicorn -w 4 'src.main:app'
# windows : waitress-serve --host 0.0.0.0 --port 8081 src.main:app
if __name__ == "__main__":
    debug_info()

    run_app()
