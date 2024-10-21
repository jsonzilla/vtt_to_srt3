#!/usr/bin/python
# Jeison Cardoso

import os
import pytest

from test_base import concat_path, equals_files, clean_files
from vtt_to_srt.vtt_to_srt import ConvertFile


class TestConvertFile:
    """Test ConvertFile class"""

    def test_convert_file(self, clean_files):
        """Test convert file"""
        convert_file = ConvertFile(
            concat_path("input_utf8.vtt"), "utf-8")
        convert_file.convert()

        assert equals_files("input_utf8.srt",
                            "valid_output_utf8.srt", "utf-8")

    def test_convert_file_with_simple_identifier(self, clean_files):
        """Test convert file with simple identifier"""
        convert_file = ConvertFile(concat_path("idd.vtt"), "utf-8")
        convert_file.convert()

        assert equals_files("idd.srt",
                            "valid_output_idd.srt", "utf-8")

    def test_convert_file_not_utf8(self, clean_files):
        """Test convert file with not utf-8 encoding"""
        convert_file = ConvertFile(
            concat_path("input_iso-8859-2.vtt"), "ISO-8859-2")
        convert_file.convert()

        assert equals_files("input_iso-8859-2.srt",
                            "valid_output_iso-8859-2.srt", "ISO-8859-2")
                            
    def test_convert_file_no_format(self, clean_files):
        """ Test convert file with remove format tags """
        convert_file = ConvertFile(concat_path("idd_format.vtt"), "utf-8", True)
        convert_file.convert()
        
        assert equals_files("idd_format.srt",
                            "valid_output_idd_format.srt", "utf-8")
                            
    def test_convert_file_different_timestamp_formats(self, clean_files):
        """Test convert file with different timestamp formats"""
        convert_file = ConvertFile(concat_path("input_different_timestamps.vtt"), "utf-8")
        convert_file.convert()

        assert equals_files("input_different_timestamps.srt",
                            "valid_output_different_timestamps.srt", "utf-8")

    def test_convert_file_special_characters_symbols(self, clean_files):
        """Test convert file with special characters and symbols"""
        convert_file = ConvertFile(concat_path("input_special_characters.vtt"), "utf-8")
        convert_file.convert()

        assert equals_files("input_special_characters.srt",
                            "valid_output_special_characters.srt", "utf-8")

    def test_convert_file_multiple_languages(self, clean_files):
        """Test convert file with multiple languages"""
        convert_file = ConvertFile(concat_path("input_multiple_languages.vtt"), "utf-8")
        convert_file.convert()

        assert equals_files("input_multiple_languages.srt",
                            "valid_output_multiple_languages.srt", "utf-8")

    def test_convert_file_overlapping_timestamps(self, clean_files):
        """Test convert file with overlapping timestamps"""
        convert_file = ConvertFile(concat_path("input_overlapping_timestamps.vtt"), "utf-8")
        convert_file.convert()

        assert equals_files("input_overlapping_timestamps.srt",
                            "valid_output_overlapping_timestamps.srt", "utf-8")

    def test_convert_file_with_remove_format(self, clean_files):
        """Test convert file with remove format option"""
        convert_file = ConvertFile(concat_path("input_utf8.vtt"), "utf-8", True)
        convert_file.convert()

        assert equals_files("input_utf8.srt",
                            "valid_output_utf8.srt", "utf-8")
