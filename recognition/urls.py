from django.urls import path, include
from recognition  import views


urlpatterns = [
    path('men', views.men, name='men'),
    path('women', views.women, name='women'),
    
    
    #access the laptop camera
    path('video_feed', views.video_feed, name='video_feed'), # path for men

    path('video_fee', views.video_fee, name='video_fee'), # path for women


    ## for women dress path
    
    path('Camel', views.Camel, name='Camel'),
    path('Tan', views.Tan, name='Tan'),
    path('Tumbleweed', views.Tumbleweed, name='Tumbleweed'),
    path('Antique_Brass', views.Antique_Brass, name='Antique_Brass'),
    path('Pastle_Brown', views.Pastle_Brown, name='Pastle_Brown'),
    path('Desert_sand', views.Desert_sand, name='Desert_sand'),
    
    ## for men dress path 
    # Takin a first character of colour 
    path('C', views.C, name='C'),           # Camel
    path('T', views.T, name='T'),           # Tan
    path('Tumb', views.Tumb, name='Tumb'),  # Tumbleweed
    path('A', views.A, name='A'),           # Antique_brass
    path('P', views.P, name='P'),           # Pastle_brown
    path('D', views.D, name='D'),           # Desert_sand
    path('Tus', views.Tus, name='Tus'),     # Tuscany
    path('B', views.B, name='B'),           # Blast-off bronze
    path('L', views.L, name='L'),           # liver(organ)
    ]
    