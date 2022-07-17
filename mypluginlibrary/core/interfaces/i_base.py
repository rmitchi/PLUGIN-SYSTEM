# Author - Karan Parmar

"""
Base inteface
- log
"""

from ...components import LogManager

class IBase:

	def log(self, log_type:str, message:str) -> None:
		"""
		Log the data\n
		"""
		LogManager.log(log_type=log_type, message=message)