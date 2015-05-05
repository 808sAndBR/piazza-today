from datetime import datetime, date
from pytz import timezone

class Clocks:
    
    def pa_clock(self):
        pa = timezone('America/Los_Angeles')
        pa_data = datetime.now(pa)
        pa_time = pa_data.strftime(' %I:%M%p').replace(" 0", " ").replace(' ','').lower()
        return pa_time

    def lv_clock(self):
        lv = timezone('Europe/Riga')
        lv_data = datetime.now(lv)
        lv_time =lv_data.strftime(' %I:%M%p').replace(" 0", " ").replace(' ','').lower()
        return lv_time

    def head_date(self):
        day_test = date.today().strftime('%d')
        if day_test[:1] != '1':
            todays_date = date.today().strftime('%A, %B %dth').replace(' 0',' ')
        elif day_test[1:] == '02':
            todays_date = date.today().strftime('%A, %B %dnd').replace(' 0',' ')
        elif day_test[1:] == '03':
            todays_date = date.today().strftime('%A, %B %drd').replace(' 0',' ')
        else:
            todays_date = date.today().strftime('%A, %B %dth').replace(' 0',' ')
        return todays_date