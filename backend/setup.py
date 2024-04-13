#!/usr/bin/env python



try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup



setup(name='Gmail-Inbox-Manager',
      version='1.0',
      description='Python Distribution Utilities',
      author='Yakobishin Timofey',
      author_email='yakovishintimofey@gmail.com',
     )

install_requires=[
    "fastapi==0.110.1",
    "uvicorn[standard]==0.29.0",
    "pydantic[email]==2.7.0"
],