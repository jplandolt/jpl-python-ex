# docker build command is very vanilla:
# 	docker build --no-cache=true -t APPNAME[-ENV] .

FROM centos/python-36-centos7

WORKDIR .
ENV TERM linux
ENV DEBIAN_FRONTEND noninteractive

# Stage the app code
COPY simple.py .

# exec command for the image when it cranks up
CMD ["python3", "simple.py"]

