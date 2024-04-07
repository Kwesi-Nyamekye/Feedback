from django.shortcuts import render
from .form import Reviewform
from django.http import HttpResponseRedirect

# Create your views here.

def review(request):
    if request.method == "POST":
        form = Reviewform()

        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")

    else:   
        form = Reviewform() 

    return render(request, "reviews/review.html", {
        "form": form
    })

def thank_you(request):
    return render(request, "reviews/thank_you.html")