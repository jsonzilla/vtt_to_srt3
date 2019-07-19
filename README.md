# vtt_to_srt.py
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/19bdc455a1df45f59423445e4cb92110)](https://www.codacy.com/app/0um/vtt-to-srt.py?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=0um/vtt-to-srt.py&amp;utm_campaign=Badge_Grade)

Convert vtt files to srt subtitle format

## Note
For Python 3.7 [you can get version for Python 2.7 here](https://github.com/jansenicus/vtt-to-srt.py)

## Installation
```shell
pip install vtt_to_srt3
```

## Usage from terminal

```shell
python -m vtt_to_srt pathname [-r]

pathname - a file or directory with files to be converted 

-r       - walk path recursively                          
```

## Usage as a lib

Convert vtt file
```shell
from vtt_to_srt import vtt_to_srt
path = '/path/to/file.vtt'
vtt_to_srt(path)
```		
		
Recursively convert all vtt files in directory
```shell
from vtt_to_srt import vtts_to_srt
path = '/path/to/directory'
vtts_to_srt(path, rec = True)
```
