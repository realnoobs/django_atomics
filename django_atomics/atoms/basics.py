from django_atomics.base import Component


class NoTag(Component):
    template_string = """{{ childs }}"""


class Tag(Component):
    template_string = """<{{ tag }}>{{ text|safe }}</{{ tag }}>"""


class Content(Component):
    template_string = """{{ value|safe }}"""


class Paragraph(Component):
    template_string = """<p>{{ text|safe }}</p>"""


class Icon(Component):
    template_string = """<i {{ attrs }} class="{{ classes }}" href="{{ url }}"></i> """


class MaterialIcon(Icon):
    template_string = """<i {{ attrs }} class="mdi mdi-{{ name }} {{ classes}}""></i> """


class BoostrapIcon(Icon):
    template_string = """<i {{ attrs }} class="bi bi-{{ name }} {{ classes}}"></i> """


class FontAwesomeIcon(Icon):
    template_string = """<i {{ attrs }} class="fa fa-{{ name }} {{ classes}}"></i> """


class Link(Component):
    template_string = """
    <a {{ attrs }}
         {% if style %}style="{{ style }}"{% endif %}
         {% if classes %}class="{{ classes }}"{% endif %}
         href="{{ url }}"
        >{{ childs }}{{ label }}</a>
    """


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


__all__ = [
    "Content",
    "Paragraph",
    "Icon",
    "MaterialIcon",
    "BoostrapIcon",
    "FontAwesomeIcon",
    "Link",
    "Button",
    "ButtonLink",
]
