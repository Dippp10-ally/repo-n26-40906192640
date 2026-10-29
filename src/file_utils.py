"""File system helpers."""

from pathlib import Path


def file_exists(path):
    """Return True when the path exists."""
    return Path(path).exists()
