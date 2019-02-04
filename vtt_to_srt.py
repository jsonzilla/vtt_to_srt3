#!/usr/bin/python
# ---------------------------------------
# vtt_to_srt.py
# (c) Jansen A. Simanullang
# ---------------------------------------
# Usage: 
#
# vtt_to_srt.py pathname [-r]
#
# pathname - a file or directory with files to be converted"
#
# -r  - walk path recursively
#
# example:
# vtt_to_srt.py subtitle.vtt
#
# features:
# convert file individually
# check a directory and all its subdirectories
# convert all vtt files to srt subtitle format
#
# real world cases:
# convert vtt web subtitles

import os
import re
import sys
import io
from stat import *
from typing import TextIO


def convert_content(file_contents: str):
    replacement = re.sub(r"(\d\d:\d\d:\d\d).(\d\d\d) --> (\d\d:\d\d:\d\d).(\d\d\d)(?:[ \-\w]+:[\w\%\d:]+)*\n", r"\1,\2 --> \3,\4\n", file_contents)
    replacement = re.sub(r"(\d\d:\d\d).(\d\d\d) --> (\d\d:\d\d).(\d\d\d)(?:[ \-\w]+:[\w\%\d:]+)*\n", r"\1,\2 --> \3,\4\n", replacement)
    replacement = re.sub(r"(\d\d).(\d\d\d) --> (\d\d).(\d\d\d)(?:[ \-\w]+:[\w\%\d:]+)*\n", r"\1,\2 --> \3,\4\n", replacement)
    replacement = re.sub(r"WEBVTT\n", "", replacement)
    replacement = re.sub(r"Kind:[ \-\w]+\n", "", replacement)
    replacement = re.sub(r"Language:[ \-\w]+\n", "", replacement)
    # replacement = re.sub(r"^\d+\n", "", replacement)
    # replacement = re.sub(r"\n\d+\n", "\n", replacement)
    replacement = re.sub(r"<c[.\w\d]*>", "", replacement)
    replacement = re.sub(r"</c>", "", replacement)
    replacement = re.sub(r"<\d\d:\d\d:\d\d.\d\d\d>", "", replacement)
    replacement = re.sub(r"::[\-\w]+\([\-.\w\d]+\)[ ]*{[.,:;\(\) \-\w\d]+\n }\n", "", replacement)
    replacement = re.sub(r"Style:\n##\n", "", replacement)
    return replacement


def file_create(str_name_file, str_data):
    # --------------------------------
    # file_create(str_name_file, str_data)
    # create a text file
    try:
        f = open(str_name_file, "w")
        f.writelines(str(str_data))
        f.close()
    except IOError:
        str_name_file = str_name_file.split(os.sep)[-1]
        f = open(str_name_file, "w")
        f.writelines(str(str_data))
        f.close()
    print("file created: " + str_name_file + "\n")


def read_text_file(str_name_file):
    f = open(str_name_file, mode="r")
    print("file being read: " + str_name_file + "\n")
    return f.read()


def vtt_to_srt(str_name_file):
    file_contents: str = read_text_file(str_name_file)
    str_data: str = ""
    str_data = str_data + convert_content(file_contents)
    str_name_file: str = str_name_file.replace(".vtt", ".srt")
    print(str_name_file)
    file_create(str_name_file, str_data)


def walk_tree(top_most_path, callback):
    # recursively descend the directory tree rooted at top_most_path,
    # calling the callback function for each regular file
    for f in os.listdir(top_most_path):
        pathname = os.path.join(top_most_path, f)
        mode = os.stat(pathname)[ST_MODE]
        if S_ISDIR(mode):
            # It"s a directory, recurse into it
            walk_tree(pathname, callback)
        elif S_ISREG(mode):
            # It"s a file, call the callback function
            callback(pathname, rec)
        else:
            # Unknown file type, print a message
            print("Skipping %s" % pathname)


def walk_dir(top_most_path, callback):
    for f in os.listdir(top_most_path):
        pathname = os.path.join(top_most_path, f)
        if not os.path.isdir(pathname):
            # It"s a file, call the callback function
            callback(pathname)


def convert_vtt_to_str(f):
    if ".vtt" in f:
        vtt_to_srt(f)


def vtts_to_srt(directory, rec = False):
    top_most_path = directory
    if rec:
        walk_tree(top_most_path, convert_vtt_to_str)
    else:
        walk_dir(top_most_path, convert_vtt_to_str)


def print_usage():
    print("\nUsage:\tpython vtt_to_srt.py pathname [-r]\n")
    print("\tpathname\t- a file or directory with files to be converted")
    print("\t-r\t\t- walk path recursively\n")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "--help" or not os.path.exists(sys.argv[1]):
        print_usage()
        exit()
    path = sys.argv[1]
    rec = True if len(sys.argv) > 2 and sys.argv[2] == "-r" else False
    if os.path.isdir(path):
        vtts_to_srt(path, rec)
    else:
        vtt_to_srt(path)

