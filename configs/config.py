"""
platform: win
env: any
name: config.py
project configurations
"""

import os

# platform specific
platform_delimiter = "\\"

# project structure
configs_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.split(configs_dir)[0]
tmp_dir = os.path.join(project_dir, "tmp")

# dataset related
coreset_dir = "E:\\datasets\\casf2016\\CASF-2016\\coreset"
