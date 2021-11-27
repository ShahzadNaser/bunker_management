# -*- coding: utf-8 -*-
# Copyright (c) 2021, Raaj Tailor	 and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.mapper import get_mapped_doc
from frappe.model.document import Document

class BunkerJobMaster(Document):
    def validate(self):
        for item in self.items:
            if not item.max:
                item.max = item.qty 
        frappe.db.set_value("Quotation",self.quotation,"bunker_job",self.name)
	# pass

@frappe.whitelist()
def create_sales_order(source_name, target_doc=None):
 
    from frappe.model.mapper import get_mapped_doc
 
    def set_missing_values(source, target):
        target.order_type = "Bunker"
    
    def update_item(obj, target, source_parent):
        target.item_name = frappe.db.get_value("Item",obj.item_code,"item_name")
        target.description = frappe.db.get_value("Item",obj.item_code,"description")
            
    doc = get_mapped_doc("Bunker Job Master", source_name,   {
        "Bunker Job Master": {
            "doctype": "Sales Order",
            "field_map": {
                "vessel_name":"vessel",
                "delivery_port":"port"
                
                
                
            }
        },
        "Bunker Cargo":{
            "doctype":"Sales Order Item",
            "postprocess": update_item
            
        }
 
    }, target_doc, set_missing_values)
   
 
    return doc