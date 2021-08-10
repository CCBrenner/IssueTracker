from django import forms
from .models import Issue


class IssueCreateForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'content', 'priority', 'difficulty']
        # edits display of input and textarea fields
        widgets = {
            'title': forms.TextInput(attrs={'size': 39}),
            # 'content': forms.Textarea(attrs={'rows': 5, 'cols': 54}),
        }


class IssueUpdateForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'content', 'priority', 'difficulty', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'size': 39}),
            # 'content': forms.Textarea(attrs={'rows': 7, 'cols': 54}),
        }
