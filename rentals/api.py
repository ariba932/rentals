import frappe

@frappe.whitelist()
def get_emoji():
    driverlist = frappe.db.get_all("Driver")
    return  driverlist