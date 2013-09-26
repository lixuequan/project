#coding:utf-8
from django.db import models


class Enterprise(models.Model):
    name = models.CharField(max_length=64,verbose_name="公司名称")
    master = models.CharField(max_length=64,verbose_name="公司法人")
    brief = models.CharField(max_length=256,verbose_name="公司简介",blank=True,null=True)
    class Meta:
        verbose_name = "公司"
        verbose_name_plural = "公司信息管理"
    def __unicode__(self):
        return self.name



class User(models.Model):
    username = models.CharField(max_length=32,verbose_name='姓名')
    password = models.CharField(max_length=256,verbose_name='密码')
    email = models.EmailField(max_length=64,verbose_name='邮箱',blank=True,null=True)
    disc = models.TextField(max_length=512,verbose_name='自述',blank=True,null=True)
    headimg = models.FileField(upload_to="headimg/%Y%m%d",verbose_name='头像',blank=True,null=True)

    class Meta:
        verbose_name='用户'
        verbose_name_plural='用户管理'
    def __unicode__(self):
        return self.username


class Team(models.Model):
    name = models.CharField(max_length=16,verbose_name="部门名称")
    member = models.ManyToManyField(User,blank=True,null=True)
    disc = models.CharField(max_length=32,verbose_name="职责描述",blank=True,null=True)
    parent = models.ForeignKey(Enterprise,verbose_name="直属公司",blank=True,null=True)
    class Meta:
        verbose_name = '部门'
        verbose_name_plural = '部门管理'
    def __unicode__(self):
        return self.name




class Post(models.Model):
    pfile = models.ForeignKey("File",verbose_name="评论对象(文件)")
    puser = models.ManyToManyField(User,verbose_name="评论人")
    title = models.CharField(max_length=30,verbose_name="标 题")
    content = models.TextField(verbose_name="内 容")
    pdate = models.DateTimeField(auto_now_add=True,verbose_name="评论时间")


    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论管理'

    def __unicode__(self):
        return self.title


class Project(models.Model):
    project_name = models.CharField(max_length=32,verbose_name="项目名")
    pcreate_date = models.DateTimeField(auto_now_add=True,verbose_name="创建日期")
    project_admin = models.ManyToManyField(User,blank=True,null=True)
    project_disc = models.CharField(max_length=64,verbose_name="项目描述",blank=True,null=True)
    post = models.ManyToManyField(Post,verbose_name="项目评论",blank=True,null=True)

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '项目管理'
    def __unicode__(self):
        return self.project_name


class Classify(models.Model):
    name = models.CharField(max_length=16)
    disc = models.CharField(max_length=64)


class Announcment(models.Model):
    announ_title = models.CharField(max_length=32,verbose_name='主题')
    context = models.TextField(max_length=512,verbose_name='正文')
    announ_user = models.ForeignKey(User,verbose_name='发布者')
    announ_date = models.DateField(auto_now_add=True,verbose_name='发布日期')
    announ_enterprise = models.ManyToManyField(Enterprise)
    announ_obj = models.ManyToManyField(Team)

    class Meta:
        verbose_name = '公告'
        verbose_name_plural = '公告管理'
    def __unicode__(self):
        return self.announ_title

class File(models.Model):
    file_disc = models.CharField(max_length=16,verbose_name="文件描述")
    project = models.ForeignKey(Project,verbose_name="项目名称")
    file_dir = models.FilePathField(default="upload/",allow_folders=True,null=True,blank=True)
    file_select = models.FileField(upload_to='upload/filetype',null=True,blank=True)
    fcreate_date = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    create_user = models.ForeignKey(User,verbose_name="创建者")


    class Meta:
        verbose_name = '文件'
        verbose_name_plural = '文件管理'
    def __unicode__(self):
        return self.file_disc