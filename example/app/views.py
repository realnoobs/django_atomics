from django.views.generic import TemplateView
from .components.sidebar import sidebar


class IndexPage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        kwargs.update(
            {
                "sidebar": sidebar,
            }
        )
        return super().get_context_data(**kwargs)
