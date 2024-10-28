from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalAveragePooling2D
from tensorflow.keras.models import Model
import numpy as np

# 加载预训练的Inception V3模型，去掉顶层的全连接层
# base_model = InceptionV3(weights='imagenet', include_top=False)
inception_v3_weights_file = 'mymodels/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5'
inception_v3_base_model = InceptionV3(weights=None, include_top=False)  # 或者 include_top=False 如果不需要顶部的全连接层
inception_v3_base_model.load_weights(inception_v3_weights_file)
# 添加全局平均池化层来获取固定长度的向量
inception_v3_model = Model(
    inputs=inception_v3_base_model.input,
    outputs=GlobalAveragePooling2D()(inception_v3_base_model.output),
)


def extract_features_by_inception_v3(file_path):
    # 加载并预处理图像
    img = image.load_img(file_path, target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # 使用模型预测
    features = inception_v3_model.predict(x)
    # 特征向量形状将是 (None, 2048)，其中 None 表示 batch size
    feature_vector = features[0]  # 取出第一个也是唯一一个元素

    return feature_vector
