FROM python:3

ADD main.py /

RUN pip install requests python_graphql_client python-dotenv

CMD [ "python", "./main.py" ]
