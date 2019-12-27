FROM python:3.7
ADD . /usr/app
WORKDIR /usr/app
RUN pip install -r requirements.txt

RUN ["chmod", "u+r+x", "./wait-for-it.sh"]

CMD ["./wait-for-it.sh", "db:5432", "--", "flask", "run", "--host=0.0.0.0"]