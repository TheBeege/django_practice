from django.core import serializers
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404
from django.template import loader

from .models import Document, User


# Create your views here.
def view_doc(request, doc_id):
    doc = get_object_or_404(Document, pk=doc_id)
    return render(request, 'docs/view_doc.html', {'doc':doc})


def create_doc(request, doc_obj):
    return HttpResponse('New doc')


def list_docs(request, filter=None):
    doc_list = Document.objects.order_by('-updated_at')[:10]
    template = loader.get_template('docs/index.html')
    context = {
        'doc_list': doc_list,
    }
    return render(request, 'docs/index.html', context)


def add_author_to_doc(request, doc_id, author_id):
    return HttpResponse('add author to doc')


def view_doc_authors(request, doc_id, author_id):
    return HttpResponse('see doc authors')
