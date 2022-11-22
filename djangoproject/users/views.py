from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django import forms
from .models import Account
from .utils import get_user_data
from players.models import Player


class AccountForm(UserCreationForm):
    nickname = forms.CharField(label="your faceit nickname", max_length=100)
    class Meta:
        model = Account
        fields = ("email", 'nickname')


def register(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data.get('nickname')
            if Player.objects.filter(nickname=nickname).exists():
                messages.error(request, f"Account already exist")
                return render(request, 'users/register.html', {'form': form})
            user_data = get_user_data(user_nickname=nickname)
            if not user_data:
                messages.error(request, f"Faceit Account with {nickname} does not exist" )
                return render(request, 'users/register.html', {'form': form})
            form.save()
            messages.success(request, f"Account created - {nickname}")
            return redirect('players')
    else:
        form = AccountForm()

    return render(request, 'users/register.html', {'form': form})
