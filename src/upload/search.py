import os
from flask import Blueprint, request
from src.upload.const import SEARCH_FOLDER, allowed_file

search_pb = Blueprint('search_pb', __name__)


@search_pb.route('/search', methods=['POST'])
def search_similar():
    # 创建上传目录（如果不存在的话）
    if not os.path.exists(SEARCH_FOLDER):
        os.makedirs(SEARCH_FOLDER)

    files = request.files.getlist('file')  # 使用JavaScript的数组形式获取多文件
    for file in files:
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(SEARCH_FOLDER, filename))
    return """File successfully uploaded.
    <br/>
    <a href="/">返回主页</a>"""
