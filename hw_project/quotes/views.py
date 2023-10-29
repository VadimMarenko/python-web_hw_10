from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib.auth.decorators import login_required

from .utils import get_mongo_db
from .models import Author, Tag, Quote
from .forms import QuoteForm, AuthorForm


# Create your views here.
def main(request, page=1):
    # db = get_mongo_db()
    # quotes = db.quotes.find()
    quotes = Quote.objects.all().order_by("-created_at")
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    top_tags = Tag.objects.annotate(tag_count=Count("quote")).order_by("-tag_count")[
        :10
    ]

    return render(
        request,
        "quotes/index.html",
        context={
            "top_tags": top_tags,
            "quotes": quotes_on_page,
        },
    )


def author(request, author_name):
    # db = get_mongo_db()
    # author = db.authors.find_one({"fullname": author_name})
    author = Author.objects.get(fullname=author_name)
    if not author:
        author = None

    return render(request, "quotes/author_detail.html", context={"author": author})


def tag(request, tag_name):
    # db = get_mongo_db()
    # quotes = db.quotes.find({"tags": tag_name})
    quotes = Quote.objects.filter(tags__name=tag_name).order_by("-created_at")
    top_tags = Tag.objects.annotate(tag_count=Count("quote")).order_by("-tag_count")[
        :10
    ]
    return render(
        request,
        "quotes/tag_view.html",
        context={
            "top_tags": top_tags,
            "tag_name": tag_name,
            "quotes": quotes,
        },
    )


@login_required
def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = QuoteForm()

    return render(request, "quotes/add_quote.html", {"form": form})


@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = AuthorForm()

    return render(request, "quotes/add_author.html", {"form": form})
