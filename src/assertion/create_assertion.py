"""Create the final assertion."""
import uuid
from datetime import datetime, timedelta

import click
from authlib.jose import jwt

from assertion.fingerprint import get_fingerprint
from assertion.settings import SETTINGS, SettingsProtocol


def get_authlib_payload(settings: SettingsProtocol) -> jwt:
    header = {"alg": "RS256", "x5t": get_fingerprint(settings.OIDC.fingerprint)}
    _timestamp = datetime.now()
    payload = {
        "sub": f"{settings.OIDC.client_id}",
        "jti": uuid.uuid1().hex,
        "aud": f"{settings.OIDC.token_url}",
        "iss": f"{settings.OIDC.client_id}",
        "exp": int((_timestamp + timedelta(hours=1)).timestamp()),
        "iat": int(_timestamp.timestamp()),
        "nbf": int(_timestamp.timestamp()),
    }
    with open(settings.OIDC.public_key, "r") as fp:
        _secret = fp.read()
        res = jwt.encode(header, payload, _secret)
    return res


@click.command()
def print_authlib_payload():
    print(get_authlib_payload(SETTINGS).decode())
