#!/usr/bin/python
# Jeison Cardoso

import os
import pytest

from test_base import concat_path, equals_files, clean_files
from vtt_to_srt.vtt_to_srt import ConvertDirectories


class TestConvertDirectories:
    """Test ConvertFile class"""

    def test_convert_directory(self, clean_files):
        """Test convert file"""
        convert_file = ConvertDirectories(
            concat_path("."), False, "utf-8")
        convert_file.convert()

        assert equals_files("input_alternative_utf8.srt",
                            "valid_output_utf8.srt", "utf-8")

    def test_convert_directory_recursive(self, clean_files):
        """Test convert file"""
        convert_file = ConvertDirectories(
            concat_path("."), True, "utf-8")
        convert_file.convert()

        assert equals_files("input_alternative_utf8.srt",
                            "valid_output_utf8.srt", "utf-8")
