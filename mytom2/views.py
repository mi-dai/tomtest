from django.views.generic import TemplateView
from tom_targets.models import Target

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        return {'targets': Target.objects.all()}


class DetailView(TemplateView):
    template_name = 'target_detail.html'

    def get_context_data(self, pk, **kwargs):
        target = Target.objects.get(id=pk)
        return {'target': target}