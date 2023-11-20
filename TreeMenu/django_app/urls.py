from django.urls import path

from .templatetags.menu_tags import draw_menu
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('<path:path>/', draw_menu, name='draw_menu'),
]
