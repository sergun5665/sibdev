import csv, io
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Deals


def index(request):
    return render(request, 'index.html', )


@permission_required('admin.can_add_log_entry')
def deals_upload(request):
    template = "index.html"

    if request.method == "GET":
        return render(request, template)
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Только csv фаил')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Deals.objects.update_or_create(
            customer=column[0],
            item=column[1],
            total=column[2],
            quantity=column[3],
            date=column[4]
        )

    context = {}
    return render(request, template, context, )


def top(request):
    high = Deals.objects.all()

    return render(request, 'index.html', {"high": high})

