# from keras.src.applications.resnet import ResNet50, ResNet101, ResNet152, preprocess_input
# # from tensorflow.keras.applications.resnet101 import ResNet101, preprocess_input
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.layers import GlobalAveragePooling2D
# from tensorflow.keras.models import Model
# import numpy as np
#
# print("==> loading resnet101 model...")
# # 加载预训练的ResNet50模型，去掉顶层的全连接层
# # base_model = ResNet101(weights='imagenet', include_top=False)
# resnet101_weights_file = 'mymodels/resnet101_weights_tf_dim_ordering_tf_kernels_notop.h5'
# resnet101_base_model = ResNet101(weights=None, include_top=False)  # 或者 include_top=False 如果不需要顶部的全连接层
# resnet101_base_model.load_weights(resnet101_weights_file)
#
# # 添加全局平均池化层来获取固定长度的向量
# resnet101_model = Model(
#     inputs=resnet101_base_model.input,
#     outputs=GlobalAveragePooling2D()(resnet101_base_model.output),
# )
# print("==> resnet101 model loaded")
#
#
# def extract_features_by_resnet101(file_path):
#     # 加载并预处理图像
#     img = image.load_img(file_path, target_size=(224, 224))
#     x = image.img_to_array(img)
#     x = np.expand_dims(x, axis=0)
#     x = preprocess_input(x)
#
#     # 使用模型预测
#     features = resnet101_model.predict(x)
#     # 特征向量形状将是 (None, 2048)，其中 None 表示 batch size
#     feature_vector = features[0]  # 取出第一个也是唯一一个元素
#
#     return feature_vector
