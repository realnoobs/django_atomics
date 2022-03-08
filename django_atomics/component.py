from copy import copy
from functools import cached_property

from django.forms.widgets import MediaDefiningClass
from django.utils.safestring import mark_safe

from .renderers import get_default_renderer
from .utils import construct_template_name, flatatt, flatstyle


class NotComponent(Exception):
    pass


class InvalidComponentTemplate(Exception):
    pass


class BaseComponent:

    template_string = None
    renderer_class = None

    def __init__(self, **context):
        # classes=None, attrs=None, style=None, childs=None,
        self.attrs = self.build_attrs(context.pop("attrs", dict()))
        self.classes = self.build_classes(context.pop("classes", list()))
        self.childs = self.build_childs(context.pop("childs", None))
        self.style = self.build_style(context.pop("style", dict()))
        self.context = self.build_context_data(context)

    def __str__(self):
        return str(self.__class__)

    def __repr__(self):
        return "<%(cls)s childs=(%(childs)s)>" % {
            "cls": self.__class__.__name__,
            "childs": ";".join(self.childs),
        }

    def __getitem__(self, index):
        try:
            return self.childs[index]
        except KeyError:
            raise KeyError(
                "Key '%s' not found in '%s'. Choices are: %s."
                % (
                    index,
                    self.__class__.__name__,
                    ", ".join(sorted(self.childs)),
                )
            )

    @cached_property
    def renderer(self):
        renderer = self.get_renderer()
        return renderer

    def get_renderer(self):
        return self.renderer_class or get_default_renderer()

    def build_classes(self, classes):
        if classes is None:
            classes = []
        elif isinstance(classes, list):
            classes = classes.copy()
        elif isinstance(classes, str):
            classes = classes.split(" ")
        else:
            raise ValueError("%s is not valid valid classes." % classes)
        return classes

    def get_classes(self, extra_classes=None):
        new_classes = self.build_classes(extra_classes)
        return " ".join(self.classes + new_classes)

    def build_attrs(self, attrs):
        if attrs is None:
            attrs = {}
        elif not isinstance(attrs, dict):
            raise ValueError("%s is not valid valid attrs." % type(attrs))
        else:
            pass
        return attrs

    def get_attrs(self, extra_attrs=None):
        """Build an attribute dictionary."""
        extra = self.build_attrs(extra_attrs)
        attrs = {**self.attrs, **extra}
        return flatatt(attrs)

    def build_style(self, style):
        if style is None:
            style = {}
        elif not isinstance(style, dict):
            raise ValueError("%s is not valid valid style." % type(style))
        else:
            pass
        return style

    def get_style(self, extra_style=None):
        """Build an attribute dictionary."""
        extra = self.build_attrs(extra_style)
        attrs = {**self.style, **extra}
        return flatstyle(attrs)

    def build_childs(self, childs):
        if childs is None:
            _childs = []
        elif isinstance(childs, BaseComponent):
            _childs = [childs]
        elif isinstance(childs, (tuple, list)):
            _childs = list(childs)
        else:
            raise ValueError("%s is not valid childs argument type." % type(childs))
        for child in _childs:
            assert isinstance(child, BaseComponent), (
                "childs item %s must be an instance of Component class " % child
            )
        return _childs

    def get_childs(self, parent_context):
        rendered_childs = ""
        for child in self.childs:
            rendered_childs += child.render(context=parent_context)
        return mark_safe(rendered_childs)

    def build_context_data(self, context):
        if context is None:
            context = {}
        elif not isinstance(context, dict):
            raise ValueError("%s is not valid valid context dict." % context)
        else:
            pass
        return context

    def get_context_data(self, **context):
        # set default component context
        parent_context = copy(context)
        context.update(
            {
                "attrs": self.get_attrs(extra_attrs=None),
                "classes": self.get_classes(extra_classes=None),
                "style": self.get_style(extra_style=None),
                "childs": self.get_childs(parent_context),
                **self.context,
            }
        )
        return context

    def get_template_string(self):
        return str(self.template_string)

    def get_template_name(self, context=None):
        return construct_template_name(self.template_name)

    def get_template(self, template_name=None):
        """Return template name"""
        if not (template_name or self.template_string or self.template_name):
            class_name = self.__class__.__name__
            raise InvalidComponentTemplate(
                "template_string or template_name is not set for atomic component %s" % class_name
            )
        if self.template_string:
            template = self.renderer.engine.from_string(self.get_template_string())
            return template
        if not template_name:
            return self.renderer.engine.get_template(template_name or self.get_template_name())

    def is_shown(self, context=dict()):
        return context.get("is_shown", True)

    def render(self, context=dict(), extra_attrs=None, extra_style=None, extra_classes=None):
        if self.is_shown(context):
            # update base context based with render context
            context_data = self.get_context_data(**context)
            if context_data is None:
                raise TypeError("Expected a dict from get_context_data, got None")
            render_method = getattr(self, "render_html")
            return render_method(context_data)
        else:
            return ""

    def render_html(self, context):
        template = self.get_template()
        return mark_safe(template.render(context))

    def render_json(self, context):
        raise NotImplementedError("%s doesn't implement render_json method" % self.__class__.__name__)

    def render_dict(self, context):
        raise NotImplementedError("%s doesn't implement render_dict method" % self.__class__.__name__)


class ComponentMetaclass(MediaDefiningClass):
    """Collect child components declared on the base classes."""

    def __new__(mcs, name, bases, attrs):
        # Collect childs from current class and remove them from attrs.
        attrs["declared_childs"] = {
            key: attrs.pop(key) for key, value in list(attrs.items()) if isinstance(value, BaseComponent)
        }

        new_class = super().__new__(mcs, name, bases, attrs)

        # Walk through the MRO.
        declared_childs = {}
        for base in reversed(new_class.__mro__):
            # Collect fields from base class.
            if hasattr(base, "declared_childs"):
                declared_childs.update(base.declared_childs)

            # Field shadowing.
            for attr, value in base.__dict__.items():
                if value is None and attr in declared_childs:
                    declared_childs.pop(attr)

        new_class.base_childs = declared_childs
        new_class.declared_childs = declared_childs

        return new_class


class Component(BaseComponent):
    pass
