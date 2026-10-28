from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from book.models import Book

def book_list_view(request):
    if request.method == "GET":
        book = Book.objects.all().order_by('-id')
    return render(request, 'book_list.html', {'book': book})

def book_detail_view(request, id):
    book_id = get_object_or_404(Book, id=id)
    return render(request, 'book_detail.html', {'book': book_id})

def about_me(request):
    if request.method == "GET":
        return HttpResponse("Меня зовут Данияр. Мне 36 лет. Я работаю начальником научно-исследовательского отделения Учебно-исследовательского центра при Министерстве чрезвычайных ситуаций. Воинское звание МАЙОР. В данный момент прохожу курс Бэкенд разработки")

def my_favorite_writers(request):
    if request.method == "GET":
        return HttpResponse("Чингиз Айтматов, Алыкул Осмонов, Александр Пушкин")

def sayings_of_great_poets(request):
    if request.method == "GET":
        return HttpResponse("""
                    <p>«Перед каждым человеком стоит неизбывная задача — быть человеком, сегодня, завтра, всегда».</p>
                    <p><img src="https://sputnik.kg/img/103069/39/1030693965_0:192:1607:1799_1920x0_80_0_0_1805d67ebf1438b4028b6b6c003eebde.jpg"</p>

                    <p>«О силе поэзии и судьбе:«Жизнь человека коротка, но слово поэта и любовь к родной земле остаются вечными».</p>
                    <p><img src="https://upload.wikimedia.org/wikipedia/ky/4/49/Alikul_osmonov.jpg?utm_source=ky.wikipedia.org&utm_campaign=index&utm_content=original"</p>

                    <p>«О творчестве «Гений и злодейство несовместны».</p>
                    <p><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYUS67shq8z18jkt7-IVLnJiZw7488Hc9jaSaGygNesGLFdXL_hz1Gp3H1744d1PbtfkS1gQ-MZOUqVtGuqQr6cV5LOYrVqCoBn31O2w&s=10"</p>
                """)