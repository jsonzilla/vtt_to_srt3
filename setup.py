import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(
     name='vtt_to_srt3',
     version='0.1.8.3',
     author="Jeison Cardoso",
     author_email="cardoso.jeison@gmail.com",
     description="vtt to srt subtitles converter package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/amorvincitomnia/vtt-to-srt.py",
     packages=['vtt_to_srt'],
     classifiers=[
         "Programming Language :: Python :: 3.7",
         "Operating System :: OS Independent",
     ],
 )
