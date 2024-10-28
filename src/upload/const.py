import os

# 设置上传文件保存目录
UPLOAD_FOLDER = 'mytest/images'
SEARCH_FOLDER = 'mytest/search'
# 允许上传的文件类型
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
# 首页
dashboard = '<a href="/"><h2>返回主页</h2></a>'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_file(file, file_path):
    # 如果文件已存在，则删除旧文件
    if os.path.exists(file_path):
        os.remove(file_path)
    file.save(file_path)
