"""Get final authentication token."""

import json
from pathlib import Path
from typing import TypedDict

import click
import requests
from beartype.typing import Unpack

from assertion.create_assertion import get_authlib_payload
from assertion.settings import SETTINGS, SettingsProtocol


def build_headers_and_payload(settings: SettingsProtocol) -> tuple[str, dict[str, str]]:
    assertion = get_authlib_payload(settings).decode()
    payload = "".join(
        [
            f"client_id={settings.OIDC.client_id}&grant_type={settings.OIDC.grant_type}",
            f"&assertion={assertion}&scope={settings.OIDC.scope}",
        ]
    )
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    return (payload, headers)


def get_token(settings: SettingsProtocol) -> requests.Response:
    payload, headers = build_headers_and_payload(settings)
    response = requests.post(settings.OIDC.token_url, headers=headers, data=payload)
    return response


class TokenKwargs(TypedDict):
    cert: Path
    client_id: str
    statuscode: bool
    print_header: bool
    print_payload: bool
    print_token_string: bool


@click.command()
@click.option("--cert", default=None, show_default=True)
@click.option("--client-id", default=None, show_default=True)
@click.option("--statuscode/--no-statuscode", default=True, show_default=True)
@click.option("--print-header", is_flag=True, show_default=True)
@click.option("--print-payload", is_flag=True, show_default=True)
@click.option("--print-token-string", is_flag=True, show_default=True)
def print_token(
    **kwargs: Unpack[TokenKwargs],
):
    """Print the response from a token request.

    The default behaviour is that the command reads the .env file.
    Setting the options will override options from .env file.
    """

    if kwargs["cert"] is not None:
        SETTINGS.OIDC.fingerprint = kwargs["cert"]

    if kwargs["client_id"] is not None:
        SETTINGS.OIDC.client_id = kwargs["client_id"]

    if kwargs["print_header"] or kwargs["print_payload"]:
        _payload, _header = build_headers_and_payload(SETTINGS)
        if kwargs["print_header"]:
            print(f"{_header!r}")
        if kwargs["print_payload"]:
            print(f"{_payload!r}")

    res = get_token(SETTINGS)
    if kwargs["statuscode"]:
        if kwargs["print_token_string"]:
            print(f"{json.loads(res.content)['access_token']}")
        else:
            print(f"{res.status_code} - {res.content!r}")


if __name__ == "__main__":
    print_token()
