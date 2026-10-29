from pathlib import Path

from src.file_utils import file_exists


def test_existing_file(tmp_path):
    path = tmp_path / "sample.txt"
    path.write_text("ok")
    assert file_exists(str(path))


def test_missing_file(tmp_path):
    assert not file_exists(str(tmp_path / "missing.txt"))
