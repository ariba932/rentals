import frappe
import random

def get_driver_random():
		try:
			driver_names = frappe.get_list("Driver", fields=["name"], as_list=True)
			if not driver_names:
				frappe.logger("No Driver Information available")
				return None
			driver_names_flat = [item[0] for item in driver_names]
			return driver_names_flat
		except frappe.DoesNotExistError:
			frappe.logger("Driver not found )this should not happen).")
			return None
		except Exception as e:
			frappe.logger(f"An error occurred: {e}")
			return None


def execute():
	driver_list = get_driver_random()
	#random_driver = random.choice(driver_list)
	vehicles = frappe.db.sql("select name from tabVehicle", pluck="name")
	for v in vehicles:
		vehicle = frappe.get_doc("Vehicle",v)
		vehicle.set_driver(random.choice(driver_list))
		vehicle.save()
        
	frappe.db.commit()