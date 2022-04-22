# configuration for making the file installable

installation_config = """
[build-system]
requires = ["setuptools>=42.0", "wheel"]
build-backend = "setuptools.build_meta
"""

setup_code = """
import setuptools import setup

if __name__ == "__main__":
    setup()

"""

def setup_cfg(project, desc, author):
    return f"""
[metadata]
name = {project}
description = {desc}
author = {author}
license = GNU
license = LICENSE.md
platform = unix, linux, win32
classifiers = 
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3 :: only
    Programming Language :: Python :: 3.6
    Programming Language :: Python :: 3.7
    Programming Language :: Python :: 3.8
    Programming Language :: Python :: 3.9
    
[options]
packages = src
python_requires = >=3.*
package_dir = 
    =src
zip_safe = no
    
"""