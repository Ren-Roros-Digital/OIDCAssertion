"""Decode a x509 certificate."""


from pathlib import Path
from subprocess import call

import click


@click.command()
@click.option("--cert", default="ca/ca.crt", show_default=True)
def decode(cert: Path):
    call(
        [
            "openssl",
            "x509",
            "-text",
            "-in",
            f"{cert}",
        ]
    )
