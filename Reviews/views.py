from typing import Any
from django.shortcuts import render
from .form import ReviewForm
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

# Create your views here.

class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

    def get(self, request):
        form = ReviewForm() 

        return render(request, "reviews/review.html", {
           "form": form })
    
    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        
        return render(request, "reviews/review.html", {
        "form": form })

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    
class ReviewListView(ListView):
    template_name="reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review 