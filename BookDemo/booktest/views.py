from django.shortcuts import render

from django.http import *
from django.template import RequestContext,loader
def index(request):
    # temp = loader.get_template("index.html")
    # return HttpResponse(temp.render())
    content= {"title":"hello"}
    return render(request,"index.html",content)
