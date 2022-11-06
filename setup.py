import setuptools

with open(file="README.md", mode="r", encoding="utf-8") as fh:

    long_description = fh.read()

setuptools.setup(name='vtt_to_srt3',
                 version='0.1.9.2',
                 author="Jeison Cardoso",
                 author_email="j@jsonzilla.com",
                 description="vtt to srt subtitles converter package",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://github.com/jsonzilla/vtt-to-srt.py",
                 packages=setuptools.find_packages(
                     exclude=["test_*.py", "valid*.*", "input*.*"]),
                 classifiers=["Programming Language :: Python :: 3.7",
                              "Programming Language :: Python :: 3.8",
                              "Programming Language :: Python :: 3.9",
                              "Programming Language :: Python :: 3.10",
                              "Programming Language :: Python :: 3.11",
                              "Operating System :: OS Independent"],
                 entry_points={
                     "console_scripts":
                     ["vtt_to_srt=vtt_to_srt.vtt_to_srt:main"]
                 },
                 )
