from django import forms

class Reviewform(forms.Form):
    user_name = forms.CharField( label="Your Name", max_length=100, error_messages={
        "required": "Your name must not be empty"
    })

    review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length= 500, rating = forms.IntegerField(label="Your Rating", min_value=5)) 