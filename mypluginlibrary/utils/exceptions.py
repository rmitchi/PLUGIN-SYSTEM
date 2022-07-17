# Author - Karan Parmar

"""
EXCEPTIONS
	- Custom exceptions through out the app that categorized here.
	- It is very useful to filter the exceptions and execute tasks accordingly.
"""

# Plugins
class PluginTypeNotAllowed(Exception):
	"""
	Plugin is not allowed\n
	"""

class PluginChangeAccessDenied(Exception):
	"""
	Access denied while changes meta data of plugin\n
	"""

class PluginNotFound(Exception):
	"""
	Plugin not found\n
	"""
