# ----
# daily cron for checking if any email notifications need to be sent out
# -----

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.template import Context, loader
from django.core.mail import EmailMessage
from polls.models import Poll
from datetime import date, timedelta


def notify_all_users(poll, email_template):

    # get emails of all users
    users = User.objects.all()
    # users = ['santeyio@gmail.com', 'caleb123@yopmail.com']

    for user in users:

        subject = "Phantastes: " + poll.title
        email_from = "Phantastes <no-reply@phantastesproject.com>"

        # generate email template
        template = loader.get_template(email_template)
        context = Context({
            'name': user.username,
            'poll_title': poll.title,
            'poll_id': poll.id,
            'site_base': Site.objects.get_current().domain
        })  
        email_html = template.render(context)

        msg = EmailMessage(subject, email_html, email_from, [user.email])
        msg.content_subtype = "html"
        msg.send()
        fh = open('/tmp/mail_log/'+user.username, 'w')
        fh.write(email_html)
        fh.close()

                           

class Command(BaseCommand):

    def handle(self, *args, **options):

        polls = Poll.objects.filter()

        # poll = Poll.objects.get(id=4)
        # notify_all_users(poll, "polls/email_update.html")

        for poll in polls:
            if poll.nominations_open.date() == date.today():
                notify_all_users(poll, "polls/email_nominations.html")
            if poll.voting_open.date() == date.today():
                notify_all_users(poll, "polls/email_voting_open.html")
            if poll.voting_close.date() - date.today() == timedelta(1):
                notify_all_users(poll, "polls/email_voting_close.html")

        self.stdout.write('Successfully sent out update emails')


