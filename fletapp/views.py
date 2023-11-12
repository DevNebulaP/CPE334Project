from flet import *
from homepage import Home
#from todo import main
from tobuy_new import ToBuyMain
from calculator_new import Calculate
#import signup
from login import LoginMain

def views(page):
    return {
        '/': View(
            route='/',
            controls=[
                Home(page)
            ]
        ),
        
        '/todo': View(
            route='/todo/',
            controls=[
                #main(page)
            ]
        ),
        '/thirdpage': View(
            route='/thirdpage/',
            controls=[
                ToBuyMain(page)
            ]
        ),
        '/calculator': View(
            route='/calculator/',
            controls=[
                Calculate(page).build_container()
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
                LoginMain(page)
            ]
        )
    }