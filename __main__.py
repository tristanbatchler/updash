import pprint
import os
import argparse
import dotenv
import updash.core as core
from updash.helpers import accounts


def print_response(res: core.Response):
    pretty_printer = pprint.PrettyPrinter(depth=10)
    if not (200 <= res.status_code < 300):
        print(f"Error code {res.status_code}")

    pretty_printer.pprint(res.content)


def set_access_token():
    dotenv.load_dotenv()
    core.access_token = os.environ.get("UPDASH_ACCESS_TOKEN")


def main() -> int:
    set_access_token()
    if not core.access_token:
        print("UPDASH_ACCESS_TOKEN environment variable not set")
        return 1

    argparser = argparse.ArgumentParser(
        prog="Updash",
        description="A programmatic way to obtain banking information\n"
                    'Example: ./updash.py -e accounts -p "page[size]=1" '
                    '"something[else]=2"',
        epilog="A big shoutout to my cats Ferris and Goldie",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    argparser.add_argument('-i', "--interactive", action='store_true')
    argparser.add_argument('-e', "--endpoint")
    argparser.add_argument('-p', "--param", nargs='*')

    args = argparser.parse_args()

    params = {}
    if args.param:
        for p in args.param:
            key, value = p.split("=")
            params[key] = value

    if not (args.interactive or args.endpoint):
        print("Must supply either interactive or endpoint argument")
        argparser.print_help()
        return 1

    while args.interactive:
        endpoint = input("Enter an endpoint or type quit: ")
        if endpoint.strip() in ("", "quit"):
            return 0

        print_response(core.get(endpoint, params))

    print_response(core.get(args.endpoint, params))
    return 0


def main_test() -> int:
    set_access_token()
    print_response(accounts.list_accounts(
        ownership_type=accounts.OwnershipType.INDIVIDUAL))
    return 0


if __name__ == '__main__':
    try:
        exit(main())
    except KeyboardInterrupt:
        exit(130)
