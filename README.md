# vtt_to_srt.py
Convert vtt files to srt subtitle format

## Note
For Python 3.x [you can get version for Python 2.7 here](https://github.com/jansenicus/vtt-to-srt.py)

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
```shell
from vtt_to_srt.vtt_to_srt import vtt_to_srt
path = '/path/to/file.vtt'
vtt_to_srt(path)
```

Recursively convert all vtt files in directory
```shell
from vtt_to_srt.vtt_to_srt import vtt_to_srt
path = '/path/to/directory'
vtt_to_srt(path, rec = True)
```
