"""Settings file."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

from assertion.protocols import OIDCProtocol, SettingsProtocol

load_dotenv()

__all__: list[str] = [
    "SETTINGS",
    "SettingsProtocol",
]


@dataclass(eq=False)
class BaseSettings:
    def __post_init__(self):
        """Read and set the config object."""
        for name, _ in self.__dataclass_fields__.items():
            if match := os.getenv(name):
                setattr(self, name, match)


@dataclass(eq=False)
class OIDC(BaseSettings):
    fingerprint: Path = field(default_factory=lambda: Path())
    public_key: Path = field(default_factory=lambda: Path())
    token_url: str = field(default="")
    client_id: str = field(default="")
    grant_type: str = field(default="")
    scope: str = field(default="")
    headers: dict[str, str] = field(
        default_factory=lambda: {
            "Content-type": "application/x-www-form-urlencoded",
        }
    )


@dataclass(eq=False)
class Settings(BaseSettings):
    base_dir: Path = field(
        default_factory=lambda: Path(__file__).resolve().parent.parent,
    )
    OIDC: OIDCProtocol = field(default_factory=lambda: OIDC())


SETTINGS: SettingsProtocol = Settings()
