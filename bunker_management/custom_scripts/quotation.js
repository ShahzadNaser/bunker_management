frappe.ui.form.on('Quotation', {
    refresh: function(frm) {
        console.log("here")
        if(frm.doc.docstatus == 1 && frm.doc.order_type == "Bunker" && !frm.doc.bunker_job){
            cur_frm.add_custom_button(__('Bunker Job'), function() {
            
                frappe.model.open_mapped_doc({
                method: "bunker_management.bunker_management.quotation.create_bunker_job",
                frm: cur_frm
                })
            },__("Create"))

        }
        
    },

})