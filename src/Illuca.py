#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import requests
import re


class Illuca():

	def __init__(self, url, failedDir):
		self.url = url
		self.failedDir = self._set_failed_dir(failedDir)
		self.session = None

	def _set_failed_dir(self, failedDir):
		if not os.path.exists(failedDir):
			os.mkdir(failedDir)

		return failedDir

	def connect(self, username, password):
		print(f"Connecting to {self.url}...")
		# reset or set the session
		self.session = requests.Session()

		# grap the login page to fetch the CSRF token
		homePageResponse = self.session.get(self.url)
		if homePageResponse.status_code != 200:
			with open(os.path.join(self.failedDir, "failed.html"), "wb") as f:
				f.write(homePageResponse.content)
			print(f"Failed to get the home page. Status code {homePageResponse.status_code}")
			return False

		# Fetch the CSRF token
		homePageContent = homePageResponse.content
		regexToken = re.compile("<input name=\"__RequestVerificationToken\" type=\"hidden\" value=\"([a-zA-Z0-9_-]*)")
		token = regexToken.search(str(homePageContent)).group(1)
		if token == '':
			print("Failed to fetch the CSRF token")
			with open(os.path.join(self.failedDir, "failed.html"), "wb") as f:
				f.write(homePageResponse.content)
			return False

		# login
		payload = {
			"ReturnUrl":None,
			"UserName":username,
			"Password":password,
			"IsPersistent":"false",
			"__RequestVerificationToken": token
		}
		conn = self.session.post(self.url + "/identity/login", data=payload)
		if conn.status_code != 200:
			print(f"Failed to connect. Status code: {conn.status_code}")
			with open(os.path.join(self.failedDir, "failed.html"), "wb") as f:
				f.write(conn.content)
			return False

		return True

	def is_connected(self):
		return self.session is not None

	def __str__(self):
		return f"Illuca object for {self.url}. Connected: {self.is_connected()}"
