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
                            
