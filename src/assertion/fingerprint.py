"""Get fingerprint of signing authority."""

import base64
import subprocess
from pathlib import Path
from typing import cast

import click
from hexdump import restore


def calc_fingerprint(fingerprint: Path) -> str:
    _fingerprint = subprocess.run(
        [
            "openssl",
            "x509",
            "-in",
            f"{fingerprint}",
            "-fingerprint",
            "-noout",
        ],
        capture_output=True,
    )
    _hexfinger = _fingerprint.stdout.decode().split("=")[1].replace(":", "")
    return _hexfinger


def get_fingerprint(fingerprint: Path) -> str:
    _hexfinger = calc_fingerprint(fingerprint)
    return base64.b64encode(cast(bytes, restore(_hexfinger))).decode()


@click.command()
@click.option("--cert", default="ca/ca.crt", show_default=True)
def print_fingerprint(cert: str) -> None:
    """Print the fingerprint of the given <path/to/certificate.crt> ."""
    _hexfinger = calc_fingerprint(Path(cert))
    print(base64.b64encode(cast(bytes, restore(_hexfinger))).decode())
