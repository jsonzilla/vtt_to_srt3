#!/usr/bin/python
# Jansen A. Simanullang / Jeison Cardoso

"""Convert of vtt to srt format"""

import os
import re
import sys
from string import Template
from stat import S_ISDIR, ST_MODE, S_ISREG


def convert_header(contents):
    """Convert of vtt header to srt format

       Keyword arguments:
       contents
       """
    replacement = re.sub(r"WEBVTT\n", "", contents)
    replacement = re.sub(r"Kind:[ \-\w]+\n", "", replacement)
    replacement = re.sub(r"Language:[ \-\w]+\n", "", replacement)
    return replacement


def padding_timestamp(contents):
    """Add 00 to padding timestamp of to srt format

       Keyword arguments:
       contents
       """
    find_srt = Template(r'$a,$b --> $a,$b(?:[ \-\w]+:[\w\%\d:,.]+)*\n')
    minute = r"((?:\d\d:){1}\d\d)"
    second = r"((?:\d\d:){0}\d\d)"
    padding_minute = find_srt.substitute(a=minute, b=r"(\d{0,3})")
    padding_second = find_srt.substitute(a=second, b=r"(\d{0,3})")
    replacement = re.sub(padding_minute, r"00:\1,\2 --> 00:\3,\4\n", contents)
    return re.sub(padding_second, r"00:00:\1,\2 --> 00:00:\3,\4\n", replacement)


def convert_timestamp(contents):
    """Convert timestamp of vtt file to srt format

       Keyword arguments:
       contents
       """
    find_vtt = Template(r'$a.$b --> $a.$b(?:[ \-\w]+:[\w\%\d:,.]+)*\n')
    all_timestamp = find_vtt.substitute(a=r"((?:\d\d:){0,2}\d\d)", b=r"(\d{0,3})")
    return padding_timestamp(re.sub(all_timestamp, r"\1,\2 --> \3,\4\n", contents))


def convert_content(contents):
    """Convert content of vtt file to srt format

       Keyword arguments:
       contents
       """
    replacement = convert_timestamp(contents)
    replacement = convert_header(replacement)
    replacement = re.sub(r"<c[.\w\d]*>", "", replacement)
    replacement = re.sub(r"</c>", "", replacement)
    replacement = re.sub(r"<\d\d:\d\d:\d\d.\d\d\d>", "", replacement)
    replacement = re.sub(r"::[\-\w]+\([\-.\w\d]+\)[ ]*{[.,:;\(\) \-\w\d]+\n }\n", "", replacement)
    replacement = re.sub(r"Style:\n##\n", "", replacement)
    replacement = add_sequence_numbers(replacement)
    return replacement

  
def timestamp_line(content):
    """Check if line is a timestamp srt format

       Keyword arguments:
       contents
       """
    return re.match(r"((\d\d:){2}\d\d),(\d{3}) --> ((\d\d:){2}\d\d),(\d{3})", content) is not None


def add_sequence_numbers(contents):
    """Adds sequence numbers to subtitle contents and returns new subtitle contents

       Keyword arguments:
       contents
       """
    output = ''
    lines = contents.split(os.linesep)

    i = 1
    for line in lines:
        if timestamp_line(line):
            output += str(i) + os.linesep
            i += 1
        output += line + os.linesep
    return output


def file_create(str_name_file: str, str_data):
    """Create a file with some data

       Keyword arguments:
       str_name_file -- filename pat
       str_data -- dat to write
       """
    try:
        with open(str_name_file, "w", encoding='utf-8') as file:
            file.writelines(str(str_data))
    except IOError:
        str_name_file = str_name_file.split(os.sep)[-1]
        with open(str_name_file, "w") as file:
            file.writelines(str(str_data))
    print("file created: " + str_name_file + "\n")


def read_text_file(str_name_file: str):
    """Read a file text

       Keyword arguments:
       str_name_file -- filename pat
       """
    content: str = ''
    with open(str_name_file, mode="r", encoding='utf-8') as file:
        print("file being read: " + str_name_file + "\n")
        content = file.read()
    return content


def vtt_to_srt(str_name_file: str):
    """Convert vtt file to a srt file

       Keyword arguments:
       str_name_file -- filename path
       """
    file_contents: str = read_text_file(str_name_file)
    str_data: str = ""
    str_data = str_data + convert_content(file_contents)
    str_name_file: str = str_name_file.replace(".vtt", ".srt")
    print(str_name_file)
    file_create(str_name_file, str_data)


def walk_tree(top_most_path, callback):
    """Recursively descend the directory tree rooted at top_most_path,
       calling the callback function for each regular file

       Keyword arguments:
       top_most_path -- parent directory
       callback -- function to call
       """
    for file in os.listdir(top_most_path):
        pathname = os.path.join(top_most_path, file)
        mode = os.stat(pathname)[ST_MODE]
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walk_tree(pathname, callback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
            callback(pathname)
        else:
            # Unknown file type, print a message
            print("Skipping %s" % pathname)


def walk_dir(top_most_path, callback):
    """Walk a directory

       Keyword arguments:
       top_most_path -- parent directory
       callback -- function to call
       """
    for file in os.listdir(top_most_path):
        pathname = os.path.join(top_most_path, file)
        if not os.path.isdir(pathname):
            # It"s a file, call the callback function
            callback(pathname)


def convert_vtt_to_str(file):
    """Convert vtt file to string

       Keyword arguments:
       f -- file to convert
       """
    if ".vtt" in file:
        vtt_to_srt(file)


def vtts_to_srt(directory, rec = False):
    """Walk down directory seaching for vtt files

       Keyword arguments:
       directory -- path to search
       rec -- enable recursive
       """
    top_most_path = directory
    if rec:
        walk_tree(top_most_path, convert_vtt_to_str)
    else:
        walk_dir(top_most_path, convert_vtt_to_str)


def print_usage():
    """Show a info message about the usage"""
    print("\nUsage:\tvtt_to_srt pathname [-r]\n")
    print("\tpathname\t- a file or directory with files to be converted")
    print("\t-r\t\t- walk path recursively\n")


def main():
    """main

       Keyword arguments:
        pathname - a file or directory with files to be converted
        -r walk path recursively
       """
    if len(sys.argv) < 2 or sys.argv[1] == "--help" or not os.path.exists(sys.argv[1]):
        print_usage()
        sys.exit()
    path = sys.argv[1]
    rec = bool(len(sys.argv) > 2 and sys.argv[2] == "-r")
    if os.path.isdir(path):
        vtts_to_srt(path, rec)
    else:
        vtt_to_srt(path)


if __name__ == "__main__":
    main()
