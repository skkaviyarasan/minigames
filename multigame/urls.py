"""multigame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from games import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="LOGIN AND SIGNUP"),
    
    path('home',views.Home,name="home1"),
    path('ninja/',views.Ninja,name="ninja1"),
    path('snake2/',views.Snake2,name="snake2"),
    path('ColorShoot/',views.ColorShoot,name="colorshoot1"),
    path('SpaceShoot/',views.SpaceShoot,name="spaceshoot1"),
    
    path('snake/',views.Snake,name='snake1'),
    path('break/',views.Breakout,name='breakout1'),
    path('tictac/',views.Tictac,name='tictactoe'),
    path('birds/',views.Birds,name='birds1'),
    path('tetris/',views.Tetris,name='tetris1'),
    path('pong/',views.Pong,name='pong1'),
    path('bubble/',views.Bubble,name='bubble1'),
    path('sudoku/',views.Sudoku,name='sudoku1'),
    path('chess/',views.chess,name='chess1'),
    path('birds2/',views.Birds2,name='birds2'),
    path('tower/',views.tower,name='tower1'),
    path('memory/',views.memory,name='memory1'),

    ]

