# Author - Karan Parmar

"""
Plugin manager - Manages plugins loads and activates
"""

# Importing built-in libraries
import importlib

# Importing dependent libraries
from ..utils.exceptions import PluginNotFound
from ..utils.constants import INTERNAL_PLUGINS

class PluginManager:

	_installed_plugins = {}

	# Public methods
	def load_plugin(self, plugin_path:str):
		"""
		Loads plugin class reference from the plugin module path\n
		"""
		slugs = plugin_path.split('.')
		plugin_module, plugin_name = '.'.join(slugs[:-1]), slugs[-1]
		try:
			return getattr(importlib.import_module(plugin_module), plugin_name)
		except AttributeError:
			raise PluginNotFound(f"Plugin with name {plugin_name} is not found")

	def load_all_internal_plugins(self) -> None:
		"""
		Loads all the internal plugins for the app\n
		"""
		for plugin_path in INTERNAL_PLUGINS:
			plugin = self.load_plugin(plugin_path)
			self.sync_plugin(plugin)

	def load_all_external_plugins(self, plugins:list) -> None:
		"""
		Loads all the external plugins for the app\n
		"""
		for plugin_path in plugins:
			plugin = self.load_plugin(plugin_path)
			self.sync_plugin(plugin)

	def get_plugin(self, plugin_id:str):
		"""
		Get plugin class reference\n
		"""
		Plugin = self._installed_plugins.get(plugin_id)
		if Plugin: 
			return Plugin

		raise PluginNotFound(f"Plugin with id {plugin_id} is not found")

	def get_all_installed_plugins_by_type(self, plugin_type:str) -> list:
		"""
		Gets all installed plugins by type\n
		"""
		return [Plugin for Plugin in self._installed_plugins.values() if Plugin.TYPE == plugin_type]

	def get_all_installed_plugins(self) -> list:
		"""
		Gets all installed plugins in the app\n
		"""
		return self._installed_plugins

	def sync_plugin(self, plugin) -> None:
		"""
		Installs the plugin\n
		"""
		self._installed_plugins[plugin.ID] = plugin
	