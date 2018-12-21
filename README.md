# vtt_to_srt.py

useful python script

## convert all vtt files to srt subtitle format

Usage from terminal:
----------

pyhton vtt_to_srt.py pathname [-r]
	
pathname - a file or directory with files to be converted 

-r       - walk path recursively                          

Usage as a lib:
----------

		# convert vtt file
		
		from vtt_to_srt import vtt_to_srt
		path = '/path/to/file.vtt'
		vtt_to_srt(path)
		
		
		# recursively convert all vtt files in directory
		
		from vtt_to_srt import vtts_to_srt
		path = '/path/to/directory'
		vtts_to_srt(path, rec = True)
