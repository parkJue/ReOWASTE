from django.contrib.auth import authenticate, login
from common.forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.forms import PasswordChangeForm
from common.models import Profile
from owaste.forms import ArticleForm
from common.forms import ImageForm
from collections import defaultdict
from django.shortcuts import render, redirect, get_object_or_404
from owaste.models import Oreview
from pybo.models import Answer, Question
from django.contrib.auth.models import User

# 회원가입

def signup(request):
    # 복사
    if request.method == 'POST':
        form_1 = ArticleForm(request.POST)
        if form_1.is_valid():
            article = form_1.save()
            return redirect('/')
    else:
        form_1 = ArticleForm()
    # 복사
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            Profile.objects.create(user=signed_user)

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,
                                password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('/owaste/index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form, 'form_1': form_1})


def academy(request):
    # 복사
    if request.method == 'POST':
        form_1 = ArticleForm(request.POST)
        if form_1.is_valid():
            article = form_1.save()
            article.save()
            return redirect('common:academy')
    else:
        form_1 = ArticleForm()
    return render(request, 'common/academy.html', {'form': form_1})



# 은주한테 받은 프로필
@login_required
def profile(request):
    if request.method == 'POST':
        form_1 = ImageForm(request.POST)

        if form_1.is_valid():
            img = form_1.save(commit=False)
            if request.FILES.get("image"):
                img.image = request.FILES.get("image")
            else:
                img.image = "rab.jpg"
            
            img.user = request.user
            img.save()
            
            return redirect('common:profile')
    else:
        form_1 = ImageForm()

    # 복사
    user = User.objects.filter(id=request.user.id)

    myreview_dict = defaultdict(list)
    myanswer_dict = defaultdict(list)
    myquestion_list = []
    myreview_qs = Oreview.objects.filter(user_id=request.user.id).select_related("shop")
    myanswer_qs = Answer.objects.filter(author_id=request.user.id).select_related("question")
    myquestion_qs = Question.objects.filter(author_id=request.user.id)
    mylike_qs = User.objects.filter(id=request.user.id).first()
    mylike_list = []

    for myreview in myreview_qs:
        myreview_dict[myreview.shop].append(myreview)

    for myanswer in myanswer_qs:
        myanswer_dict[myanswer.author].append(myanswer)

    for myquestion in myquestion_qs:
        myquestion_list.append(myquestion)

    for mylike in mylike_qs.voter_question.all():
        mylike_list.append(mylike)

    context = {
        'myreview_dict': dict(myreview_dict),
        'myanswer_dict' : dict(myanswer_dict),
        'myquestion_list':myquestion_list,
        'mylike_list' : mylike_list,
        'form_1': form_1,
        'user' : user,
    }
    return render(request, "common/profile.html", context)

# 비밀번호 변경
@login_required
def change_password(request):
    # 복사
    if request.method == 'POST':
        form_1 = ArticleForm(request.POST)
        if form_1.is_valid():
            article = form_1.save()
            return redirect('/')
    else:
        form_1 = ArticleForm()
    # 복사
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('/owaste/index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'common/change_password.html', {
        'form': form, 'form_1': form_1
    })


@login_required(login_url='common:login')
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        logout(request)
    return redirect('/owaste/index')
