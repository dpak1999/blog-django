from django.shortcuts import render

posts = [
    {
        "author": "Deepak",
        "title": "Post 1",
        "content": "Pariatur incididunt culpa sit minim amet proident. Duis do cupidatat nisi esse minim tempor laboris. Qui commodo elit et adipisicing ut do est.",
        "date": "February 17, 2021"
    },
    {
        "author": "Raj",
        "title": "Post 2",
        "content": "Irure qui consequat proident in occaecat qui. Aliquip adipisicing tempor elit tempor id do qui qui culpa eu irure in laborum. Consectetur est ullamco dolore aliquip irure ut ipsum quis elit laborum dolore labore fugiat pariatur. Proident labore qui consequat ad labore irure duis officia. Officia sunt cupidatat et excepteur nostrud enim.",
        "date": "February 17, 2021"
    }
]


def home(request):
    context = {
        "posts": posts
    }

    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "Get to know me.."})
