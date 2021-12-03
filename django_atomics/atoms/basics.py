from django_atomics.component import Component


class Content(Component):
    template_string = """{{ value|safe }}"""


class Paragraph(Component):
    template_string = """<p>{{ text|safe }}</p>"""


class Icon(Component):
    template_string = """<i {{ attrs }} class="{{ classes }}" href="{{ url }}"></i> """


class MaterialIcon(Icon):
    template_string = """<i {{ attrs }} class="mdi mdi-{{ name }} {{ classes}}" href="{{ url }}"></i> """


class BoostrapIcon(Icon):
    template_string = """<i {{ attrs }} class="bi bi-{{ name }} {{ classes}}" href="{{ url }}"></i> """


class FontAwesomeIcon(Icon):
    template_string = """<i {{ attrs }} class="fa fa-{{ name }} {{ classes}}" href="{{ url }}"></i> """


class Link(Component):
    template_string = """<a {{ attrs }} class="{{ classes}}" href="{{ url }}">{{ label }}</a> """


class Button(Component):
    template_string = """
    <button {{ attrs }} class="{{ classes}}"
            type="{{ type }}" {% if action %}formaction="{{ action }}"{% endif %}>
            {{ label }}
    </button>
    """


class ButtonLink(Component):
    template_string = """
    <a href="{{ url }}" class="btn btn{{ variant }}" target="{{ target }}" >{{ text }}</a>
    """
