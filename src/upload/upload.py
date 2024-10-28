import os
from flask import Blueprint, request
from src.upload.const import UPLOAD_FOLDER, allowed_file, to_slash, save_file, dashboard
from src.extract_search.extract_and_search import extract_features_and_upsert_collection
from src.milvus.milvus import my_collection_name

upload_pb = Blueprint('upload_pb', __name__)


@upload_pb.route('/upload', methods=['POST'])
def upload_files():
    # 创建上传目录（如果不存在的话）
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    files = request.files.getlist('files[]')  # 使用JavaScript的数组形式获取多文件
    img_list = []
    counter = 1

    # 上传
    for file in files:
        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = to_slash(os.path.join(UPLOAD_FOLDER, filename))
            print(f"==> upload_files[{counter}]: ", file_path)
            counter += 1
            save_file(file, file_path)
            img_list.append(file_path)

    # 上传图片列表
    upload_file_str = "--> 本次上传文件列表为空。"
    if len(img_list) > 0:
        upload_file_str = '<br/><hr/>'.join(img_list)
        upload_file_str = ''
    for img_path in img_list:
        upload_file_str += f'<img width="100" height="100" alt="{img_path}" src="{img_path}"/>&nbsp;&nbsp;&nbsp;'

    # 提前特征和更新Milvus
    extract_features_and_upsert_collection(img_list=img_list, collection_name=my_collection_name)
    return """Files successfully uploaded.<br/>""" + dashboard + "<br/><h2>上传结果：</h2><br/><hr/>" + upload_file_str
