import os
from flask import Blueprint, request
from src.upload.const import UPLOAD_FOLDER, allowed_file, save_file, dashboard

upload_pb = Blueprint('upload_pb', __name__)


@upload_pb.route('/upload', methods=['POST'])
def upload_files():
    # 创建上传目录（如果不存在的话）
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    files = request.files.getlist('files[]')  # 使用JavaScript的数组形式获取多文件
    counter = 1
    for file in files:
        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            print(f"==> upload_files[{counter}]: ", file_path)
            counter += 1
            save_file(file, file_path)
    return """Files successfully uploaded.<br/>""" + dashboard
