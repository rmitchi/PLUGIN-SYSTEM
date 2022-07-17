# Author - Karan Parmar

"""
App
"""

# Importing depending libraries
from .components import PluginManager
from .utils.constants import DEFAULT_TIMEZONE
from .utils.enums import APP_KEY

class App:

	TIMEZONE = DEFAULT_TIMEZONE

	def __init__(self, *, credentials:dict=..., config:dict=..., app_config:dict=...):
		
		# Configurations
		self.CREDS = credentials
		self.CONFIG = config
		self.APP_CONFIG = app_config

		# Components
		self.PluginManager = PluginManager()

		# Initialize
		self._initialize()

	# Helper methods

	# Private methods
	def _initialize(self) -> None:
		"""
		"""
		
		# NOTE Initializing plugin manager
		self.PluginManager.load_all_internal_plugins()
		self.PluginManager.load_all_external_plugins(plugins=self.APP_CONFIG[APP_KEY.PLUGINS])

	# Public methods
	def run(self) -> None:
		"""
		"""
		...