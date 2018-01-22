# coding:utf-8

from django.shortcuts import render_to_response, HttpResponse

from .tasks import sendEmail, hello_world
from home.models import Column


def index(request):
    print "kaishi"
    hello_world.delay()
    # column = Column(name="name1", slug="slug1", intro="intro1")
    # column.save()
    #sendEmail.delay()
    return HttpResponse(u"欢迎光临 自强学堂!")
    # return render_to_response('index.html', locals())


def success(request):
    sendEmail.delay()
    return render_to_response('success.html', locals())
