#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
from getpass import getpass

try:
	import dotenv
except ModuleNotFoundError:
	print(
"""Missing dependencies. Run:
pip install -r requirements.txt"""
	)
	exit(1)


class Config():
	def __init__(self, saveDir):

		self.file = os.path.join(saveDir, ".env")
		dotenv.load_dotenv(self.file)

		# NikoNiko config
		self.endpoint = self._get_env("illuca_endpoint", safe=False)
		self.username = self._get_env("illuca_username", safe=False)
		self.password = self._get_env("illuca_password", safe=True)


	def _get_env(self, name, safe=False):
		if name in os.environ:
			return os.environ.get(name)
		else:
			return self._set_env(name, safe)

	def _set_env(self, name, safe=False):
		if not safe:
			val = input(f"Input value for {name}:\n")
		else:
			val = getpass(f"Input value for {name}:\nWill be save in plain-text\n")
		with open(self.file, "a") as f:
			f.write(f"{name}={val}\n")
		os.environ[name] = str(val)

		return val


