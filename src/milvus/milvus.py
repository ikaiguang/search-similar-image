from pymilvus import FieldSchema, CollectionSchema, DataType, MilvusClient
from pymilvus.exceptions import MilvusException, DescribeCollectionException

my_db_name = "my_database"
my_collection_name = "my_collection_for_inception_v3"
my_milvus_client = MilvusClient(
    uri="http://localhost:19530",
    db_name="default"
)


def create_milvus_database(db_name="my_database"):
    try:
        my_milvus_client.create_database(db_name)
    except MilvusException as e:
        # code=65535, message=database already exist: my_database
        print(f'code: {e.code}, e.compatible_code: {e.compatible_code}, message: {e.message}')
    db_list = my_milvus_client.list_databases()
    print(f"==> db_list: {db_list}")
    my_milvus_client.using_database(db_name)


def create_milvus_collection(collection_name="my_collection", dimension=2048):
    vector_index_name = "vector_index"
    try:
        describe_res = my_milvus_client.describe_collection(collection_name=collection_name)
        print(f'==> collection_name: {collection_name}, describe_collection: {describe_res}')
        index_res = my_milvus_client.list_indexes(collection_name=collection_name)
        print(f'==> collection_name: {collection_name}, list_indexes: {index_res}')
        index_res = my_milvus_client.describe_index(collection_name=collection_name, index_name=vector_index_name)
        print(f'==> collection_name: {collection_name}, describe_index: {index_res}')
        my_milvus_client.load_collection(collection_name=collection_name)
        # my_milvus_client.drop_collection(collection_name=collection_name)
    except DescribeCollectionException as e:
        # code=100, message=can't find collection[database=my_database][collection=my_collection]
        print(f'DescribeCollectionException e.code: {e.code}, '
              f'e.compatible_code: {e.compatible_code}, '
              f'e.message: {e.message}')
        # 定义集合模式
        # field_id = FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True, description="id")
        field_path = FieldSchema(name="path", dtype=DataType.VARCHAR, is_primary=True,
                                 max_length=1024, default_value="", description="img path")
        field_vector = FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=dimension, description="img vector")
        # schema = CollectionSchema(fields=[field_id, field_path, field_vector], description="Image vectors")
        schema = CollectionSchema(fields=[field_path, field_vector], description="Image vectors")

        my_milvus_client.create_collection(collection_name=collection_name, schema=schema)
        index_params = my_milvus_client.prepare_index_params(
            field_name="vector",
            metric_type="L2",
            index_type="IVF_FLAT",
            index_name=vector_index_name,
            params={"nlist": 128},
        )
        my_milvus_client.create_index(collection_name=collection_name, index_params=index_params)
        my_milvus_client.load_collection(collection_name=collection_name)
        state_res = my_milvus_client.get_load_state(
            collection_name=collection_name
        )
        print(f"==> collection_name: {collection_name}, get_load_state: {state_res}")
        describe_res = my_milvus_client.describe_collection(collection_name=collection_name)
        print(f'==> collection_name: {collection_name}, describe_collection: {describe_res}')
        index_res = my_milvus_client.list_indexes(collection_name=collection_name)
        print(f'==> collection_name: {collection_name}, list_indexes: {index_res}')
        index_res = my_milvus_client.describe_index(collection_name=collection_name, index_name=vector_index_name)
        print(f'==> collection_name: {collection_name}, describe_index: {index_res}')


def insert_into_collection(vector, collection_name="my_collection", path=""):
    data = [
        {"path": path, "vector": vector}
    ]
    my_milvus_client.upsert(collection_name=collection_name, data=data)


def search_similar_images(query_vector, collection_name="my_collection", top_k=5):
    query_data = [query_vector]
    results = my_milvus_client.search(
        collection_name=collection_name, anns_field="vector", limit=top_k,
        data=query_data, search_params={"metric_type": "L2", "params": {"nprobe": 16}},
    )
    # result_json = json.dumps(results, indent=4)
    # print(f"==> Similar resultJson: {result_json}")
    i = 0
    for result in results[0]:
        i += 1
        print(f"==> Similar result[{i}]: {result} \n\t id: {result.get('id')}, distance: {result.get('distance')}")
        # print(f"Similar image with score {result.distance}: {result.get('id')}")


create_milvus_database(db_name=my_db_name)
create_milvus_collection(collection_name=my_collection_name)
