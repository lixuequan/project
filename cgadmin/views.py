#coding:utf8
# Create your views here.
import hashlib
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from cgadmin.models import User, Post, Team, Announcment, Project, Enterprise,File,Classify
from cgadmin.forms import RegForm
from django.contrib.auth import authenticate, login, logout


def reg(req):
    if req.method == "POST":
        rf = RegForm(req.POST)
        if rf.is_valid():
            print rf
            rf.instance.set_password(rf.cleaned_data['password'])
            rf.save()
            return render_to_response('login.html', {})
    else:
        rf = RegForm()
    return render_to_response('reg.html', {'rf': rf})


def login(req):
    if req.method == "POST":
        username = req.POST.get('username', None)
        password = req.POST.get('password', None)
        if username and password:
            password = hashlib.sha1(password + username).hexdigest()
            try:
                user = User.objects.get(username=username, password=password)
                return HttpResponseRedirect('/?uid=%s' % user.id)
            except ObjectDoesNotExist:
                return HttpResponseRedirect('/login/')
    else:
        pass
    return render_to_response('login.html', {})


def index(req):
    uid = req.GET.get('uid', None)
    if uid:
        user = User.objects.get(id=uid)
        return render_to_response('index.html', {'user': user})
    else:
        return HttpResponseRedirect('/reg/')


def plist(req):
    new_list = Post.objects.all()
    return render_to_response('plist.html', {'new_list': new_list})


def show_plist(req):
    nid = req.GET.get('nid')
    new = Post.objects.get(id=nid)
    return render_to_response('show_plist.html', {'new': new})


def send_post(req):
    nid = req.GET.get('nid')
    new = Post.objects.get(id=nid)
    return render_to_response('send_post.html', {'new': new})


def team_admin(req):
    team_list = Team.objects.all()
    return render_to_response('team_admin.html', {'team_list': team_list})


def classify_admin(req):
    class_list = Classify.objects.all()
    return render_to_response('classify_admin.html',{'class_list':class_list})


def announ_admin(req):
    announ_list = Announcment.objects.all()
    return render_to_response('announ_admin.html',{'announ_list':announ_list})

def project_admin(req):
    project_list = Project.objects.all()
    return render_to_response('project_admin.html',{'project_list':project_list})

def view_file(req):
    view_list = File.object.all()
    return render_to_response('view_list.html',{'view_list':view_list})


def use_help(req):
    return render_to_response('use_help.html',{})

def view_file(req):
    file_list = File.objects.all()
    return render_to_response('view_list.html',{'file_list':file_list})
