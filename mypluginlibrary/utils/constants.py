# Author - Karan Parmar

"""
Constants - App default settings, that can be changed from here
"""

# Importing built-in libraries
from pathlib import PurePath

BASE_DIR = PurePath(__file__).parent.parent
BASE_DIR_NAME = BASE_DIR.name

# NOTE INTERNAL PLUGINS THAT MUST BE LOADED
INTERNAL_PLUGINS = []

# NOTE APP CONSTANTS

# NOTE DEFAULT SETTINGS
DEFAULT_TIMEZONE = "UTC"

# NOTE DEFAULT PLUGIN