import json
from ..constants import lc_queries


def get_lc_options(query_type, username, alt_options=None):
    options = {"username": username, **(alt_options or {})}

    return {
        "method": "GET",
        "url": "https://leetcode.com/graphql/",
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps({"query": lc_queries[query_type], "variables": options}),
    }
