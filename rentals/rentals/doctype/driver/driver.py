# Copyright (c) 2024, KOM and contributors
# For license information, please see license.txt

# import frappe
#from typing import Self
from frappe.website.website_generator import WebsiteGenerator


class Driver(WebsiteGenerator):
	def before_save(self):
		self.full_name = f"{self.first_name} {self.last_name}"

	def send_alert(self):
		print("send message")

	def set_name(self):
		self.full_name = f"{self.first_name} {self.last_name}"
