from django import forms

class InputForm(forms.Form):
    input_text = forms.CharField(label='Input Text', widget=forms.Textarea)
