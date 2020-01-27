from django.shortcuts import render
from datetime import datetime

import random


def index(request):
    now = datetime.now()
    context = {
        'current_date': now
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'first/index.html', context)


def select(request):
    context = {'number':3}
    return render(request, 'first/select.html', context)


def result(request):
    chosen = int(request.GET['number']) ## number라는 값으로 전달받은 데이터를 꺼내옵니다.
    result = []
    if chosen >= 1 and chosen <= 45:
        result.append(chosen)
    box = []
    for i in range(0, 45):
        if chosen != i+1:
            box.append(i+1)
    random.shuffle(box)

    while len(result) < 6:
        result.append(box.pop())
    context = {'numbers': result} ## 첫 데이터를 받은 데이터로 넣습니다.
    return render(request, 'first/result.html', context)
