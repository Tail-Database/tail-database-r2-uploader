#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "rt") as fh:
    long_description = fh.read()

dependencies = [
    "boto3==1.26.9",
]

dev_dependencies = []

setup(
    name="tail-database-r2-uploader",
    packages=find_packages(exclude=("tests",)),
    author="Freddie Coleman",
    author_email="f.coleman@chia.net",
    setup_requires=["setuptools_scm"],
    install_requires=dependencies,
    url="https://github.com/Tail-Database/tail-database-r2-uploader",
    license="https://opensource.org/licenses/Apache-2.0",
    description="Uploads data to R2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Security :: Cryptography",
    ],
    extras_require=dict(
        dev=dev_dependencies,
    ),
    project_urls={
        "Bug Reports": "https://github.com/Tail-Database/tail-database-r2-uploader",
        "Source": "https://github.com/Tail-Database/tail-database-r2-uploader",
    },
)
