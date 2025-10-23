# from  django.http import HttpResponse
from  django.shortcuts import render

def home(req):
    return render(req,"index.html")

def about(req):
    return render(req,"about.html")

def news(req):
    return render(req,"news.html")

def grapes(req):
    return render(req,"grapes_news.html")

def fruits_table(req):
    return render(req,"fruits_table_news.html")

def fruits_stall(req):
    return render(req,"fruits_stall_news.html")

def fruits_plate(req):
    return render(req,"fruits_plate_news.html")

def fruits_bucket(req):
    return render(req,"fruits_bucket_news.html")

def celeb_straw(req):
    return render(req,"celeb_straw_news.html")

def contact(req):
    return render(req,"contact.html")

def shop(req):
    return render(req,"shop.html")

def singlepage_straw(req):
    return render(req,"singlepage_straw.html")

def singlepage_grapes(req):
    return render(req,"singlepage_grapes.html")

def singlepage_lemon(req):
    return render(req,"singlepage_lemon.html")

def singlepage_kiwi(req):
    return render(req,"singlepage_kiwi.html")

def singlepage_apple(req):
    return render(req,"singlepage_apple.html")

def singlepage_rasp(req):
    return render(req,"singlepage_rasp.html")

def cart(req):
    return render(req,"cart.html")

def checkout(req):
    return render(req,"checkout.html")

def error404(req):
    return render(req,"404.html")