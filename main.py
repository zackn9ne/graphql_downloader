from python_graphql_client import GraphqlClient
import os
import json
from dotenv import load_dotenv


def main():
    # set vars
    load_dotenv()  # take environment variables from .env in case debugging
    coded_string = os.environ.get('INPUT_GH_TOKEN')
    query = os.environ.get('INPUT_QUERY')

    decoded = f"Bearer {str(coded_string)}"
    headers = { "Authorization": decoded }
    client = GraphqlClient(endpoint="https://api.github.com/graphql", headers=headers)

    variables = {
        "owner": os.environ.get('INPUT_OWNER'),
        "repo": os.environ.get('INPUT_REPO')
    }
    print(f"{variables.get('owner')} and {variables.get('repo')}")
    # Synchronous request
    data = client.execute(query=query, variables=variables)
    print(data)
    with open(os.environ.get('INPUT_OUTFILE'), "w", encoding="utf-8") as d:
        d.write(json.dumps(data.get("data")))
    print(f"::set-output name=myOutput::{data}")

if __name__ == "__main__":
    main()
