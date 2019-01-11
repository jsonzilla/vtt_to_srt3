# vtt_to_srt.py

useful python script for Python 2.7

## convert all vtt files to srt subtitle format


Installation:
----------

		pip install --user vtt_to_srt

Usage from terminal:
----------

		vtt_to_srt.py pathname [-r]
		
		pathname - a file or directory with files to be converted 
		
		-r       - walk path recursively                          

As a lib:
----------

Usage:

		# convert vtt file
		
		from vtt_to_srt import vtt_to_srt
		path = '/path/to/file.vtt'
		vtt_to_srt(path)
		
		
		# recursively convert all vtt files in directory
		
		from vtt_to_srt import vtts_to_srt
		path = '/path/to/directory'
		vtts_to_srt(path, rec = True)

