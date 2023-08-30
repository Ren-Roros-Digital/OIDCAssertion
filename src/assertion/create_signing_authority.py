"""An attempt at creating an azure assertion."""


from pathlib import Path
from subprocess import call

import click


@click.command()
@click.option("--authname", default="ca", show_default=True)
@click.option("--force", is_flag=True, default=False, show_default=True)
@click.option("--bits", default=2048, show_default=True)
@click.option("--cipher", default="sha256", show_default=True)
@click.option("--days", default="1095", show_default=True)
@click.option("--country")
@click.option("--organization")
@click.option("--commonname")
def create_signing_authority(
    authname: str,
    force: bool,
    bits: int,
    cipher: str,
    days: int,
    country: str,
    organization: str,
    commonname: str,
):
    """Create signing auth.

    Cowardly refuse to overwrite existing signing auth unless
    forced.
    """
    Path(f"{authname}").mkdir(parents=True, exist_ok=True)
    if not any([Path(f"{authname}/{authname}.crt").is_file() and Path(f"{authname}/{authname}.key").is_file()]):
        print(
            f"""Nothing found, creating:
- {authname}/{authname}.crt
- {authname}/{authname}.key
- {authname}/{authname}.pfx
- {authname}/{authname}.cer
            """
        )
    elif not force and all(
        [
            Path(f"{authname}/{authname}.crt").is_file() and Path(f"{authname}/{authname}.key").is_file(),
        ]
    ):
        print(
            f"""A signing authority and Key with the name {authname}.[ crt | key ] already exists.
Use --force to overwrite."""
        )
        raise KeyboardInterrupt
    elif not force:
        print(
            f"""{authname}/{authname}.crt: {'FOUND' if Path(f'{authname}/{authname}.crt').is_file() else 'NOT FOUND'}
{authname}/{authname}.key: {'FOUND' if Path(f'{authname}/{authname}.key').is_file() else 'NOT FOUND'}

You will either have to locate the missing file, or recreate the signing authority and key with --force
"""
        )
        raise KeyboardInterrupt

    call(
        [
            "openssl",
            "genrsa",
            "-out",
            f"{authname}/{authname}.key",
            f"{bits}",
        ]
    )
    call(
        [
            "openssl",
            "req",
            "-x509",
            "-new",
            "-nodes",
            "-subj",
            f"/C={country}/O={organization}/CN={commonname}",
            "-key",
            f"{authname}/{authname}.key",
            f"-{cipher}",
            "-days",
            f"{days}",
            "-out",
            f"{authname}/{authname}.crt",
        ]
    )
    call(
        [
            "openssl",
            "pkcs12",
            "-export",
            "-inkey",
            f"{authname}/{authname}.key",
            "-in",
            f"{authname}/{authname}.crt",
            "-out",
            f"{authname}/{authname}.pfx",
        ]
    )
    call(
        [
            "openssl",
            "x509",
            "-inform",
            "PEM",
            "-in",
            f"{authname}/{authname}.crt",
            "-outform",
            "DER",
            "-out",
            f"{authname}/{authname}.cer",
        ]
    )
