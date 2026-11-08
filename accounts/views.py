import random
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from accounts.models import CustomUser
from accounts.forms import CustomRegisterForm
from accounts.forms import CustomLoginForm

# 1. РЕГИСТРАЦИЯ
def register_view(request):
    if request.method == "POST":
        form_account = CustomRegisterForm(request.POST, request.FILES)
        if form_account.is_valid():
            user_data = form_account.cleaned_data
            avatar_file = user_data['avatar']
            user_data['avatar'] = avatar_file.name 
            
            if user_data.get('birth_date'):
                user_data['birth_date'] = user_data['birth_date'].strftime('%Y-%m-%d')

            verification_code = random.randint(100000, 999999)

            request.session['temp_user_data'] = user_data
            request.session['verification_code'] = verification_code

            send_mail(
                'Код подтверждения регистрации',
                f'Ваш специальный код: {verification_code}',
                'noreply@library.kg',
                [user_data['email']], 
                fail_silently=True,
            )

            return redirect('/verify/')
    else:
        form_account = CustomRegisterForm()

    return render(request, 'register.html', {'form': form_account})  


# 2. ПОДТВЕРЖДЕНИЕ КОДА 
def verify_code_view(request):
    if request.method == "POST":
        entered_code = request.POST.get('code')
        saved_code = request.session.get('verification_code')
        user_data = request.session.get('temp_user_data')

        if str(entered_code) == str(saved_code) and user_data:
            new_user = CustomUser.objects.create(
                email=user_data['email'],
                password=user_data['password'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                phone_number=user_data['phone_number'],
                birth_date=user_data['birth_date'],
                gender=user_data['gender'],
                city=user_data['city'],
                avatar=user_data['avatar']
            )
            
            del request.session['temp_user_data']
            del request.session['verification_code']

            return redirect('/login/')
        else:
            return render(request, 'verify.html', {'error': 'Неверный код!'})

    return render(request, 'verify.html')


# 3. АВТОРИЗАЦИЯ (Вход)
def auth_login_view(request):
    if request.method == "POST":
        form_account = CustomLoginForm(request.POST)
        if form_account.is_valid():
            email = form_account.cleaned_data.get('email')
            password = form_account.cleaned_data.get('password')
            
            try:
                account = CustomUser.objects.get(email=email, password=password)
                request.session['auth_user_id'] = account.id
                return redirect('/profile/')
            except CustomUser.DoesNotExist:
                return render(request, 'login.html', {
                    'form': form_account, 
                    'error': 'Неверный email или пароль'
                })
    else:
        form_account = CustomLoginForm()
    return render(request, 'login.html', {'form': form_account})


# 4. ВЫХОД
def auth_logout_view(request):
    if 'auth_user_id' in request.session:
        del request.session['auth_user_id']
    return redirect('/login/')


# 5. ЛИЧНЫЙ КАБИНЕТ
def profile_view(request):
    user_id = request.session.get('auth_user_id')
    if not user_id:
        return redirect('/login/')
        
    user = CustomUser.objects.get(id=user_id)
    return render(request, 'profile.html', {'user': user})
