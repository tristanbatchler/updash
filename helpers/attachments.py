from updash.core import Response, get


def list_attachments() -> Response:
    return get("attachments")


def get_attachment(_id: str) -> Response:
    return get(f"attachments/{_id}")
