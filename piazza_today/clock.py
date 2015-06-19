from apscheduler.schedulers.blocking import BlockingScheduler
from piazza_today.management.commands.zero_scraper import 

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=2)
def scheduled_job():
    #import the scraping file and run it here

    sched.start()
