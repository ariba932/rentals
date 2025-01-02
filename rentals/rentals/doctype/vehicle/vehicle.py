# Copyright (c) 2024, KOM and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
import random


class Vehicle(WebsiteGenerator):
	def before_save(self):
		self.vehicle_info = f"{self.make}/{self.model}"


	def set_driver(self, name):
		if not name:
			frappe.throw("Driver name cannot be empty")
	
		self.driver_name = name

