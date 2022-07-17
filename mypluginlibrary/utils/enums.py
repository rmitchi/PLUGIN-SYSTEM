# Author - Karan Parmar


"""
ENUMS
"""

class APP_MODE:

	LIVE = "LIVE"
	BACKTEST = "BACKTEST"
	PAPERTRADE = "PAPERTRADE"
	OPTIMIZE = "OPTIMIZE"

class APP_KEY:
	
	# App config keys
	PLUGINS = "plugins"

	LOGS = "logs"

	# Root level keys
	TIMEZONE = "timezone"

class PLUGIN_TYPE:

	...