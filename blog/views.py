from django.shortcuts import render


def index(request):
    number = 400
    title = "Blog"
    context = {"title": title, "products":["products1", "products2", "product3"]}
    return render(request, "blog/old_index.html", context)
# Create your views here.
