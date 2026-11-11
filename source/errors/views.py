from django.views.generic import TemplateView
from branding.models import Branding

class ErrorView(TemplateView):
    template_name = 'error.html'

    def render_to_response(self, context, **response_kwargs):
        response_kwargs["status"] = context["status_code"]
        return super().render_to_response(context, **response_kwargs)

    # Accept status code from kwargs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['branding'] = Branding.objects.first()
        context['status_code'] = kwargs.get('status_code', 500)
        return context
    
    
def handler400(request, exception):
    return ErrorView.as_view()(request, status_code=400)

def handler403(request, exception):
    return ErrorView.as_view()(request, status_code=403)

def handler404(request, exception):
    return ErrorView.as_view()(request, status_code=404)

def handler500(request):
    # For 500, do NOT pass `exception`
    return ErrorView.as_view()(request, status_code=500)
