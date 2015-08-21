<%inherit file="/admin/admin.mako" />
<div class="generic-form">
    <div class="title">Add a dump type</div>
    ${h.form(url(controller='admin', action='adddt'), method='POST', id='frm-adddt')}
        <div class="form-row">
            <label for='type'>Type:</label>
            ${h.text('type','', autocomplete='off')}
        </div>
        <div class="genbutton">
            ${h.submit('submit','Submit','submitbutton')}
        </div>
    ${h.end_form()}
    <br />
    <div class="form-row">
        <b>Voci esistenti</b><br><br>
        % for i in c.dt:
            <div id="dt-listview-${i.id}">
                ${i.type} <img class="minus" src="/img/minus.png" onclick="delExDt(${i.id});"/> <br />
            </div>
        % endfor
    </div>
</div>
