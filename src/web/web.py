from flask import Blueprint, request, render_template

# app = Flask(__name__)
web_pb = Blueprint('web_pb', __name__)


@web_pb.route('/')
def upload_form():
    # 默认加载 主目录为 templates
    return render_template('upload.html')
