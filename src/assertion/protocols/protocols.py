"""Protocols definition."""
from pathlib import Path
from typing import Protocol


class OIDCProtocol(Protocol):
    fingerprint: Path
    public_key: Path
    token_url: str
    client_id: str
    grant_type: str
    scope: str
    headers: dict[str, str]


class SettingsProtocol(Protocol):
    base_dir: Path
    OIDC: OIDCProtocol

