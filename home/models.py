from django.db import models
from django.contrib.auth.models import User
import pytz
from pytz import timezone
import datetime
from django.core.paginator import Paginator, PageNotAnInteger

class UtcTzinfo(datetime.tzinfo):
    def utcoffset(self, dt): return datetime.timedelta(0)
    def dst(self, dt): return datetime.timedelta(0)
    def tzname(self, dt): return 'UTC'
    def olsen_name(self): return 'UTC'


TZINFOS = {
  'utc':UtcTzinfo(),
}

class POST(models.Model):
    author = models.ForeignKey(User)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    has_next = False
    next_page = 0

    def __unicode__(self):
        return u'%s %s' % (self.author, self.content[:20])

    def translate(self):
        utc = TZINFOS['utc']
        self.date = self.date.replace(tzinfo=utc)
        return self.date.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))


    def get_comment(self):
        comments_list = COMMENT.objects.filter(post=self).order_by("-date")
        paginator = Paginator(comments_list, 5)
        comments = paginator.page(1)
        self.has_next = comments.has_next()
        self.next_page = comments.next_page_number()
        return reversed(comments)

    def get_image(self):
        if self.author.username == "vohien":
            return "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/v/t1.0-1/c0.8.50.50/p50x50/28772_114592531904646_6681744_n.jpg?oh=3b3e926bff754f54b0063be4f32ba60d&oe=54D64EE3&__gda__=1427771457_e61b233fa6fa5446d3c4932ffbb0e65b"
        elif self.author.username == "met":
            return "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xap1/v/t1.0-1/c0.0.160.160/p160x160/11608_373424162819254_2043029436955836004_n.jpg?oh=b064caae5f1cc2c61026de977343e3f1&oe=55184D6D&__gda__=1426544220_48597063de14f4b91395acce335ceaf2"
        else:
            return "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xpf1/v/t1.0-1/c2.0.50.50/p50x50/10177407_839821572703570_3363226913857924213_n.jpg?oh=82b709d4e4130d4b4fa2c2d5013a9242&oe=551F5CF9&__gda__=1423660972_967de75eaa114a961cfc2145cea0cc8a"

class COMMENT(models.Model):
    author = models.ForeignKey(User)
    post = models.ForeignKey(POST)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
            return u'%s %s' % (self.author, self.content[:20])

    def get_image(self):
        if self.author.username == "vohien":
            return "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/v/t1.0-1/c0.8.50.50/p50x50/28772_114592531904646_6681744_n.jpg?oh=3b3e926bff754f54b0063be4f32ba60d&oe=54D64EE3&__gda__=1427771457_e61b233fa6fa5446d3c4932ffbb0e65b"
        elif self.author.username == "met":
            return "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xap1/v/t1.0-1/c0.0.160.160/p160x160/11608_373424162819254_2043029436955836004_n.jpg?oh=b064caae5f1cc2c61026de977343e3f1&oe=55184D6D&__gda__=1426544220_48597063de14f4b91395acce335ceaf2"
        else:
	       return "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xpf1/v/t1.0-1/c2.0.50.50/p50x50/10177407_839821572703570_3363226913857924213_n.jpg?oh=82b709d4e4130d4b4fa2c2d5013a9242&oe=551F5CF9&__gda__=1423660972_967de75eaa114a961cfc2145cea0cc8a"

class TAICHINH(models.Model):
    author = models.ForeignKey(User)
    content = models.TextField()
    money = models.DecimalField(max_digits=19, decimal_places=10)
    chi = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s %s' % (self.author, self.content[:20])

    def translate(self):
        utc = TZINFOS['utc']
        self.date = self.date.replace(tzinfo=utc)
        return self.date.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))

    class Meta:
        ordering = ['-date']