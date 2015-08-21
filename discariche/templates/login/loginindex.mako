<%inherit file="/login/login.mako" />
<div class="generic-form"> 
    ${h.form(url(controller='login', action='submit'), method='POST')}
        <div class="form-row">
            <label for='user'>Username:</label>
            ${h.text('username','', autocomplete='off')}
        </div>
        <div class="form-row">
            <label for='password'>Password:</label>
            ${h.password('password','', autocomplete='off')} <br />
        <div class="genbutton">
            ${h.submit('submit','Submit','submitbutton')}
        </div>
    ${h.end_form()}
</div>
