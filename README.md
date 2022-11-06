# vtt_to_srt3
Convert vtt files to srt subtitle format
> For Python 3.x [you can get version for Python 2.7 here](https://github.com/jansenicus/vtt-to-srt.py)

## Docs
[https://jsonzilla.github.io/vtt_to_srt3/](https://jsonzilla.github.io/vtt_to_srt3/)


## Installation
```shell
pip install vtt_to_srt3
```

```cmd
python -m pip install vtt_to_srt3
```

## Usage from terminal

```shell
usage: vtt_to_srt.py [-h] [-r] [-e ENCODING] pathname

Convert vtt files to srt files

positional arguments:
  pathname              a file or directory with files to be converted

options:
  -h, --help            show this help message and exit
  -r, --recursive       walk path recursively
  -e ENCODING, --encoding ENCODING
                        encoding format for input and output files
```

## Usage as a lib

Convert vtt file
```python
from vtt_to_srt.vtt_to_srt import ConvertFile

convert_file = ConvertFile("input_utf8.vtt", "utf-8")
convert_file.convert()
```

Recursively convert all vtt files in directory
```python
from vtt_to_srt.vtt_to_srt import ConvertDirectories

recursive = False
convert_file = ConvertDirectories(".", recursive, "utf-8")
convert_file.convert()
```

## Manual build

Generate wheel
```shell
python -m pip install --upgrade setuptools wheel build
python -m build
```

## Generate documentation

Generate documentation
```shell
python -m pip install pdoc3
pdoc --html vtt_to_srt/vtt_to_srt.py -o docs
mv docs/vtt_to_srt.html docs/index.html
rm -rm docs/vtt_to_srt
```
