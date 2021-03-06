from django.shortcuts import render, redirect

from expenses_site.web.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, CreateExpenseForm, \
    EditExpenseForm, DeleteExpenseForm
from expenses_site.web.models import Profile, Expense


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    expenses = Expense.objects.all()
    all_expenses_prices = [exp.price for exp in expenses]
    budget_left = profile.budget - sum(exp.price for exp in expenses)

    context = {
        'profile': profile,
        'expenses': expenses,
        'expenses_prices': all_expenses_prices,
        'budget_left': budget_left,
    }

    return render(request, 'home-with-profile.html', context)


def create_expense_page(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateExpenseForm()

    context = {
        'form': form,
    }
    return render(request, 'expense-create.html', context)


def edit_expense_page(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditExpenseForm(instance=expense)

    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense-edit.html', context)


def delete_expense_page(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeleteExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteExpenseForm(instance=expense)

    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense-delete.html', context)


def show_profile(request):
    profile = get_profile()

    expenses = Expense.objects.all()
    expenses_count = len(expenses)
    budget_left = profile.budget - sum(exp.price for exp in expenses)

    context = {
        'profile': profile,
        'expenses_count': expenses_count,
        'budget_left': budget_left,
    }
    return render(request, 'profile.html', context)


def edit_profile_page(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditProfileForm()

    context = {
        'form': form
    }
    return render(request, 'profile-edit.html', context)


def delete_profile_page(request):
    profile = get_profile()
    
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteProfileForm()

    context = {
        'form': form
    }
    return render(request, 'profile-delete.html', context)


def create_profile(request):

    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)
