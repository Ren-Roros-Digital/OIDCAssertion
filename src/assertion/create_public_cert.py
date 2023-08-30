"""Create a public certificate."""

from pathlib import Path
from subprocess import call

import click


@click.command()
@click.argument("domain")
@click.option("--authname", default="ca", show_default=True)
@click.option("--bits", default=2048, show_default=True)
@click.option("--cipher", default="sha256", show_default=True)
@click.option("--days", default=1095, show_default=True)
@click.option("--country")
@click.option("--organization")
@click.option("--commonname")
def create_public_certificate(
    domain: str,
    authname: str,
    bits: int,
    cipher: str,
    days: str,
    country: str,
    organization: str,
    commonname: str,
):
    certstore = Path(f"{domain}").stem
    Path(certstore).mkdir(parents=True, exist_ok=True)
    if not all([Path(f"{authname}/{authname}.crt").is_file() and Path(f"{authname}/{authname}.key").is_file()]):
        print(f"{authname}/{authname}.[ crt | key ] was not found. Create with poetry run create_ca")
        raise KeyboardInterrupt

    call(
        [
            "openssl",
            "genrsa",
            "-out",
            f"{certstore}/{domain}.key",
            f"{bits}",
        ]
    )

    call(
        [
            "openssl",
            "req",
            "-new",
            "-subj",
            f"/C={country}/O={organization}/CN={commonname}",
            "-key",
            f"{certstore}/{domain}.key",
            "-out",
            f"{certstore}/{domain}.csr",
        ]
    )

    call(
        [
            "openssl",
            "x509",
            "-req",
            "-in",
            f"{certstore}/{domain}.csr",
            "-CA",
            f"{authname}/{authname}.crt",
            "-CAkey",
            f"{authname}/{authname}.key",
            "-CAcreateserial",
            "-out",
            f"{certstore}/{domain}.crt",
            "-days",
            f"{days}",
            f"-{cipher}",
        ],
    )

    call(
        [
            "openssl",
            "pkcs12",
            "-export",
            "-inkey",
            f"{certstore}/{domain}.key",
            "-in",
            f"{certstore}/{domain}.crt",
            "-out",
            f"{certstore}/{domain}.pfx",
        ],
    )
    Path(f"{certstore}/{domain}.csr").unlink()
