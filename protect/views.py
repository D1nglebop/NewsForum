from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class AddPost(PermissionRequiredMixin, CreateView):
    permission_required = ('NewsForumApp.add_post', )


class ChangePost(PermissionRequiredMixin, CreateView):
    permission_required = ('NewsForumApp.change_post', )
