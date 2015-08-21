<%def name="navheader()">
    <ul class="tabs">
        <li><a href="/admin">Home</a></li>
        <li><a href="/admin/viewdump">Edit/Modify</a>
            <ul class="dropdown">
                <li><a href="/insertdata/comune">Comuni</a></li>
                <li><a href="/insertdata/statoestero">Stati esteri</a></li>
                <li><a href="/insertdata/prestazione">Prestazione</a></li>
                <li><a href="/insertdata/esenzione">Esenzioni</a></li>
                <li><a href="/insertdata/tipomedico">Tipi medico</a></li>
                <li><a href="/insertdata/onereprestazione">Oneri prestazione</a></li>
                <li><a href="/insertdata/asl">ASL</a></li>
                <li><a href="/insertdata/distretto">Distretti</a></li>
                <!--<li><a href="/insertdata/"></a></li>-->
            </ul>
        </li>
    </ul>
</%def>

${next.body()}
