# ----
# daily cron for checking if any email notifications need to be sent out
# -----

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from polls.models import Poll
from datetime import date, timedelta


def notify_all_users(poll, notification_type):

    # get emails of all users
    users = User.objects.all()
    email_list = []
    for user in users:
        email_list.append(user.email)

    subject = "Phantastes: " + poll.title
    email_from = "Phantastes <no-reply@phantastesproject.com>"
    email_body = "this is the email body. It rocks, right?<br/> <br/><b>This is some more text in the email</b>"
    # print subject
    # print email_list
    
    msg = EmailMessage(subject, email_body, email_from, ['no-reply@phantastesproject.com'], email_list)
    msg.content_subtype = "html"
    msg.send()
                           

class Command(BaseCommand):

    def handle(self, *args, **options):

        polls = Poll.objects.filter()

        for poll in polls:
            if poll.nominations_open.date() == date.today():
                notify_all_users(poll, "nominations_open")
            if poll.voting_open.date() == date.today():
                notify_all_users(poll, "voting_open")
            if poll.voting_close.date() - date.today() == timedelta(1):
                notify_all_users(poll, "voting_close")



