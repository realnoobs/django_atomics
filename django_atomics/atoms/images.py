from django_atomics.component import Component


class Img(Component):
    template_string = """
    <img {{ attrs }}
         src="{{ url }}"
         {% if width %} width={{ width }}{% endif %}
         {% if height %} height={{ height }}{% endif %}
         class="{{ classes }}"
         alt="{{ alt }}"/>
    """
