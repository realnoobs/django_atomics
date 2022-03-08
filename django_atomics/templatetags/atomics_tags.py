from django.template import Library

from django_atomics import Component, NotComponent

register = Library()


@register.simple_tag(name="component", takes_context=True)
def render_component(context, component, **extra_context):
    if not isinstance(component, Component):
        raise NotComponent("%s is not component!")
    context = {"request": context["request"], **extra_context}
    return component.render(context)
