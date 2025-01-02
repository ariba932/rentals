// Copyright (c) 2024, MKO - Tevc Space and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
 	refresh(frm) {
        frm.add_custom_button("Accept K", ()=> { 
            frm.save();
            console.log("now I saved it using JS");
    })

   	},
    
    rate(frm)
    {
        //recaculate total
       frm.trigger("update_total_amount");
    },

    update_total_amount(frm)
    {
        let sum=0;
        for (let item of frm.doc.items)
        {
            sum+=frm.doc.rate*item.distance;
        }
        frm.set_value("total_amount", sum);
    }
 });

 
frappe.ui.form.on("Ride Booking Item", {
    refresh(frm) {
    },
    //track changes on distance
    distance(frm) {
        frm.trigger("update_total_amount");
    },
    //track changes when item is remove
    items_remove(frm){
        frm.trigger("update_total_amount");
    },
//while (condition) {

  //      items_add(frm){
   //         frm.trigger("update_total_amount");
  //      }

});