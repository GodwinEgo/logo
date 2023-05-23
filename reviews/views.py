from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review


def review_logo(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_logo.html', {'form': form})


def home(request):
    return render(request, 'reviews/home.html')


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})
