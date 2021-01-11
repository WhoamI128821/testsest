from django.views.generic import TemplateView
from datetime import date


class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "Hentai"
        ctxt["sincebirth"] = date.today()-date(1990,12,8)
        return ctxt
        
    def get_days_birth(self):
        
        return age
    
class AboutView(TemplateView):
    template_name = "about.html"
    
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["sincebirth"] = date.today()-date(1990,12,8)
        ctxt["evilthings"] = [
            "Betrayals",
            "Blaming",
            "Lies",
            "Lazy",
            "Taking easy ways",
            ]
        return ctxt