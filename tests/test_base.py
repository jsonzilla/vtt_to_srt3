#!/usr/bin/python
# Jeison Cardoso


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
    """Concat path to file for unix and windows"""
    return os.path.join(os.path.dirname(__file__), pathname)


def equals_files(file_a, file_b, encoding):
    """Compare two text files independently of line endings"""
    with open(concat_path(file_a), "r", encoding=encoding) as file_a:
        with open(concat_path(file_b), "r", encoding=encoding) as file_b:
            a = file_a.read()
            b = file_b.read()
            return a == b
