<%inherit file="/u-menu.mako" />
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html>
<head>
    <title></title>
    ${self.css_jscript()}
        <meta property="og:title" content="La mappa dei rifiuti in Campania"/>
        <meta property="og:type" content="website"/>
        <meta property="og:url" content="http://www.munnezza.info"/>
        <meta property="og:image" content="http://www.munnezza.info/img/munlogo_0.png"/>
        <meta property="og:site_name" content="munnezza.info"/>
        <meta property="fb:admins" content="munnezza.info"/>
        <meta property="og:description" content="Il problema dei rifiuti in Campania è un'emergenza cronica. A nostro parere, la diffusione delle informazioni su vasta scala, la consapevolezza e la partecipazione sono un requisito fondamentale per qualsiasi approccio alla soluzione del problema. In quest'ottica, il progetto munnezza.info si propone di mappare tutti i siti che sono stati destinati al conferimento, al trattamento e al deposito dei rifiuti. "/>
</head>
    <%def name="css_jscript()">
        ${h.stylesheet_link('/css/publicnew.css')}
        ${h.stylesheet_link('/css/ui-lightness/jquery-ui-1.8.5.custom.css')}
        ${h.javascript_link('/js/jquery-1.4.2.min.js')}
        ${h.javascript_link('/js/jquery-ui-1.8.5.custom.min.js')}
        ${h.javascript_link('/js/jquery.mousewheel.js')}
        ${h.javascript_link('/js/jquery.smoothDivScroll-1.1-min.js')}
        ${h.javascript_link('/js/jquery.pagination.js')}
        ${h.javascript_link('/js/jquery.validate.min.js')}
        ${h.javascript_link('/js/jquery.form.js')}
        ${h.javascript_link('http://maps.google.com/maps/api/js?sensor=true')}
        ${h.javascript_link('/js/shownew.js')}
    </%def>
<body>
    <div id="menu">
        <div id="menu-entries">
            <div class="menu-item" onclick="resetMap();">
                home
            </div>
            <div class="menu-item" onclick="showHomeOlay();">
                about
            </div>
            <div class="menu-item" onclick="showContactOlay();">
                contacts
            </div>
        </div>
    </div>
    <div id="show-home">
        <div id="logo-home">
            <img src="/img/munlogo_0.png" alt="munnezza logo"/>
        </div>
        <div id="home-text">
            <b>Perchè questo progetto?</b> <br />
            <p>
            Il problema dei rifiuti in Campania è ormai una emergenza cronica. A
            nostro parere, la diffusione delle informazioni su vasta scala, la
            consapevolezza e la partecipazione sono un requisito fondamentale per
            qualsiasi approccio alla soluzione del problema.
            In quest'ottica, il progetto munnezza.info si propone di mappare tutti
            i siti che sono stati destinati al conferimento, al trattamento e al
            deposito dei rifiuti.
            </p>
            <b>Come si usa?</b> <br />
            <p>
            Naviga la mappa.<br />
            Cliccando su un segnaposto, ottieni uno zoom della mappa sul luogo
            selezionato e visulizzi la relativa scheda informatica. Le schede informazione
            possono essere chiuse in qualsiasi momento cliccando sull apposita icona
            o utilizzando il tasto "Esc".<br />
            Cliccando su un segnaposto col tasto destro, visualizzi le info senza zoomare
            sul luogo prescelto.<br />
            Ove disponibile, prova la funzione StreetView delle mappe di Google per
            visualizzare riprese fotografiche ravvicinate dal livello stradale.
            </p>
            Questo sito è ottimizzato per qualunque browser che NON sia  
            Internet Explorer (ovvero presenta problemi di visualizzazione con IE)
        </div>
    </div>
    <div id="show-contact">
        <div id="logo-home">
            <img src="/img/munlogo_0.png" alt="munnezza logo"/>
        </div>
        <div id="contact-text">
            Per segnalazioni, suggerimenti, collaborazioni, scrivici a
            munnezza.info@gmail.com
        </div>
    </div>
    <div id="show-info">
        <div id="show-left">
            <div id="geninfo">
            </div>
            <div id="cer">
            </div>
            <div id="status">
            </div>
            <div id="dest">
            </div>
            <div id="agent">
            </div>
            <div id="qty">
            </div>
            <div id="biblio">
            </div>
        </div>
        <div id="show-right">
            <div id="card-header">
                <div id="card-title">
                </div>
                <div id="card-close">
                    <img src="/img/close-button.png" width="25" height="25" onclick="hideAllOlay();"/>
                </div>
            </div>
            <div id="card-subtitle">
            </div>
            <div id="card-history">
            </div>
        </div>
    </div>
    <div id="map-container">
    </div>
    <script type="text/javascript">
        initialize();
    </script>
<!-- Piwik -->
<script type="text/javascript">
var pkBaseURL = (("https:" == document.location.protocol) ? "https://munnezza.info/piwik/" : "http://munnezza.info/piwik/");
document.write(unescape("%3Cscript src='" + pkBaseURL + "piwik.js' type='text/javascript'%3E%3C/script%3E"));
</script><script type="text/javascript">
try {
var piwikTracker = Piwik.getTracker(pkBaseURL + "piwik.php", 1);
piwikTracker.trackPageView();
piwikTracker.enableLinkTracking();
} catch( err ) {}
</script><noscript><p><img src="http://munnezza.info/piwik/piwik.php?idsite=1" style="border:0" alt="" /></p></noscript>
<!-- End Piwik Tag -->
</body>
</html>
