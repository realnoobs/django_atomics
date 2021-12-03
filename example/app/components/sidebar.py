from django.urls.base import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django_atomics.atoms.basics import Link
from django_atomics.atoms.containers import Div, ListItem, UnOrderedList
from django_atomics.permissions import IsAuthenticated, PermissionMixin


class AuthenticatedListItem(PermissionMixin, ListItem):
    permission_classes = [IsAuthenticated]


sidebar_header = Div(
    classes=["sidebar-header"],
)

sidebar_menu = Div(
    classes=["sidebar-menu"],
    childs=UnOrderedList(
        childs=[
            ListItem(
                style={"color": "red", "font-weight": "bolder"},
                childs=Link(
                    url=reverse_lazy("index"),
                    label=_("Home"),
                ),
            ),
            ListItem(
                childs=Link(
                    url=reverse_lazy("index"),
                    label=_("Contact"),
                )
            ),
            AuthenticatedListItem(
                childs=[
                    Link(label=_("Settings")),
                    UnOrderedList(
                        childs=[
                            ListItem(childs=Link(url=reverse_lazy("index"), label=_("Profile"))),
                            ListItem(childs=Link(url=reverse_lazy("index"), label=_("Logout"))),
                        ]
                    ),
                ]
            ),
        ]
    ),
)

sidebar_footer = Div(
    classes=["sidebar-footer"],
)

sidebar = Div(
    classes=["sidebar"],
    attrs={"x-data": "sidebar"},
    childs=[sidebar_header, sidebar_menu, sidebar_footer],
)
