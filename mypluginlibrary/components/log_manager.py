# Author - Karan Parmar

"""
Log manager - manages logs
"""

# Importing built-in libraries
import os, pytz
from datetime import datetime

# Importing third-party libraries
import pandas as pd

class LOG_TYPE:

	STARTED = "STARTED"
	STOPPED = "STOPPED"
	SHUTDOWN = "SHUTDOWN"
	INFO = "INFO"
	NULL = ""
	SUCCESS = "SUCCESS"
	UPDATE = "UPDATE"
	ERROR = "ERROR"

	OPENED = "OPENED"
	CLOSED = "CLOSED"

class LogManager:

	_logs_directory = os.getcwd()
	_timezone = "UTC"
	_logs_file_name = datetime.now(pytz.timezone(_timezone)).strftime("%Y-%m-%d") + '.csv'
	_log_columns = ['datetime', 'log_type', 'log']

	# Public methods
	@staticmethod
	def initialize() -> None:
		"""
		Initialize the log manager\n
		"""
		os.makedirs(LogManager._logs_directory, exist_ok=True)
		log_file_path = os.path.join(LogManager._logs_directory, LogManager._logs_file_name)
		if not os.path.exists(log_file_path):
			df = pd.DataFrame(columns=LogManager._log_columns)
			df.to_csv(log_file_path, index=None)

	@staticmethod
	def set_logs_directory(logs_directory_path:str) -> None:
		"""
		Sets logs directory path\n
		"""
		LogManager._logs_directory = logs_directory_path

	@staticmethod
	def set_logs_file_name(logs_file_name:str) -> None:
		"""
		Sets logs file name\n
		"""
		LogManager._logs_file_name = logs_file_name

	@staticmethod
	def set_timezone(timezone:str) -> None:
		"""
		Set log timezone\n
		"""
		LogManager._timezone = timezone

	@staticmethod
	def log(log_type:str, message:str) -> None:
		"""
		Log the data\n
		"""
		current_datetime = str(datetime.now(pytz.timezone(LogManager._timezone)))

		if log_type not in [LOG_TYPE.NULL]:
			print(f"{current_datetime} {log_type:<10s} {message}")

		# NOTE Adding log entry
		log_file_path = os.path.join(LogManager._logs_directory, LogManager._logs_file_name)
		signal = {k:v for k, v in zip(LogManager._log_columns, [current_datetime, log_type, message])}
		df = pd.DataFrame([signal], index=None)
		df.to_csv(log_file_path, mode='a', index=False, header=False)
