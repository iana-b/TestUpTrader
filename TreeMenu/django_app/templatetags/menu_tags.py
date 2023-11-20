from django import template
from ..models import MenuItem
from ..views import build_menu_tree

register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(menu__name=menu_name)
    menu_tree = build_menu_tree(menu_items)
    return {
        'menu_name': menu_name,
        "menu_items": menu_tree,
    }
