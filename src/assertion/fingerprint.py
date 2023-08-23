"""Get fingerprint of signing authority."""

import base64
import subprocess
from typing import cast

import click
from hexdump import restore


def calc_fingerprint(authname: str) -> str:
    fingerprint = subprocess.run(
        [
            "openssl",
            "x509",
            "-in",
            f"{authname}/{authname}.crt",
            "-fingerprint",
            "-noout",
        ],
        capture_output=True,
    )
    _hexfinger = fingerprint.stdout.decode().split("=")[1].replace(":", "")
    return _hexfinger


def get_fingerprint(authname: str) -> str:
    _hexfinger = calc_fingerprint(authname)
    return base64.b64encode(cast(bytes, restore(_hexfinger))).decode()


@click.command()
@click.option("--authname", default="ca", show_default=True)
def print_fingerprint(authname: str) -> None:
    _hexfinger = calc_fingerprint(authname)
    print(base64.b64encode(cast(bytes, restore(_hexfinger))).decode())
