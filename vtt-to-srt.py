#!/usr/bin/python
#---------------------------------------
# vtt-to-srt.py
# (c) Jansen A. Simanullang
# 02.04.2016 13:39
#---------------------------------------
# usage: python vtt-to-srt.py
#
# example:
# python vtt-to-srt.py
#
# features:
# convert all vtt files in a directory
# to srt subtitle format
#
# real world needs:
# converting Coursera's vtt subtitle


import os, re


def fileFilter(path, fileExtension):

	dirContents  = os.listdir(path)
	selectedFiles = []
	
	count = 0

	for filename in dirContents:

		if fileExtension in filename:
		
			print filename.strip()
			
			count = count + 1
			
			selectedFiles.append(path+filename)
			
	print "\nThere are ", count, fileExtension + " files\n\n"

	return selectedFiles
	

	
def convertContent(fileContents):

	replacement = re.sub(r'([\d]+)\.([\d]+)', r'\1,\2', fileContents)
	replacement = re.sub(r'WEBVTT\n\n', '', replacement)
	replacement = re.sub(r'^\d+\n', '', replacement)
	replacement = re.sub(r'\n\d+\n', '\n', replacement)

	return replacement
	


def fileCreate(strNamaFile, strData):
	#--------------------------------
	# fileCreate(strNamaFile, strData)
	# create a text file
	#
	try:
	
		f = open(strNamaFile, "w")
		f.writelines(str(strData))
		f.close()
	
	except IOError:
	
		strNamaFile = strNamaFile.split(os.sep)[-1]
		f = open(strNamaFile, "w")
		f.writelines(str(strData))
		f.close()
		
	print "file created: " + strNamaFile + "\n"
	
	
	
def readTextFile(strNamaFile):

	f = open(strNamaFile, "r")
	
	print "file being read: " + strNamaFile + "\n"
	
	return f.read().decode("windows-1252").encode('ascii', 'ignore')
	


def vtt_to_srt(strNamaFile):

	fileContents = readTextFile(strNamaFile)
	
	strData = ""
	
	strData = strData + convertContent(fileContents)
	
	strNamaFile = strNamaFile.replace(".vtt",".srt")
		
	print strNamaFile
		
	fileCreate(strNamaFile, strData)
	
	
	
def main():

	# just edit the path below
	path = 'C:\Users\developer\Videos\Virtual Universities\Coursera\Using Databases with Python\\'

	selectedFiles = fileFilter(path, ".vtt")

	for files in selectedFiles:
		
		vtt_to_srt(files)

	
main()