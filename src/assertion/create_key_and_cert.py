
"""Create a public certificate."""

from pathlib import Path
from subprocess import call

import click


@click.command()
@click.argument("domain")
@click.option("--bits", default=2048, show_default=True)
@click.option("--days", default=1095, show_default=True)
def create_public_certificate(
    domain: str,
    bits: int,
    days: str,
):
    certstore = Path(f"{domain}").stem
    Path(certstore).mkdir(parents=True, exist_ok=True)

    call(
        [
            "openssl",
            "req",
            "-newkey",
            f"rsa:{bits}",
            "-nodes",
            "-keyout",
            f"{certstore}/{domain}.key.pem",
            "-x509",
            "-days",
            f"{days}",
            "-out",
            f"{certstore}/{domain}.cert.pem",
        ]
    )
    call(
        [
            "openssl",
            "pkcs12",
            "-export",
            "-inkey",
            f"{certstore}/{domain}.key.pem",
            "-in",
            f"{certstore}/{domain}.cert.pem",
            "-out",
            f"{certstore}/{domain}.pfx",
        ],
    )
