FROM python:3.9.2-slim-buster

RUN pip install fastapi uvicorn
RUN /usr/local/bin/python -m pip install --upgrade pip
EXPOSE 8080

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

### run as root
# USER root
# RUN echo '$*' > /bin/sudo
# RUN chmod 555 /bin/sudo

# COPY ./app /app
# RUN pip install --upgrade pip
# RUN pip install fastapi uvicorn
# EXPOSE 8080
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

# WORKDIR /app
# RUN apt update && apt update
# RUN apt install -y python3-pip && pip3 install .
# RUN pip install -r requirements.txt
# CMD ["uvicorn", "main:app --reload"]

# docker build -t myimage.
# docker run -d --name mycontainer -p 8080:80 myimage