# @login_required
# def IssueUpdate(request, pk):
#     if request.method == 'POST':
#         form = IssueUpdateForm(request.POST)
#         if form.is_valid():
#             form_object = form.save(commit=False)
#             form_object.parent_project = Project.objects.get(pk=pk)
#             form_object.creator = request.user
#             form_object.worker = request.user
#             form.save()
#             projpk = Issue.objects.get(pk=pk).parent_project.pk
#             return redirect('track:track-issue-details', projpk)
#     else:
#         form = IssueUpdateForm()
#     template = 'issue_tracker_app/issue_update.html'
#     context = {
#         'issue': Issue.objects.get(pk=pk),
#     }
#     return render(request, template, context)

#  HTML to go with the directly above function view
# <form method="POST" class="w3-container w3-left-align">
#     {% csrf_token %}
#     <fieldset class="w3-teal w3-border-0 w3-padding-16">
#         <label for="title">Subject </label>
#         <input type="text" class="w3-input" name="title" value="{{ issue.title }}">
#         <br />
#         <label for="content">Content </label>
#         <textarea type="text" class="w3-input" rows="4" name="content">{{ issue.content }}</textarea>
#         <br />
#         <label for="status">Status </label>
#         <select name="status">
#             <option value="Not Started">Not Started</option>
#             <option value="In Progress">In Progress</option>
#             <option value="Done">Done</option>
#         </select>
#     </fieldset>
#     <br />
#     <button type="submit" class="w3-btn w3-black w3-hover-white">Update</button>
# </form>


# class IssueUpdate(UserPassesTestMixin, UpdateView):
#     model = Issue
#     template_name = 'issue_tracker_app/issue_update.html'
#     fields = ['title', 'content', 'status']
#     context = 'issue'
#     success_url = reverse_lazy('track:track-project-details')

#     def test_func(self):
#         issue = self.get_object()
#         if issue.worker == self.request.user:
#             return True
#         return False

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         issue = Issue.objects.get(self.kwargs['pk'])
#         context['title'] = issue.title
#         context['content'] = issue.content
#         return context
