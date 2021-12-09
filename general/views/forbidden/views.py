from django.db.models.base import Model
from django.views.generic import TemplateView


class ForbiddenView(TemplateView):
    template_name = 'forbidden/forbidden.html'
