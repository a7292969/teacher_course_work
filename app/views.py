from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import CommentForm
from .models import Comment


def index(req):
    comments = Comment.objects.all()
    return render(req, 'index.html', {'comments': comments})


def add_comment(req):
    if req.method == 'POST':
        form = CommentForm(req.POST)
    if not form.is_valid():
        print(form.errors)
        return HttpResponse(status=400)
    Comment.objects.create(
        author=form.cleaned_data['author'], text=form.cleaned_data['text'])
    return redirect('/')
