import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from users.models import Profile
from .models import Project, Issue
from .forms import IssueCreateForm, IssueUpdateForm


def about_view(request):
    template = 'issue_tracker_app/about.html'
    return render(request, template)


def for_learner_view(request):
    template = 'issue_tracker_app/for_learner.html'
    return render(request, template)


class ProfileDetailsView(TemplateView):

    model = Profile
    template_name = 'issue_tracker_app/profile.html'
    success_url = reverse_lazy('track:track-project-details')


@login_required
def project_details_view(request, slug):
    template = 'issue_tracker_app/project.html'
    context = {
        'project': get_object_or_404(Project, slug=slug)
    }
    return render(request, template, context)


@login_required
def issue_details_view(request, slug):
    template = 'issue_tracker_app/issue.html'
    context = {
        'issue': get_object_or_404(Issue, slug=slug),
    }
    return render(request, template, context)


class ProjectCreateView(CreateView):

    model = Project
    template_name = 'issue_tracker_app/project_create.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('track:track-home')

    # sets the owner field of the project object to the current logged-in user
    def form_valid(self, form):
        form_object = form.instance
        form_object.owner = self.request.user
        dtnowstr = datetime.datetime.now().strftime('%m%d%Y%H%M%S%f')
        rpltitle = form_object.title.replace(
            ' ', '-').replace('/', '-')
        form_object.slug = rpltitle + dtnowstr
        return super().form_valid(form)


@login_required
def issue_create_view(request, slug):
    if request.method == 'POST':
        form = IssueCreateForm(request.POST)
        if form.is_valid():
            form_object = form.save(commit=False)
            form_object.parent_project = get_object_or_404(Project, slug=slug)
            dtnowstr = datetime.datetime.now().strftime('%m%d%Y%H%M%S%f')
            form_object.slug = form_object.title.replace(' ', '-') + dtnowstr
            form_object.creator = request.user
            form_object.worker = request.user
            form.save()
            return redirect('track:track-project-details', slug)
    else:
        form = IssueCreateForm()
    template = 'issue_tracker_app/issue_create.html'
    context = {
        'project': get_object_or_404(Project, slug=slug),
        'form': form
    }
    return render(request, template, context)


class ProjectUpdateView(UserPassesTestMixin, UpdateView):

    model = Project
    template_name = 'issue_tracker_app/project_update.html'
    fields = ['title', 'description']
    context = 'project'
    success_url = reverse_lazy('track:track-home')

    def test_func(self):
        project = self.get_object()
        if project.owner == self.request.user:
            return True
        return False


@login_required
def issue_update_view(request, slug):
    issue = get_object_or_404(Issue, slug=slug)
    form = IssueUpdateForm(instance=issue)
    if request.method == 'POST':
        form = IssueUpdateForm(request.POST, instance=issue)
        if form.is_valid():
            # form_object = form.save(commit=False)
            # form_object.last_updated = timezone.now
            form.save()
            return redirect('track:track-issue-details', slug)
    template = 'issue_tracker_app/issue_update.html'
    context = {
        'issue': issue,
        'form': form
    }
    return render(request, template, context)


class ProjectDeleteView(UserPassesTestMixin, DeleteView):

    model = Project
    template_name = 'issue_tracker_app/project_delete.html'
    context = 'project'
    success_url = reverse_lazy('track:track-home')

    def test_func(self):
        project = self.get_object()
        if project.owner == self.request.user:
            return True
        return False


@login_required
def issue_delete_view(request, slug):
    issue = get_object_or_404(Issue, slug=slug)
    if request.method == 'POST':
        issue.delete()
        projpk = issue.parent_project.slug
        return redirect('track:track-project-details', projpk)
    template = 'issue_tracker_app/issue_delete.html'
    context = {
        'issue': issue
    }
    return render(request, template, context)
