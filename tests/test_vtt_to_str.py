#!/usr/bin/python
# Jeison Cardoso

import pytest

from vtt_to_srt.vtt_to_srt import VttToStr


class TestVttToStr:
    def test_convert_header(self):
        assert repr(VttToStr().convert_header(
            "WEBVTT\nKind: captions\nLanguage: zh-TW")) == repr("Language: zh-TW")

    def test_convert_timestamp(self):
        vtt_to_str = VttToStr()
        assert repr(vtt_to_str.convert_timestamp("00:03:08.500 --> 00:03:15.300\n")
                    ) == repr("00:03:08,500 --> 00:03:15,300\n")
        assert repr(vtt_to_str.convert_timestamp("03:08.500 --> 03:15.300\n")
                    ) == repr("00:03:08,500 --> 00:03:15,300\n")
        assert repr(vtt_to_str.convert_timestamp("08.500 --> 15.300\n")
                    ) == repr("00:00:08,500 --> 00:00:15,300\n")

    def test_not_add_sequence_before(self):
        vtt_to_str = VttToStr()
        assert repr(vtt_to_str.add_sequence_numbers("What you got, a billion could've never bought (oooh)")) == repr(
            "What you got, a billion could've never bought (oooh)\n")
        assert repr(vtt_to_str.add_sequence_numbers("")
                    ) == repr("\n")
        assert repr(vtt_to_str.add_sequence_numbers("告訴你，今晚我想帶你出去。")) == repr(
            "告訴你，今晚我想帶你出去。\n")
        assert repr(vtt_to_str.add_sequence_numbers("Hi --> MAX")
                    ) == repr("Hi --> MAX\n")

    def test_add_sequence_before_timestamp(self):
        vtt_to_str = VttToStr()
        assert repr(vtt_to_str.add_sequence_numbers("00:03:08,500 --> 00:03:15,300")
                    ) == repr("1\n00:03:08,500 --> 00:03:15,300\n")

    def test_convert_empty_return_newline(self):
        vtt_to_str = VttToStr()
        assert repr(vtt_to_str.convert_content("")) == repr("\n")

    def test_convert_header_language(self):
        vtt_to_str = VttToStr()
        assert repr(vtt_to_str.convert_content("WEBVTT\nKind: captions\nLanguage: zh-TW")
                    ) == repr("Language: zh-TW\n")

    def test_text(self):
        vtt_to_str = VttToStr()
        assert repr(vtt_to_str.convert_content("告訴你，今晚我想帶你出去。")) == repr(
            "告訴你，今晚我想帶你出去。\n")
        assert repr(vtt_to_str.convert_content("What you got, a billion could've never bought (oooh)")) == repr(
            "What you got, a billion could've never bought (oooh)\n")

    def test_convert_different_timestamp_formats(self):
        vtt_to_str = VttToStr()
        input_content = "00:03:08.500 --> 00:03:15.300\n03:08.500 --> 03:15.300\n08.500 --> 15.300\n"
        expected_output = "00:03:08,500 --> 00:03:15,300\n00:03:08,500 --> 00:03:15,300\n00:00:08,500 --> 00:00:15,300\n"
        assert repr(vtt_to_str.convert_content(input_content)) == repr(expected_output)

    def test_convert_special_characters_symbols(self):
        vtt_to_str = VttToStr()
        input_content = "00:03:08.500 --> 00:03:15.300\n- Special characters: !@#$%^&*()\n"
        expected_output = "1\n00:03:08,500 --> 00:03:15,300\n- Special characters: !@#$%^&*()\n"
        assert repr(vtt_to_str.convert_content(input_content)) == repr(expected_output)

    def test_convert_multiple_languages(self):
        vtt_to_str = VttToStr()
        input_content = "00:03:08.500 --> 00:03:15.300\n- English\n00:03:16.000 --> 00:03:20.000\n- 中文\n"
        expected_output = "1\n00:03:08,500 --> 00:03:15,300\n- English\n2\n00:03:16,000 --> 00:03:20,000\n- 中文\n"
        assert repr(vtt_to_str.convert_content(input_content)) == repr(expected_output)

    def test_convert_overlapping_timestamps(self):
        vtt_to_str = VttToStr()
        input_content = "00:03:08.500 --> 00:03:15.300\n00:03:10.000 --> 00:03:12.000\n"
        expected_output = "1\n00:03:08,500 --> 00:03:15,300\n2\n00:03:10,000 --> 00:03:12,000\n"
        assert repr(vtt_to_str.convert_content(input_content)) == repr(expected_output)

    def test_convert_content_with_remove_format(self):
        vtt_to_str = VttToStr()
        input_content = "WEBVTT\n00:03:08.500 --> 00:03:15.300\n<i>Formatted text</i>\n"
        expected_output = "1\n00:03:08,500 --> 00:03:15,300\nFormatted text\n"
        assert repr(vtt_to_str.convert_content(input_content, remove_format=True)) == repr(expected_output)
