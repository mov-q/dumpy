<%inherit file="/admin/admin.mako" />
<div class="generic-form">
    <div class="title">Add a status</div>
    ${h.form(url(controller='admin', action='addstatus'), method='POST', id='frm-addstatus')}
        <div class="form-row">
            <label for='status'>Status:</label>
            ${h.text('status','', autocomplete='off')}
        </div>
        <div class="genbutton">
            ${h.submit('submit','Submit','submitbutton')}
        </div>
    ${h.end_form()}
    <br />
    <div class="form-row">
        <b>Voci esistenti</b><br><br>
        % for i in c.s:
            <div id="st-listview-${i.id}">
                ${i.description} <img class="minus" src="/img/minus.png" onclick="delExStatus(${i.id});"/> <br />
            </div>
        % endfor
    </div>
</div>
