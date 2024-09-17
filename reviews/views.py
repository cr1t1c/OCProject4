from itertools import chain

from django.db.models import Value, CharField
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from . import forms, models


@login_required
def feed(request):
    followers = request.user.following.all()
    followers_id = []
    for follower in followers:
        followers_id.append(follower.followed_user.pk)

    return render(request, "reviews/feed.html")


@login_required
def posts(request):
    reviews = models.Review.objects.filter(user=request.user)
    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))

    books = models.Book.objects.filter(user=request.user)
    books = books.annotate(content_type=Value("book", CharField()))

    return render(request, "reviews/posts.html")


@login_required
def create_book(request):
    form = forms.BookForm()
    if request.method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect("posts")
    return render(request, "reviews/create_book.html", context={"form": form})

@login_required
def create_review(request):
    form_book = forms.BookForm()
    form_review = forms.ReviewForm()
    if request.method == "POST":
        form_book = forms.BookForm(request.POST, request.FILES)
        form_review = forms.ReviewForm(request.POST)
        if all([form_book.is_valid(), form_review.is_valid()]):
            book = form_book.save(commit=False)
            book.user = request.user
            book.closed = True
            book.save()
            review = form_review.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            return redirect("posts")

    context = {"form_book": form_book, "form_review": form_review}
    return render(request, "reviews/create_review.html", context=context)
