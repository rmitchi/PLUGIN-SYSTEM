# Author - Karan Parmar

from mypluginlibrary import App
from mypluginlibrary.utils.functions.io import read_json_file

def main(debug:bool=False):
	
	CREDENTIALS_PATH = "credentials.json"
	CONFIG_PATH = "config.json"
	APP_CONFIG_PATH = "app_config.json"

	credentials = read_json_file(file_path=CREDENTIALS_PATH)
	config = read_json_file(file_path=CONFIG_PATH)
	app_config = read_json_file(file_path=APP_CONFIG_PATH)

	app = App(credentials=credentials, config=config, app_config=app_config)
	app.run()

if __name__ == "__main__":
	main(debug=True)