from django.shortcuts import render, get_object_or_404
from . models import Author, Epoch, Picture
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def pictures(request):
    pictures_list = Picture.objects.filter(status='published').order_by('-publish')
    paginator = Paginator(pictures_list, 6)
    page = request.GET.get('page')

    try:
        pictures = paginator.page(page)
    except PageNotAnInteger:
        pictures = paginator.page(1)
    except EmptyPage:
        pictures = paginator.page(paginator.num_pages)

    author = None
    authors_list = Author.objects.all().order_by('author')

    unsorted_epochs = Epoch.objects.all()
    epochs = sorted(unsorted_epochs, key=lambda x: x.epoch.split('-')[0])   # , reverse=True

    context = {
        'pictures': pictures,
        'authors_list': authors_list,
        'epochs': epochs,
        'page': page,
    }

    return render(request, 'blog/pictures.html', context)

def authors(request):
    authors_list = Author.objects.all().order_by('author')
    paginator = Paginator(authors_list, 6)
    page = request.GET.get('page')

    try:
        authors = paginator.page(page)
    except PageNotAnInteger:
        authors = paginator.page(1)
    except EmptyPage:
        authors = paginator.page(paginator.num_pages)

    unsorted_epochs = Epoch.objects.all()
    epochs = sorted(unsorted_epochs, key=lambda x: x.epoch.split('-')[0])
    pictures = Picture.objects.filter(status='published').order_by('-publish')
    for author in authors:
        picture = author.picture.first()

    context = {
        'pictures': pictures,
        'authors_list': authors_list, 
        'authors': authors,
        'epochs': epochs,
        'author': author,
        'page': page,
    }

    return render(request, 'blog/authors.html', context)

def epochs(request):
    unsorted_epochs = Epoch.objects.all()
    epochs = sorted(unsorted_epochs, key=lambda x: x.epoch.split('-')[0])
    pictures = Picture.objects.filter(status='published').order_by('-publish')
    authors_list = Author.objects.all().order_by('author')
    for epoch in epochs:
        picture = epoch.picture.first()

    context = {
        'pictures': pictures, 
        'authors_list': authors_list,
        'epochs': epochs,
        'epoch': epoch,
    }

    return render(request, 'blog/epochs.html', context)

def author_pictures(request, author_slug=None):
    epoch = None
    unsorted_epochs = Epoch.objects.all()
    epochs = sorted(unsorted_epochs, key=lambda x: x.epoch.split('-')[0])
    author = None
    authors_list = Author.objects.all().order_by('author')
    pictures = Picture.objects.filter(status='published').order_by('-publish')

    if author_slug:
        author = get_object_or_404(Author, slug=author_slug)
        pictures = pictures.filter(author=author)

    paginator = Paginator(pictures, 6)
    page = request.GET.get('page')

    try:
        pictures = paginator.page(page)
    except PageNotAnInteger:
        pictures = paginator.page(1)
    except EmptyPage:
        pictures = paginator.page(paginator.num_page)

    context = {'author': author,
                'authors_list': authors_list,
                'epochs': epochs,
                'pictures': pictures,
                'page': page
    }
    return render(request, 'blog/author_pictures.html', context)

def epoch_pictures(request, epoch_slug=None):
    epoch = None
    unsorted_epochs = Epoch.objects.all()
    epochs = sorted(unsorted_epochs, key=lambda x: x.epoch.split('-')[0])
    author = None
    authors_list = Author.objects.all().order_by('author')
    pictures_list = Picture.objects.filter(status='published').order_by('-publish')

    if epoch_slug:
        epoch = get_object_or_404(Epoch, slug=epoch_slug)
        pictures_epoch = pictures_list.filter(epoch=epoch)

    paginator = Paginator(pictures_epoch, 6)
    page = request.GET.get('page')

    try:
        pictures = paginator.page(page)
    except PageNotAnInteger:
        pictures = paginator.page(1)
    except EmptyPage:
        pictures = paginator.page(paginator.num_page)

    context = {'epoch': epoch,
                'epochs': epochs,
                'authors_list': authors_list,
                'pictures': pictures,
                'page': page,
    }
    return render(request, 'blog/epoch_pictures.html', context)

def picture_detail(request, picture_slug=None):
    epoch = None
    unsorted_epochs = Epoch.objects.all()
    epochs = sorted(unsorted_epochs, key=lambda x: x.epoch.split('-')[0])
    author = None
    authors_list = Author.objects.all().order_by('author')

    picture = get_object_or_404(Picture, slug=picture_slug, status='published')

    context = {'picture': picture,
                'epochs': epochs,
                'authors_list': authors_list,
                'author': author}
    return render(request, 'blog/detail_picture.html', context)

def about(request):
    unsorted_epochs = Epoch.objects.all()
    epochs = sorted(unsorted_epochs, key=lambda x: x.epoch.split('-')[0])
    pictures = Picture.objects.filter(status='published').order_by('-publish')
    authors_list = Author.objects.all().order_by('author')

    context = {
        'pictures': pictures, 
        'authors_list': authors_list,
        'epochs': epochs,
    }

    return render(request, 'blog/about.html', context)

def contact(request):
    unsorted_epochs = Epoch.objects.all()
    epochs = sorted(unsorted_epochs, key=lambda x: x.epoch.split('-')[0])
    authors_list = Author.objects.all().order_by('author')

    if request.method == "POST":
        message_name = request.POST['message-name']
        message_subject = request.POST['message-subject']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            message_subject, # subject
            message, # message
            message_email, # from email
            ['sammlerverkauft@gmail.com'], # to email
        )

        context = {
            'epochs': epochs,
            'authors_list': authors_list,
            "message_subject": message_subject,
            "message_name": message_name,
        }

        return render(request, 'blog/contact.html', context)
    else:
        return render(request, 'blog/contact.html', {'epochs': epochs,
                                                    'authors_list': authors_list,})
 