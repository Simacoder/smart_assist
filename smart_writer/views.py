from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .forms import InputForm
from .utils import generate_text

def index(request):
    generated_text = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            generated_text = generate_text(input_text)
    else:
        form = InputForm()
    
    return render(request, 'index.html', {'form': form, 'generated_text': generated_text})

