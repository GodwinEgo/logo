from django.shortcuts import render
from .models import Logo, Review

def scan_logo(request):
    if request.method == 'POST':
        logo_name = request.POST['logo_name']
        image = request.FILES['logo_image']
        logo = Logo.objects.create(name=logo_name, image=image)
        return render(request, 'logo_scan/scan_result.html', {'logo': logo})
    return render(request, 'logo_scan/scan_logo.html')

def add_review(request, logo_id):
    logo = Logo.objects.get(pk=logo_id)
    if request.method == 'POST':
        rating = int(request.POST['rating'])
        comment = request.POST['comment']
        Review.objects.create(logo=logo, rating=rating, comment=comment)
    reviews = Review.objects.filter(logo=logo)
    return render(request, 'logo_scan/add_review.html', {'logo': logo, 'reviews': reviews})
