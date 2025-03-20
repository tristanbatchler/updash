from updash.core import get, Response
from enum import StrEnum


class AccountType(StrEnum):
    SELF = "accountType",
    SAVER = "SAVER",
    TRANSACTIONAL = "TRANSACTIONAL",
    HOME_LOAN = "HOME_LOAN",


class OwnershipType(StrEnum):
    SELF = "ownershipType",
    INDIVIDUAL = "INDIVIDUAL",
    JOINT = "JOINT",


def list_accounts(
        account_type: AccountType | None = None,
        ownership_type: OwnershipType | None = None) -> Response:
    params = {}
    if account_type:
        params[f"filter[{AccountType.SELF}]"] = account_type
    if ownership_type:
        params[f"filter[{OwnershipType.SELF}]"] = ownership_type
    return get("accounts", params)
