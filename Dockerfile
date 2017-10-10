FROM alpine:latest

MAINTAINER xujpxm

ENV ENV_CONFIG production
#创建代码目录
RUN mkdir -p /data/vsphere_ds_exporter\
    && apk update \
    && apk add --no-cache nginx py-pip tzdata py-gevent supervisor py-gunicorn\
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo 'Asia/Shanghai' > /etc/timezone \ 
    && apk del tzdata \
    && mkdir /run/nginx/ \
    && mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.bak 

#上传代码和nginx+supervisor服务的配置文件
ADD . /data/vsphere_ds_exporter/
ADD conf.d/nginx_example.conf /etc/nginx/conf.d/
ADD conf.d/supervisor_example.ini /etc/supervisor.d/

EXPOSE 80

WORKDIR /data/vsphere_ds_exporter/

#安装代码运行依赖包
RUN  pip install --no-cache-dir -r requirements.txt


# 启动supervisor，配置文件里包含nginx和gunicorn,相当于同时启动两个服务
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]