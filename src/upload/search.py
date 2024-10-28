import os
from flask import Blueprint, request
from src.upload.const import SEARCH_FOLDER, allowed_file, save_file, dashboard

search_pb = Blueprint('search_pb', __name__)


@search_pb.route('/search', methods=['POST'])
def search_similar():
    # 创建上传目录（如果不存在的话）
    if not os.path.exists(SEARCH_FOLDER):
        os.makedirs(SEARCH_FOLDER)

    file = request.files.get('file')
    if not file or not allowed_file(file.filename):
        return "请上传文件图片.<br/>" + dashboard
    filename = file.filename
    file_path = os.path.join(SEARCH_FOLDER, filename)
    print(f"==> upload_file: ", file_path)
    save_file(file, file_path)
    return """File successfully uploaded.<br/>""" + dashboard
