from uuid import uuid4
from io import StringIO

class PanelScraper():
    def __init__(self, object):
        self._object = object

    def _get_html(self):
        out = StringIO()
        self._object.save(out, embed=True)
        out.seek(0)
        return out.read().replace("'", "\'").replace('"', '\"')
    
    def _repr_html_(self):
        html = self._get_html()    
        uid = str(uuid4())       
        return f"""
<iframe id="{uid}" srcdoc='{html}' frameBorder='0'></iframe>
<script defer>
    setTimeout(() => {{
        var iframe = document.getElementById("{uid}");
        iframe.width = iframe.contentWindow.document.body.scrollWidth + 10;
        iframe.height = iframe.contentWindow.document.body.scrollHeight + 10;
    }}, 1000);
    </script>        
"""