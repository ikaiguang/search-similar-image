# 设置上传文件保存目录
UPLOAD_FOLDER = 'mytest/uploads'
SEARCH_FOLDER = 'mytest/search'
# 允许上传的文件类型
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
