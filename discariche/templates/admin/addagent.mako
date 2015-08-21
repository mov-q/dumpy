<%inherit file="/admin/admin.mako" />
<div class="generic-form">
    <div class="title">Add an agent</div>
    ${h.form(url(controller='admin', action='addagent'), method='POST', id='frm-addagent')}
        <div class="form-row">
            <label for='agent'>Agent:</label>
            ${h.text('agent','', autocomplete='off')}
        </div>
        <div class="genbutton">
            ${h.submit('submit','Submit','submitbutton')}
        </div>
    ${h.end_form()}
    <br />
    <div class="form-row">
        <b>Voci esistenti</b><br><br>
        % for i in c.a:
            <div id="ag-listview-${i.id}">
                ${i.name} <img class="minus" src="/img/minus.png" onclick="delExAgent(${i.id});"/> <br />
            </div>
        % endfor
    </div>
</div>
