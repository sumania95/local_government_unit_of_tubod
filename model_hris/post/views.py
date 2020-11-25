from django.shortcuts import render,get_object_or_404
from django.views.generic import (
    View,
    TemplateView,
)

#FUNCTIONS
from django.db.models.functions import Coalesce,Concat
from django.db.models import Q,F,Sum,Count
from django.db.models import Value
from django.urls import reverse

#JSON AJAX
from django.core import serializers
from django.http import JsonResponse
from django.template.loader import render_to_string

success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

from model_hris.post.models import (
    Post,
    Comment,
)
from model_hris.info_profile.models import (
    Profile,
    Notification,
    Message,
)
from model_hris.post.forms import (
    PostForm,
    CommentForm,
)

from django.contrib.auth.mixins import LoginRequiredMixin


class Post_AJAXView(LoginRequiredMixin,View):
    queryset = Post.objects.all()

    def get(self, request):
        data = dict()
        try:
            limit = self.request.GET.get('limit')
            start = self.request.GET.get('start')
            search_page = self.request.GET.get('search_page')
        except KeyError:
            limit = None
            start = None
            search_page = None
        if limit or start or search_page:
            data['form_is_valid'] = True
            post = self.queryset.filter(description__icontains = search_page).order_by('-date_created')[int(start):int(limit)]
            user = Profile.objects.get(user_id=self.request.user.id)
        context = {
            'post':post,
            'user':user,
        }
        data['post_table'] = render_to_string('main/components/list_post.html',context)
        return JsonResponse(data)

class Post_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = PostForm()
        context = {
            'form':form,
            'btn_name' : 'primary',
            'btn_title' : 'Submit Post',
        }
        data['html_form'] = render_to_string('main/forms/post_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = PostForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.profile_id = self.request.user.profile.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully posted.'
                data['form_is_valid'] = True
            else:
                data['form_is_valid'] = False
                data['message_type'] = error
                data['message_title'] = 'An error occurred.'
        return JsonResponse(data)

class Post_Like_AJAXView(LoginRequiredMixin,View):
    def post(self,request,pk):
        data = dict()
        post = get_object_or_404(Post, id = pk)
        post_profile = Post.objects.get(id=pk)
        if post.likes.filter(id = self.request.user.profile.pk).exists():
            post.likes.remove(self.request.user.profile)
        else:
            Notification.objects.create(profile_id = post_profile.profile.id,detail = 'Liked your post',user_id = self.request.user.id)
            post.likes.add(self.request.user.profile)
        return JsonResponse(data)

class Post_Comment_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data = dict()
        post = get_object_or_404(Post, id = pk)
        post_profile = Post.objects.get(id=pk)
        try:
            description = self.request.POST.get('comment')
        except KeyError:
            description = None
        if description:
            post.comments.create(description=description,profile=self.request.user.profile)
            Notification.objects.create(profile_id = post_profile.profile.id,detail = 'Commented your post',user_id = self.request.user.id)
        else:
            data['message_type'] = warning
            data['message_title'] = 'Warning: Missing Field!'
            data['form_is_valid'] = True
        return JsonResponse(data)
