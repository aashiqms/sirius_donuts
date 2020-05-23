from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import StrawberryForm


# def home(request):
#     return render(request, 'strawberry/base.html')

class HomeView(TemplateView):
    template_name = 'strawberry/base.html'


def order(request):
    if request.method == 'POST':
        filled_form = StrawberryForm(request.POST)
        if filled_form.is_valid():
            note = 'Thanks for ordering! Your %s %s Donuts will be delivered shortly' % (
                filled_form.cleaned_data['size'], filled_form.cleaned_data['flavour'])
            new_form = StrawberryForm()
            return render(request, 'strawberry/order.html', {'strawberryform': new_form, 'note': note})
    else:
        form = StrawberryForm()
        return render(request, 'strawberry/order.html', {'strawberryform': form})
