from django.shortcuts import render
from third.models import Restaurand, Review
from django.core.paginator import Paginator
from third.forms import RestaurantForm, ReviewForm, UpdateRestaurantForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Avg  # Count 를 임포트



def list(request):
    restaurant = Restaurand.objects.all().annotate(reviews_count=Count('review')).annotate(average_point=Avg('review__point')) # review는 forieng key임. restaurant를 선언을 했기 때문에 restaurant에 review를 인식할 수 있게 됨.
    # Relation 명은 소문자여도 되서, 'review'가 되는것
    # review라는 테이블 안에 point를 평균을 낼 것, 장고의 규칙 상 review__point가 됨.
    paginator = Paginator(restaurant, 5)

    page = request.GET.get('page')  ## third/list?page=1
    items = paginator.get_page(page)
    context = {
        'restaurants': items
    }
    return render(request, 'third/list.html', context)


def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)  # request의 POST 데이터들을 바로 PostForm에 담을 수 있습니다.
        if form.is_valid():  # 데이터가 form 클래스에서 정의한 조건 (max_length 등)을 만족하는지 체크합니다.
            new_item = form.save()  # save 메소드로 입력받은 데이터를 레코드로 추가합니다.
        return HttpResponseRedirect('/third/list/')  # 리스트 화면으로 이동합니다.
    form = RestaurantForm()
    return render(request, 'third/create.html', {'form': form})


def update(request):
    # 비밀번호를 새로 입력받는 것이 아니라 기존 비밀번호와 일치하는지 검증해야 하므로 약간의 수정이 필요
    if request.method == 'POST' and 'id' in request.POST:
        item = get_object_or_404(Restaurand, pk=request.POST.get('id'))
        password = request.POST.get("password", "")
        form = UpdateRestaurantForm(request.POST, instance=item)  # NOTE: instance 인자(수정대상) 지정
        if form.is_valid() and password == item.password:  # 비밀번호 검증 추가
            item = form.save()
    elif 'id' in request.GET:
        item = get_object_or_404(Restaurand, pk=request.GET.get('id'))
        form = RestaurantForm(instance=item)
        form.password = ''  # password 데이터를 비웁니다.
        return render(request, 'third/update.html', {'form': form})

    return HttpResponseRedirect('/third/list/')  # 리스트 화면으로 이동합니다.



def detail(request, id):
    if id is not None:
        item = get_object_or_404(Restaurand, pk=id)
        reviews = Review.objects.filter(restaurant=item).all()
        return render(request, 'third/details.html', {'item': item, 'reviews':reviews})
    return HttpResponseRedirect('/third/list/')  # 리스트 화면으로 이동합니다.


def delete(request, id):
    item = get_object_or_404(Restaurand, pk=id)
    if request.method == 'POST' and 'password' in request.POST:
        if item.password == request.POST.get('password'):
            item.delete()
            return redirect('list')  # 리스트 화면으로 이동합니다.

        return redirect('restaurant-detail', id=id)  # 비밀번호가 입력되지 않으면 상세페이지로 되돌아감

    return render(request, 'third/delete.html', {'item': item})


def review_create(request, restaurant_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)  #
        if form.is_valid():  # 데이터가 form 클래스에서 정의한 조건 (max_length 등)을 만족하는지 체크합니다.
            new_item = form.save()  # save 메소드로 입력받은 데이터를 레코드로 추가합니다.
        return redirect('restaurant-detail', id=restaurant_id)  # 전화면으로 이동합니다.

    item = get_object_or_404(Restaurand, pk=restaurant_id)
    form = ReviewForm(initial={'restaurant': item})
    return render(request, 'third/review_create.html', {'form': form, 'item': item})

def review_delete(request, restaurant_id, review_id):
    item = get_object_or_404(Review, pk=review_id)
    item.delete()

    return redirect('restaurant-detail', id=restaurant_id)  # 전 화면으로 이동합니다.

def review_list(request):
    reviews = Review.objects.all().select_related()
    paginator = Paginator(reviews, 10)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    context = {
        'reviews': items
    }
    return render(request, 'third/review_list.html', context)

