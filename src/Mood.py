#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from weakref import WeakSet
import random

class Mood():
	instances = WeakSet()

	def __init__(self, name, jsonVal, proba=None, emoji=None):
		self.name = name
		if emoji: self.emoji = emoji.decode()
		else: self.emoji = emoji
		self.jsonVal = jsonVal
		self.proba = proba

		self.instances.add(self)

	def __str__(self):
		return f"{self.emoji} {self.name} (Json value: {self.jsonVal})" 

	@classmethod
	def random_pick(cls):
		proba = list()
		inst = list()
		for instance in cls.instances:
			proba.append(instance.proba)
			inst.append(instance)

		return random.choices(
					population=inst,
					weights=proba,
					k=1
				)[0]
			
	@classmethod
	def basic_instances(cls):
		return cls("angry", 0, 0.05, b'\xf0\x9f\x98\xa4'), \
				cls("grim", 1, 0.1, b'\xf0\x9f\x98\xac'), \
				cls("neutral", 2, 0.6, b'\xf0\x9f\x99\x82'), \
				cls("happy", 3, 0.25, b'\xf0\x9f\x99\x8c')


basic_moods = Mood.basic_instances()
