import vtt_to_srt
import pytest
import os

from vtt_to_srt.vtt_to_srt import *

class TestVttToStr:
    def test_convert_header(self):
        assert repr(convert_header("WEBVTT\nKind: captions\nLanguage: zh-TW")) == repr("Language: zh-TW")

    def test_convert_timestamp(self):
        assert repr(convert_timestamp("00:03:08.500 --> 00:03:15.300\n")) == repr("00:03:08,500 --> 00:03:15,300\n")
        assert repr(convert_timestamp("03:08.500 --> 03:15.300\n")) == repr("00:03:08,500 --> 00:03:15,300\n")
        assert repr(convert_timestamp("08.500 --> 15.300\n")) == repr("00:00:08,500 --> 00:00:15,300\n")        

    def test_not_add_sequence_before(self):
        assert repr(add_sequence_numbers("What you got, a billion could've never bought (oooh)")) == repr("What you got, a billion could've never bought (oooh)"+os.linesep)
        assert repr(add_sequence_numbers("")) == repr(""+os.linesep)
        assert repr(add_sequence_numbers("告訴你，今晚我想帶你出去。")) == repr("告訴你，今晚我想帶你出去。"+os.linesep)
        assert repr(add_sequence_numbers("Hi --> MAX")) == repr("Hi --> MAX"+os.linesep)
    
    def test_add_sequence_before_timestamp(self):
        assert repr(add_sequence_numbers("00:03:08,500 --> 00:03:15,300")) == repr("1"+os.linesep+"00:03:08,500 --> 00:03:15,300"+os.linesep)

    def test_convert_empty_return_newline(self):
        assert repr(convert_content("")) == repr(os.linesep)
        
    def test_convert_header_language(self):
        assert repr(convert_content("WEBVTT\nKind: captions\nLanguage: zh-TW")) == repr("Language: zh-TW"+os.linesep)

    def test_text(self):
        assert repr(convert_content("告訴你，今晚我想帶你出去。")) == repr("告訴你，今晚我想帶你出去。"+os.linesep)
        assert repr(convert_content("What you got, a billion could've never bought (oooh)")) == repr("What you got, a billion could've never bought (oooh)"+os.linesep)