import os
import pytest


def _clean():
    """Remove all files with .srt extension without valid_output in name recursively"""
    for root, _, files in os.walk(os.path.dirname(__file__)):
        for file in files:
            if file.endswith(".srt") and "valid_output" not in file:
                os.remove(os.path.join(root, file))


@pytest.fixture(autouse=True, scope="module")
def clean_files():
    """Clean files"""
    _clean()
    yield
    _clean()


def concat_path(pathname):
    """Concat path to file"""
    return os.path.join(os.path.dirname(__file__), pathname)


def equals_files(file_a, file_b, encoding):
    """Compare two text files"""
    with open(concat_path(file_a), encoding=encoding) as f1, open(concat_path(file_b), encoding=encoding) as f2:
        return f1.read() == f2.read()
