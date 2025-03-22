from updash.core import get, post, delete, Response


def list_tags() -> Response:
    return get("tags")


def add_tags_to_transaction(transaction_id: str,
                            labels: list[str]) -> Response:
    return post(f"transactions/{transaction_id}/relationships/tags", {
        'data': [
            {'type': 'tags', 'id': label}
            for label in labels
        ]
    })


def remove_tags_from_transaction(transaction_id: str,
                                 labels: list[str]) -> Response:
    return delete(f"transactions/{transaction_id}/relationships/tags", {
        'data': [
            {'type': 'tags', 'id': label}
            for label in labels
        ]
    })
