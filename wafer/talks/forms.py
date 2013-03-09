# Forms used for managing talks

from django import forms


class SubmitTalkForm(forms.Form):

    title = forms.CharField(max_length=1024)

    abstract = forms.CharField(widget=forms.Textarea)

    other_speakers = forms.CharField(required=False,
            widget=forms.Textarea)
