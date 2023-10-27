from django.shortcuts import render
from django.core.paginator import Paginator

from .utils import get_mongo_db

from .models import Author, Tag, Quote


# Create your views here.
def main(request, page=1):
    # db = get_mongo_db()
    # quotes = db.quotes.find()
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={"quotes": quotes_on_page})


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
    quotes = Quote.objects.filter(tags__name=tag_name)
    return render(
        request,
        "quotes/tag_view.html",
        context={
            "tag_name": tag_name,
            "quotes": quotes,
        },
    )


def top_tags(request):
    top_tags = (
        Tag.objects.all()
        .annotate(quote_count=models.Count("quote"))
        .order_by("-quote_count")[:10]
    )
    return render(request, "top_tags.html", {"top_tags": top_tags})
