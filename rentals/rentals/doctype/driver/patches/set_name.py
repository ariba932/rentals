import frappe

def execute():
    drivers = frappe.db.get_all("Driver", pluck="name")
    for v in drivers:
        driver = frappe.get_doc("Driver",v)
        driver.set_name()
        driver.save()  

    frappe.db.commit()
