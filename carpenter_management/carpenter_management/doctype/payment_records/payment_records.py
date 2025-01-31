# Copyright (c) 2025, ravi and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PaymentRecords(Document):
    
    def before_save(self): 
        self.payment_validate()
        self.balance_amount_calculate()
        self.balance_zero()
        
    def payment_validate(self):
        total_amount = 0  
        
        for pay in self.payment_installments:
            total_amount += pay.amount_paid or 0  
        
        self.total_amount_paid = total_amount  
    
    def balance_amount_calculate(self):
        self.balance_amount =  self.total_invoice_amount - self.total_amount_paid      

    def balance_zero(self):
        if self.balance_amount == 0:
            frappe.db.set_value("Project Details", self.project, "status", "Completed")
            frappe.msgprint("Project Payment Completed ") 
            