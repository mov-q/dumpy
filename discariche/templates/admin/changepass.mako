<%inherit file="/admin/admin.mako" />
<div class="generic-form">
    <div class="title">Password change</div>
    ${h.form(url(controller='admin', action='changepass'), method='POST')}
        <div class="form-row">
            <label for='username'>Username:</label>
            ${h.text('username','', autocomplete='off')}
        </div>
        <div class="form-row">
            <label for='curpass'>Current password:</label>
            ${h.password('curpass','', autocomplete='off')}
        </div>
        <div class="form-row">
            <label for='newpassa'>New password:</label>
            ${h.password('newpassa','', autocomplete='off')}
        </div>
        <div class="form-row">
            <label for='curpass'>Retype new password:</label>
            ${h.password('newpassb','', autocomplete='off')}
        </div>
        <div class="genbutton">
            ${h.submit('submit','Submit','submitbutton')}
        </div>
    ${h.end_form()}
</div>
