$(document).ready(function(){
    $("#frm-addstatus").validate({
        // we could add rules here
        submitHandler: function(form){
            jQuery(form).ajaxSubmit({
                target: '#resbox',
            });
            // clear fields after submit 
            $(form).clearForm();
        }
    });
});

function delExStatus(id) {
    delstr = 'Vuoi davvero eliminare questo elemento?';
    var $dial =  $('<div></div>').html(delstr).dialog({
        autoOpen: false,
        resizable: false,
        height: 250,
        modal: true,
        buttons: {
            'Elimina': function() {
                $.ajax({
                    type: "POST",
                    url: "/admin/delexstatus",
                    data: "id="+id,
                    success: function(){
                        $('#st-listview-'+id).remove();
                    }
                });
                $(this).dialog('close');
            },
            'Annulla': function() {
                $(this).dialog('close');
            }
        }
    });

    $dial.dialog('open');
    return false;
};
