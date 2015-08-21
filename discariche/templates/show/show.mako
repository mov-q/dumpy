<%inherit file="/public.mako" />
<%def name="css_jscript()">
    ${parent.css_jscript()}
    ${h.javascript_link('http://maps.google.com/maps/api/js?sensor=true')}
    ${h.javascript_link('/js/show.js')}
</%def>
${next.body()}
