from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

@frappe.whitelist(allow_guest=True)
def sendmail_gstr3B():
	for customer in frappe.db.get_list('Customer', {'send_gstr_3b_alert': 1}, ['customer_name','email_id']):
		content = "<h4>Dear Sir/Mam,</h4>"
		content += "<p>Greetings from FinBridge Consulting.....</p>"
		content += "<p>You are requested to submit your sales, purchase & expense data of the previous month for filing GSTR 3B due soon.</p>"
		content += "<p>Please submit your data on or before the 16th to avoid interest and late fees.</p>"
		content += "<p>If you have any questions, feel free to write to us at <b>office@finbridge.co.in.</b></p>"
		content += "<p><b>Thanks & Regards,</b><br>Support Team<br>FinBridge Consulting</p>"
		content += "<p>Note : This is an auto-generated email, please ignore if you have already submitted the data.</p>"
		frappe.sendmail(recipients=str(customer.email_id),cc="ketan@finbridge.co.in",
		subject="Alert : GSTR-3B Filing", content=content)


@frappe.whitelist(allow_guest=True)
def sendmail_gstr1():
	for customer in frappe.db.get_list('Customer', {'send_gstr_1_alert': 1}, ['customer_name','email_id']):
		content = "<h4>Dear Sir/Mam,</h4>"
		content += "<p>Greetings from FinBridge Consulting.....</p>"
		content += "<p>You are requested to submit your sales data of the previous month for filing GSTR-1 due soon.</p>"
		content += "<p>Please submit your data on or before the 8th to avoid interest and late fees.</p>"
		content += "<p>If you have any questions, feel free to write to us at <b>office@finbridge.co.in.</b></p>"
		content += "<p><b>Thanks & Regards,</b><br>Support Team<br>FinBridge Consulting</p>"
		content += "<p>Note : This is an auto-generated email, please ignore if you have already submitted the data.</p>"
		frappe.sendmail(recipients=str(customer.email_id),cc="ketan@finbridge.co.in",
		subject="Alert : GSTR-1 Filing", content=content)


@frappe.whitelist(allow_guest=True)
def revert_customer():
	frappe.db.sql("""update `tabCustomer` set send_gstr_1_alert = 1, send_gstr_3b_alert = 1""")
	frappe.db.commit()
