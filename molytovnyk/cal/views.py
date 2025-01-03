from django.shortcuts import render
from datetime import date
from .models import Holiday


def today_holiday(request):
    today = date.today()  # Получаем сегодняшнюю дату
    holiday = Holiday.objects.filter(date=today).first()  # Пытаемся найти праздник
    next_holidays = Holiday.objects.filter(date__gt=today).order_by('date')[:3] # три наступні свята після поточної дати

    return render(request, 'cal/today.html', {'holiday': holiday, 'today': today, 'next_holidays': next_holidays})
