from django.shortcuts import render
from .models import Menu, MenuItem


# Create your views here.
def index(request):
    menus = Menu.objects.all()
    menu_items = MenuItem.objects.all()
    context = {'menus': menus, 'menu_items': menu_items}
    return render(request, 'index.html', context)


def build_menu_tree(items):
    tree = []
    items_dict = {item.id: item for item in items}

    for item in items:
        if item.parent_id:
            parent = items_dict[item.parent_id]
            if not hasattr(parent, 'children'):
                parent.children = []
            parent.children.append(item)
        else:
            tree.append(item)

    return tree
