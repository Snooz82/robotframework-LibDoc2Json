from setuptools import setup
from setuptools import find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="robotframework-libdoc2json",
    version='0.4',
    author="René Rohner(Snooz82)",
    author_email="snooz@posteo.de",
    description="A python module to create json for VSCode Robot Framework Intellisense.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Snooz82/robotframework-LibDoc2Json",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Acceptance",
        "Framework :: Robot Framework",
    ],
    install_requires=[
        'robotframework >= 3.1'],
    python_requires='>3.6'
)
