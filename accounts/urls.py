from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path("password/", views.change_password, name="change_password"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)