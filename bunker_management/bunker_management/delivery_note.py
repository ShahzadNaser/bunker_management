import frappe

def validate(self,method):
    frappe.msgprint("here")
    sales_order = []
    for item in self.items:
        frappe.db.set_value("Sales Order Item",item.so_detail,"qty",item.qty)
        if item.against_sales_order not in sales_order:
            sales_order.append(item.against_sales_order)
    
    for order in sales_order:
        order_doc = frappe.get_doc("Sales Order",order)
        order_doc.run_method("calculate_taxes_and_totals")
        order_doc.flags.ignore_validate_update_after_submit = True
        order_doc.save()