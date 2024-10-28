from src.image_features.inception_v3 import extract_features
from src.milvus.milvus import insert_into_collection, search_similar_images
import numpy as np
import os


def extract_features_and_upsert_collection(img_list: list, collection_name="my_collection"):
    folder = "mytest/inception"
    if not os.path.exists(folder):
        os.makedirs(folder)
    for img_path in img_list:
        out_path = folder + "/inception_" + os.path.basename(img_path) + ".npy"
        print(f'==> extract and upsert; img_path: {img_path}, out_path: {out_path}')
        feature_vector = extract_features(img_path)
        np.save(out_path, feature_vector)
        insert_into_collection(feature_vector, collection_name=collection_name, path=img_path)


def search_similar_images_by_path(query_path, collection_name="my_collection", top_k=5):
    print("\n\n\n")
    print(f'==> search_image_path: {query_path}')
    feature_vector = extract_features(query_path)
    search_similar_images(feature_vector, collection_name=collection_name, top_k=top_k)
