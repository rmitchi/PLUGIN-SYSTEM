# Author - Karan Parmar

"""
IO related functions
"""

# Importing built-in libraries
import json
import pickle

# JSON io related functions
def read_json_file(file_path:str, mode:str='r') -> dict:
	"""
	Reads json file and parse it to python object\n
	"""
	with open(file_path, mode) as f:
		data = json.load(f)
		f.close()
	return data

def write_json_file(data:dict, file_path:str, mode:str='w') -> None:
	"""
	Writes json file and parse it to python object\n
	"""
	with open(file_path, mode) as f:
		json.dump(data, f)
		f.close()

# Pickle io related functions
def read_pickle_file(file_path:str, mode:str='rb') -> object:
	"""
	Reads python object by deserializing it\n
	"""
	with open(file_path, mode) as f:
		obj = pickle.load(f)
		f.close()
	return obj

def write_pickle_file(obj:object, file_path:str, mode:str='wb') -> None:
	"""
	Writes pickle serialized file and parse it to python object\n
	"""
	with open(file_path, mode) as f:
		pickle.dump(obj, f)
		f.close()