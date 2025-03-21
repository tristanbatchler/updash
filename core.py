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


def print_request(req: requests.PreparedRequest):
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))


def normalize_endpoint(endpoint: str) -> str:
    """
    Ensures the supplied endpoint is returned to be in the form
    BASE_URL/blah
    """
    if endpoint.startswith(BASE_URL):
        endpoint = endpoint.removeprefix(BASE_URL)
    if not endpoint.startswith("/"):
        endpoint = "/" + endpoint
    return BASE_URL + endpoint


def get(endpoint: str, params: dict[str, str] = {}) -> Response:
    response = requests.get(
        normalize_endpoint(endpoint),
        params=params,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    print_request(response.request)

    # Build the content by following pagination links
    content = response.content.decode('utf-8')
    try:
        content = json.loads(content)
        if (links := content.get('links')):
            if (next_link := links.get('next')):
                next_content = get(next_link).content
                content['links'] = next_content.get('links')
                content['data'] += next_content['data']

    except json.decoder.JSONDecodeError:
        content = {'data': content}

    return Response(
        response.status_code,
        content
    )


def patch(endpoint: str, data: dict[str, str]) -> Response:
    data = json.dumps(data).encode('utf-8')

    response = requests.patch(
        normalize_endpoint(endpoint),
        data=data,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
    )

    print_request(response.request)

    content = response.content.decode('utf-8')
    try:
        content = json.loads(content)
    except json.decoder.JSONDecodeError:
        content = {'data': content}

    return Response(
        response.status_code,
        content
    )
