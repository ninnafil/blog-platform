from django.views.generic import TemplateView


# Create your views here.

class About(TemplateView):
    """Страница 'О проекте'"""
    template_name = 'pages/about.html'


class Rules(TemplateView):
    """Страница 'Правила'"""
    template_name = 'pages/rules.html'
