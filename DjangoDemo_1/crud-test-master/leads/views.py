from django.views.generic import TemplateView


class LeadsList(TemplateView):
    template_name = 'leads/list.html'
