import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='vtt_to_srt3',  
     version='0.1.1',
     scripts=['vtt_to_srt.py'] ,
     author="0um",
     author_email="cardoso.jeison@gmail.com",
     description="vtt to srt subtitles converter package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/0um/vtt-to-srt.py",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3.7",
         "Operating System :: OS Independent",
     ],
 )
