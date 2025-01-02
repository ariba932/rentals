# Copyright (c) 2024, MKO - Tevc Space and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def validate(self):
		if not self.rate:
			frappe.throw("Please provide a rate")
		sum=0
		for item in self.items:
			sum+=item.distance*self.rate
		self.total_amount = sum
