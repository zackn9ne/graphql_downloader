from python_graphql_client import GraphqlClient
import os
import json
from dotenv import load_dotenv


def main():
    # set vars
    load_dotenv()  # take environment variables from .env.

    headers = { "Authorization": f"Token {os.environ.get('INPUTS_GH_TOKEN')}" }
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
        "owner": os.environ.get('INPUTS_OWNER'),
        "repo": os.environ.get('INPUTS_REPO')
    }
    # Synchronous request
    data = client.execute(query=query, variables=variables)
    with open(os.environ.get('INPUTS_OUTFILE'), "w", encoding="utf-8") as d:
        d.write(json.dumps(data.get("data")))
    print(f"::set-output name=myOutput::{data}")

if __name__ == "__main__":
    main()
