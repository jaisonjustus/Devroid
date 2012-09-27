import os;
import json;

class Settings:

	def __init__(self):
		# Settings attributes
		self.settings_path = ''
		self.android_target_versions = {}

		# Settings filename
		self.settings_file_name = {
			"android-versions" : "android-versions.json"
		}

		self.get_settings_folder_path()
		self.fetch_application_settings("android-versions")

	def get_settings_folder_path(self):
		self.settings_path = os.path.abspath('settings')

	def fetch_application_settings(self,filename):
		json_file_path = os.path.join(self.settings_path, self.settings_file_name[filename])
		json_file_data = open(json_file_path).read()
		json_data = json.loads(json_file_data)

		if filename == "android-versions":
			self.prepare_android_version_settings(json_data)
		else:
			print "Invalid File"

	def prepare_android_version_settings(self, json_data):
		for version in json_data:
			self.android_target_versions[version["name"]] = version["target"]
