"""Get final authentication token."""

import json
from pathlib import Path

import click
import requests

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


@click.command()
@click.option("--cert", default=None, show_default=True)
@click.option("--client-id", default=None, show_default=True)
@click.option("--statuscode/--no-statuscode", default=True, show_default=True)
@click.option("--print-header", is_flag=True, show_default=True)
@click.option("--print-payload", is_flag=True, show_default=True)
@click.option("--print-token-string", is_flag=True, show_default=True)
def print_token(
    cert: Path | None = None,
    client_id: str | None = None,
    statuscode: bool = True,
    print_header: bool = False,
    print_payload: bool = False,
    print_token_string: bool = False,
):
    """Print the response from a token request given fingerprint, assertion and scope.

    This method uses the .env file.
    """

    if cert is not None:
        SETTINGS.OIDC.fingerprint = cert

    if client_id is not None:
        SETTINGS.OIDC.client_id = client_id

    if print_header or print_payload:
        _payload, _header = build_headers_and_payload(SETTINGS)
        if print_header:
            print(f"{_header!r}")
        if print_payload:
            print(f"{_payload!r}")

    res = get_token(SETTINGS)
    if statuscode:
        if print_token_string:
            print(f"{json.loads(res.content)['access_token']}")
        else:
            print(f"{res.status_code} - {res.content!r}")
