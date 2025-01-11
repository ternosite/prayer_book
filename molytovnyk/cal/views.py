from django.shortcuts import render, redirect
from datetime import date
from .models import Holiday
from .forms import HolidayForm
from django.contrib.auth.decorators import login_required


def today_holiday(request):
    today = date.today()  # Получаем сегодняшнюю дату
    holiday = Holiday.objects.filter(date=today).first()  # Пытаемся найти праздник
    next_holidays = Holiday.objects.filter(date__gt=today).order_by('date')[:3] # три наступні свята після поточної дати
    return render(request, 'cal/today.html', {'holiday': holiday, 
                                              'today': today, 
                                              'next_holidays': next_holidays})


@login_required
def add_holiday(request):
    if request.method == 'POST':
        form = HolidayForm(request.POST)
        if form.is_valid():
            holiday = form.save(commit=False)
            holiday.author = request.user
            holiday.save()
            return redirect('cal:today_holiday')
    else:
        form = HolidayForm()

    return render(request, 'cal/add_holiday.html', {'form': form})

