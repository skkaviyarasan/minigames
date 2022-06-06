from django.shortcuts import render,redirect
from .models import *
import sqlite3
# Create your views here.
def index(request):
    try:
        if request.method=="POST":
            name=request.POST['name']
            email=request.POST['email']
            phone=request.POST['number']
            password=request.POST['password']
            dob=request.POST['dob']
            da=Gameuser()
            da.Name=name
            da.Email=email
            da.PhoneNumber=phone
            da.Password=password
            da.DateofBirth=dob
            da.save()
    except:        
        if request.method=="POST":
            Name=request.POST['sname']
            Password=request.POST['spassword']
            con=sqlite3.connect("db.sqlite3")
            con.row_factory=sqlite3.Row
            cur=con.cursor()
            cur.execute("select * from games_Gameuser")
            while True:
                row=cur.fetchone()
                if row is None:
                    break;
                    
                elif row[1]==Name and row[4]==Password:
                    return redirect('home1')
    return render(request,"index.html")

def Home(request):
    return render(request,'home.html')
def Ninja(request):
    return render(request,'ninja.html')
def Snake2(request):
    return render(request,'snake2.html')
def ColorShoot(request):
    return render(request,'color-shoot.html')
def SpaceShoot(request):
    return render(request,'space-shoot.html')



def Snake(request):
    return render(request,'snake.html')

def Breakout(request):
    return render(request,'breakout.html')

def Tictac(request):
    return render(request,'tictac.html')

def Birds(request):
    return render(request,'birds.html')

def Tetris(request):
    return render(request,'tetris.html')

def Pong(request):
    return render(request,'pong.html')

def Bubble(request):
    return render(request,'bubble-shooter.html')

def Sudoku(request):
    return render(request,'sudoku.html')

def chess(request):
    return render(request,'chess.html')

def Birds2(request):
    return render(request,'birds2.html')

def tower(request):
    return render(request,'tower.html')

def memory(request):
    return render(request,'memory.html')