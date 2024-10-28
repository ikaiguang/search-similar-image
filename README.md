# milvus

```shell

# 下载脚本
curl -o install_milvus/standalone_embed.sh https://raw.githubusercontent.com/milvus-io/milvus/master/scripts/standalone_embed.sh 

## 运行 milvus
# ./install_milvus/standalone_embed.sh start
docker pull milvusdb/milvus:v2.4.13-hotfix
docker-compose -f install_milvus/docker-compose.yaml up -d

## 开发安装环境
# pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
pip install pymilvus==2.4.8 -i https://mirrors.aliyun.com/pypi/simple
pip install tensorflow-cpu==2.17.0 -i https://mirrors.aliyun.com/pypi/simple
pip install pillow==11.0.0 -i https://mirrors.aliyun.com/pypi/simple
pip install flask==3.0.3 -i https://mirrors.aliyun.com/pypi/simple
```