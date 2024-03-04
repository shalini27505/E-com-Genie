from django.urls import path
from . import views

urlpatterns=[

    path('',views.home,name='home'),
    path('profile/', views.profile, name='profile'),
    path('hermes/',views.hermes,name='hermes'),
    path('zara/',views.zara,name='zara'),
    path('chanel/',views.chanel,name='chanel'),
    path('ww/',views.ww,name='ww'),
    path('wt/',views.wt,name='wt'),
    path('lehangas/',views.lehangas,name='lehangas'),
    path('kurtis/',views.kurtis,name='kurtis'),
    path('night/',views.night,name='night'),
    path('hoodie/',views.hoodie,name='hoodie'),
    path('paulmi/',views.paulmi,name='paulmi'),
    path('shirts/',views.shirts,name='shirts'),
    path('track/',views.track,name='track'),
   # path('shirts/',views.,name='shirts'),
  
]
