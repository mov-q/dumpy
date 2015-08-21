function deleteStatusDump(id) {
    $.ajax({
        type: "POST",
        url: "/admin/delstatusdump",
        data: "id="+id,
        success: function(){
            $('#sd-modview-'+id).remove();
        }
    });
};

function deleteAgentDump(id) {
    $.ajax({
        type: "POST",
        url: "/admin/delagentdump",
        data: "id="+id,
        success: function(){
            $('#ag-modview-'+id).remove();
        }
    });
};

function deleteReallocation(id) {
    $.ajax({
        type: "POST",
        url: "/admin/delreallocation",
        data: "id="+id,
        success: function(){
            $('#dt-modview-'+id).remove();
        }
    });
};

function deleteQuantity(id) {
    $.ajax({
        type: "POST",
        url: "/admin/delquantity",
        data: "id="+id,
        success: function(){
            $('#qty-modview-'+id).remove();
        }
    });
};

function deleteCerDump(id) {
    $.ajax({
        type: "POST",
        url: "/admin/delcerdump",
        data: "id="+id,
        success: function(){
            $('#cer-modview-'+id).remove();
        }
    });
};

function deleteBibDump(id) {
    $.ajax({
        type: "POST",
        url: "/admin/delbibdump",
        data: "id="+id,
        success: function(){
            $('#bib-modview-'+id).remove();
        }
    });
};

function destroyDump(id) {
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
                    url: "/admin/destroydump",
                    data: "id="+id,
                    success: function(){
                        $('#dumpview-'+id).remove();
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
