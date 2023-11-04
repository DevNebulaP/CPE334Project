from flet import *
from homepage import home
#import todo
#import tobuy
#import signup
#import login

def views(page):
    return {
        '/': View(
            route='/',
            controls=[
                home(page)
            ]
        ),
        
        '/secondpage': View(
            route='/secondpage/',
            controls=[
                #todo.todo(page)
            ]
        ),
        '/thirdpage': View(
            route='/thirdpage/',
            controls=[
                #tobuy.tobuy(page)
            ]
        ),
        '/signup': View(
            route='/signup/',
            controls=[
                #signup.signup(page)
            ]
        ),
        '/login': View(
            route='/login/',
            controls=[
                #login.login(page)
            ]
        )
    }