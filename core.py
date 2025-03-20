import requests
import json
from typing import Any
from dataclasses import dataclass

BASE_URL = "https://api.up.com.au/api/v1"
access_token = ""


@dataclass
class Response:
    status_code: int
    content: dict[str, Any]


def get(endpoint: str, params: dict[str, str] = {}) -> Response:
    if not endpoint.startswith("/"):
        endpoint = "/" + endpoint

    req = requests.get(BASE_URL + endpoint, params=params, headers={
        "Authorization": f"Bearer {access_token}"
    })

    print(f"Making request: {req.url}")

    # Build the content by following pagination links
    content = req.content.decode('utf-8')
    try:
        content = json.loads(content)
        if (links := content.get('links')):
            if (next_link := links.get('next')):
                next_link = next_link.removeprefix(BASE_URL)
                next_content = get(next_link, access_token).content
                content['links'] = next_content.get('links')
                content['data'] += next_content['data']

    except json.decoder.JSONDecodeError:
        content = {'data': content}

    return Response(
        req.status_code,
        content
    )
