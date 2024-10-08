from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import show_main, create_product_entry, show_xml, show_json, show_json_by_id, show_xml_by_id, register, login_user, logout_user, edit_product_entry, delete_product_entry, create_product_entry_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create/', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit/<uuid:id>/', edit_product_entry, name='edit_product_entry'),
    path('delete/<uuid:id>/', delete_product_entry, name='delete_product_entry'),
    path('create_ajax/', create_product_entry_ajax, name='create_ajax'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
