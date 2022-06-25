from python_graphql_client import GraphqlClient
import os
import json
import base64
from dotenv import load_dotenv


def main():
    # set vars
    load_dotenv()  # take environment variables from .env.
    import base64
    coded_string = os.environ.get('INPUT_GH_TOKEN')
    decoded = base64.b64decode(coded_string)
    headers = { "Authorization": f"Token {decoded}" }
    client = GraphqlClient(endpoint="https://api.github.com/graphql", headers=headers)

    query = """
        query dependaBotAlerts($owner: String!, $repo: String!) {
            repository(owner: $owner, name: $repo) {
            vulnerabilityAlerts(first: 100) {
                nodes {
                createdAt
                dismissedAt
                securityVulnerability {
                    package {
                    name
                    ecosystem
                    }
                    advisory {
                    severity
                    summary
                    description
                    notificationsPermalink
                    ghsaId
                    }
                    vulnerableVersionRange
                }
                }
            }
            }
        }
    """
    variables = {
        "owner": os.environ.get('INPUT_OWNER'),
        "repo": os.environ.get('INPUT_REPO')
    }
    print(f"{variables.get('owner')} and {variables.get('repo')}")
    # Synchronous request
    data = client.execute(query=query, variables=variables)
    with open(os.environ.get('INPUT_OUTFILE'), "w", encoding="utf-8") as d:
        d.write(json.dumps(data.get("data")))
    print(f"::set-output name=myOutput::{data}")

if __name__ == "__main__":
    main()
