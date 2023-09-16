from uuid import uuid4
from io import StringIO
from html import escape

class PanelScraper():
    def __init__(self, object):
        self._object = object

    def _get_html(self):
        out = StringIO()
        self._object.save(out, embed=True)
        out.seek(0)
        return escape(out.read())
    
    def _repr_html_(self):
        html = self._get_html()    
        uid = str(uuid4())       
        return f"""
<script>
function resizeIframe(){{
    setTimeout(() => {{
        var iframe = document.getElementById("{uid}");
        iframe.width = iframe.contentWindow.document.body.scrollWidth + 10;
        iframe.height = iframe.contentWindow.document.body.scrollHeight + 10;    
    }}, "10");
    
}}
</script>        
<iframe id="{uid}" srcdoc='{html}' frameBorder='0' onload='resizeIframe(this)'></iframe>
"""