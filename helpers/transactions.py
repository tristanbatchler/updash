from datetime import datetime
from zoneinfo import ZoneInfo
from updash.core import Response, get
from updash.helpers.categories import Category


def list_transactions(
        since: datetime | None = None,
        until: datetime | None = None,
        category: Category | None = None,
        tag_label: str | None = None) -> Response:

    params = {}

    # If timezone unaware, assume UTC+10:00
    brisbane_offset = ZoneInfo('Australia/Brisbane')
    if since and not since.tzinfo:
        since = since.replace(tzinfo=brisbane_offset)
        params["filter[since]"] = since.isoformat()
    if until and not until.tzinfo:
        until = until.replace(tzinfo=brisbane_offset)
        params["filter[until]"] = until.isoformat()

    if category:
        params[f"filter[{category.SELF}"] = category

    if tag_label:
        params["filter[tag]"] = tag_label

    return get("transactions", params)
