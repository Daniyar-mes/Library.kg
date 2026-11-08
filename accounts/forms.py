from django import forms
from accounts.models import CustomUser
from captcha.fields import CaptchaField

GENDER_CHOICES = (
    ('Male', 'Мужской'),
    ('Female', 'Женский'),
)

# 1. ФОРМА РЕГИСТРАЦИИ
class CustomRegisterForm(forms.ModelForm):
    avatar = forms.ImageField(required=True, label="Аватар")
    email = forms.EmailField(required=True, initial='@gmail.com', label="Электронная почта")
    phone_number = forms.CharField(required=True, initial='996', label="Номер телефона")
    birth_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}), label="Дата рождения")
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True, initial='Male', label="Пол")
    city = forms.CharField(max_length=25, initial='Bishkek', label="Город")
    password_confirm = forms.CharField(widget=forms.PasswordInput(), label="Подтвердите пароль")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'password',
            'avatar', 
            'email',
            'phone_number',
            'birth_date',
            'gender',
            'city'
        )
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают!")
        return cleaned_data


# 2. ФОРМА АВТОРИЗАЦИИ 
class CustomLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'example@gmail.com'}), label="Email")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}), label="Пароль")
    captcha = CaptchaField(label="Введите текст с картинки")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'captcha':
                field.widget.attrs.update({'class': 'form-control'})
