from account                   import views
from django.urls                import re_path,path,include
from django.contrib.auth.views  import login,logout


urlpatterns = [
    re_path('^account/login/$',     login,                      name='login'),
    re_path('^account/logout/$',    logout,                     name='logout'),
    re_path('^account/register/$',  views.register.as_view(),   name='register'),
       path('',             views.index.as_view(),      name='index'),

]
