import os
from flask import Blueprint, request
from src.upload.const import SEARCH_FOLDER, allowed_file, to_slash, save_file, dashboard
from src.extract_search.extract_and_search import search_similar_images_by_path
from src.milvus.milvus import my_collection_name

search_pb = Blueprint('search_pb', __name__)


@search_pb.route('/search', methods=['POST'])
def search_similar():
    # 创建上传目录（如果不存在的话）
    if not os.path.exists(SEARCH_FOLDER):
        os.makedirs(SEARCH_FOLDER)

    # 上传
    file = request.files.get('file')
    if not file or not allowed_file(file.filename):
        return "请上传文件图片.<br/>" + dashboard
    filename = file.filename
    file_path = to_slash(os.path.join(SEARCH_FOLDER, filename))
    print(f"==> upload_file: ", file_path)
    save_file(file, file_path)

    # 查找相似的5个
    info_list = search_similar_images_by_path(file_path, collection_name=my_collection_name, top_k=5)
    img_list = [item.get("path", "") for item in info_list]

    # 上传图片
    upload_file_str = f'<img width="100" height="100" alt="{file_path}" src="{file_path}"/>'

    # 查找结果
    search_res_str = "找不到相似的图片"
    if len(img_list) > 0:
        # search_res_str = '<br/><hr/>'.join(img_list)
        search_res_str = ""
    for img_path in img_list:
        search_res_str += f'<img width="100" height="100" alt="{img_path}" src="{img_path}"/>&nbsp;&nbsp;&nbsp;'

    res = "File successfully uploaded.<br/>" + dashboard + "<br/><h2>上传结果：</h2><br/><hr/>" + upload_file_str + "<br/><hr/>"
    res += "<h2>匹配结果</h2>" + search_res_str
    return res
