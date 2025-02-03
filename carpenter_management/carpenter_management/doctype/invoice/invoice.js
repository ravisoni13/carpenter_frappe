// Copyright (c) 2025, ravi and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Invoice', {
//     validate: function(frm) {
//         let total_amount = 0;

//         frm.doc.furniture_item_list.forEach(i => {
//             i.amount = i.rate * i.qty * i.nos;
//             total_amount += i.amount;
//         });

//         frm.set_value('total_amount', total_amount);
//     }
// });
frappe.ui.form.on('Furniture Item Child', {
    rate: function(frm, cdt, cdn) {
        update_amount(frm, cdt, cdn);  // Update the amount when rate changes
    },
    qty: function(frm, cdt, cdn) {
        update_amount(frm, cdt, cdn);  // Update the amount when qty changes
    },
    nos: function(frm, cdt, cdn) {
        update_amount(frm, cdt, cdn);  // Update the amount when nos changes
    }
});

function update_amount(frm, cdt, cdn) {
    let row = locals[cdt][cdn];  // Get the specific row in the child table
    row.amount = row.rate * row.qty * row.nos;  // Calculate the amount for that row
    
    frm.refresh_field('furniture_item_list');  // Refresh the child table to show updated value
    calculate_total_amount(frm);  // Recalculate the total amount when the row amount is updated
}

function calculate_total_amount(frm) {
    let total_amount = 0;

    // Loop through all rows in the furniture_item_list and add their amounts
    frm.doc.furniture_item_list.forEach(function(i) {
        total_amount += i.amount;  // Sum all the amounts
    });

    frm.set_value('total_amount', total_amount);  // Set the total amount in the parent form
}




// frappe.ui.form.on('Invoice', {
//     refresh: function(frm) {
//         // Add a custom button to the form
//         frm.add_custom_button(__('Create Payment Order'), function() {
//             create_payment_order(frm);
//         });
//     }
// });

// function create_payment_order(frm) {
//     let payment_order = frappe.model.get_new_doc('Payment');
//     payment_order.client_name = frm.doc.client;  // Client Name
//     payment_order.project_name = frm.doc.project;  // Project Name
//     payment_order.balance = frm.doc.total_amount;  // Balance / Total Amount


//     frappe.set_route('Form', 'Payment', payment_order.name);
// }
frappe.ui.form.on('Invoice', {
    refresh: function(frm) {
        // Add a custom button to the form
        frm.add_custom_button(__('Create Payment Order'), function() {
            // Check if the document is saved
            if (frm.doc.__unsaved) {
                frappe.msgprint(__('Please save the invoice first.'));
                return;
            }
            create_payment_order(frm);
        });
    }
});

function create_payment_order(frm) {
    let payment_order = frappe.model.get_new_doc('Payment');
    
    // Set values from the Invoice document
    payment_order.client_name = frm.doc.client;  // Client Name
    payment_order.project_name = frm.doc.project;  // Project Name
    payment_order.balance = frm.doc.total_amount;  // Balance / Total Amount

    // Set the route to navigate to the new Payment document
    frappe.set_route('Form', 'Payment', payment_order.name);
}
