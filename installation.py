# configuration for making the file installable

installation_config = """

[build-system]
requires = ["setuptools>=42.0", "wheel"]
build-backend = "setuptools.build_meta"

[tool.pytest.ini_options]
addopts = "--cov=src"
testpaths = [
    "tests",
]

[tool.mypy]
mypy_path = "src"
check_untyped_defs = true
disallow_any_generics = true
ignore_missing_imports = true
no_implicit_optional = true
show_error_codes = true
strict_equality = true
warn_redundant_casts = true
warn_return_any = true
warn_unreachable = true
warn_unused_configs = true
no_implicit_reexport = true
"""

setup_code = """
from setuptools import setup

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
license_file = LICENSE
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
install_requires = 
    requests>=2
python_requires = >=3.*
zip_safe = no
    
"""