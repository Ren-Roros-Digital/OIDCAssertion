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
@click.option("--country", default="NO", show_default=True)
@click.option("--organization", default="Ren Røros Digital AS", show_default=True)
def create_public_certificate(
    domain: str,
    authname: str,
    bits: int,
    cipher: str,
    days: str,
    country: str,
    organization: str,
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
            f"/C={country}/O={organization}/CN={domain}",
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
    Path(f"{certstore}/{domain}.csr").unlink()
