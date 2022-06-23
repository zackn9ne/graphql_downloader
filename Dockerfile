FROM python:3-slim AS builder

# We are installing a dependency here directly into our app source dir
#RUN pip install requests python-graphql-client python-dotenv

# A distroless container image with Python and some basics like SSL certificates
# https://github.com/GoogleContainerTools/distroless
FROM gcr.io/distroless/python3-debian10

COPY . /app
#ENTRYPOINT ["python", "/app/main.py"]
ENTRYPOINT ["sh", "/app/runner.sh"]
