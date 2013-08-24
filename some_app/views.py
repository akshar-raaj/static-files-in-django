from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'some_app/home.html'
