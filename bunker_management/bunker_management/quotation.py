from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def create_bunker_job(source_name, target_doc=None):
 
    from frappe.model.mapper import get_mapped_doc
 
    def set_missing_values(source, target):
        pass
    
    def update_item(obj, target, source_parent):
        pass
            
    doc = get_mapped_doc("Quotation", source_name,   {
        "Quotation": {
            "doctype": "Bunker Job Master",
            "field_map": {
                "party_name":"customer",
                "vessel":"vessel_name",
                "eta_date":"issue_date",
                "etd_date":"delivery_date",
                "name":"quotation"
                
                
            }
        },
        "Quotation Item":{
            "doctype":"Bunker Cargo",
            "qty":"max"
        }
 
    }, target_doc, set_missing_values)
   
 
    return doc