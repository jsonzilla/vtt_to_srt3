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

    def test_convert_directory_different_timestamp_formats(self, clean_files):
        """Test convert directory with different timestamp formats"""
        convert_file = ConvertDirectories(concat_path("test_directory_different_timestamps"), False, "utf-8")
        convert_file.convert()

        assert equals_files("test_directory_different_timestamps/input_different_timestamps.srt",
                            "test_directory_different_timestamps/valid_output_different_timestamps.srt", "utf-8")

    def test_convert_directory_special_characters_symbols(self, clean_files):
        """Test convert directory with special characters and symbols"""
        convert_file = ConvertDirectories(concat_path("test_directory_special_characters"), False, "utf-8")
        convert_file.convert()

        assert equals_files("test_directory_special_characters/input_special_characters.srt",
                            "test_directory_special_characters/valid_output_special_characters.srt", "utf-8")

    def test_convert_directory_multiple_languages(self, clean_files):
        """Test convert directory with multiple languages"""
        convert_file = ConvertDirectories(concat_path("test_directory_multiple_languages"), False, "utf-8")
        convert_file.convert()

        assert equals_files("test_directory_multiple_languages/input_multiple_languages.srt",
                            "test_directory_multiple_languages/valid_output_multiple_languages.srt", "utf-8")

    def test_convert_directory_overlapping_timestamps(self, clean_files):
        """Test convert directory with overlapping timestamps"""
        convert_file = ConvertDirectories(concat_path("test_directory_overlapping_timestamps"), False, "utf-8")
        convert_file.convert()

        assert equals_files("test_directory_overlapping_timestamps/input_overlapping_timestamps.srt",
                            "test_directory_overlapping_timestamps/valid_output_overlapping_timestamps.srt", "utf-8")
