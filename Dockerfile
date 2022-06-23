FROM python:3

RUN pip install requests python_graphql_client python-dotenv

COPY main.py /main.py

ENTRYPOINT ["/main.py"]
