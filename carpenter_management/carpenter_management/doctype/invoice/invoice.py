# Copyright (c) 2025, ravi and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import date_diff,today,getdate,datetime


class Invoice(Document):
    
    # def before_save(self):
    #     self.calculate_all()
        
    def validate(self):
        total_amount = 0
        for i in self.furniture_item_list: 
            i.amount =  i.rate  * i.qty * i.nos
            total_amount += i.amount
                
        self.total_amount =  total_amount    
    
    
    
    
    # def before_save(self):
    #     self.furniture_calculate_list()
    #     self.calculate_totals()
    #     self.rental_expense_calculate()
    # def furniture_calculate_list(self):
    #     toal_furniture_cost = 0
    #     for item in self.furniture_item_list:
    #         item.amount =  item.unit_price * item.quantity
    #         toal_furniture_cost += item.amount
    #     self.total_furniture_cost =  toal_furniture_cost
    
    # def final_amount_calculate(self):
    #     self.final_amount =  self.total_raw_material_price  + self.total_furniture_cost  + self.total_rental_machine_cost
    
    # def rental_expense_calculate(self):
    #     total_rent_cost = 0
    #     for rent in self.rental_expense:
    #         date1 = getdate(rent.rental_start_date)  
    #         date2 = getdate(rent.rental_end_date)
    #         days_int = date_diff(date2, date1)+ 1
            
    #         rent.total_days =  int(days_int)
            
    #         days =  rent.total_days
    #         qty = rent.qyt or 0
    #         daily_rent = rent.daily_rent or 0
            
    #         rent.total_rental_cost =  days * qty * daily_rent
    #         total_rent_cost += rent.total_rental_cost
    #     self.total_rental_machine_cost = total_rent_cost  
    # def calculate_totals(self):
    #     total_rent_cost = 0
    #     for rent in self.rental_expense:
    #         date1 = getdate(rent.rental_start_date)  
    #         date2 = getdate(rent.rental_end_date)
    #         rent.total_days = int(date_diff(date2, date1) + 1)  # Ensure integer value
    #         qty = rent.qyt or 0
    #         daily_rent = rent.daily_rent or 0

    #         rent.total_rental_cost = rent.total_days * qty * daily_rent
    #         total_rent_cost += rent.total_rental_cost  # Accumulate total rental cost

    #     self.total_rental_machine_cost = total_rent_cost

    #     raw_material_price = self.total_raw_material_price
    #     furniture_cost = self.total_furniture_cost 
    #     rental_machine_cost = self.total_rental_machine_cost 

    #     self.final_amount = raw_material_price + furniture_cost + rental_machine_cost
    
    # # def on_submit(self):
    # #     if self.estimate_date:
    # #         self.estimate_date = frappe.utils.today()
    # #         self.save()