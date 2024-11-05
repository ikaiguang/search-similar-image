ARG WORK_DIR=/myworkspace

FROM python:3.10.15

ARG WORK_DIR

WORKDIR ${WORK_DIR}

COPY . .
RUN rm -rf ./venv ./.idea ./.git ./mytest

# RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
RUN pip install pymilvus==2.4.8 -i https://mirrors.aliyun.com/pypi/simple
RUN pip install tensorflow-cpu==2.17.0 -i https://mirrors.aliyun.com/pypi/simple
RUN pip install pillow==11.0.0 -i https://mirrors.aliyun.com/pypi/simple
RUN pip install flask==3.0.3 -i https://mirrors.aliyun.com/pypi/simple

EXPOSE 8081

ENTRYPOINT ["python", "src/main.py"]

