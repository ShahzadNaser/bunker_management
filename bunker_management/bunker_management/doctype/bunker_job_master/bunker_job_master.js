// Copyright (c) 2021, Raaj Tailor	 and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bunker Job Master', {
	refresh: function(frm) {
		
            cur_frm.add_custom_button(__('Sales Order'), function() {
            
                frappe.model.open_mapped_doc({
                method: "bunker_management.bunker_management.doctype.bunker_job_master.bunker_job_master.create_sales_order",
                frm: cur_frm
                })
            },__("Create"))

        

	}
});
