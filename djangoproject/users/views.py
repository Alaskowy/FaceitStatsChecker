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
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created - {username}")
            return redirect('players')
    else:
        form = AccountForm()

    return render(request, 'users/register.html', {'form': form})
