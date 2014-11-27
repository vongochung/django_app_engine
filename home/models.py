from django.db import models
from django.contrib.auth.models import User
import pytz
from pytz import timezone
import datetime

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

    def translate(self):
        utc = TZINFOS['utc']
        self.date = self.date.replace(tzinfo=utc)
        return self.date.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))

    def get_date(self):
        hcm = timezone('Asia/Ho_Chi_Minh')
        hcm= hcm.localize(self.date)
        return hcm.astimezone(timezone('Asia/Ho_Chi_Minh'))
        #return self.date.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))

    def fm_date(self):
        from datetime import datetime, timedelta
        from pytz import timezone
        import pytz
        bg_zone = timezone('Asia/Ho_Chi_Minh')
        bg_zone_time = bg_zone.localize(self.date)
        return bg_zone_time.strftime("%Y-%m-%d %H:%M:%S")

    def get_comment(self):
    	comments = COMMENT.objects.filter(post=self).order_by('date')
    	return comments

    def get_image(self):
	    if self.author.username == "vohien":
	        return "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/v/t1.0-1/c0.8.50.50/p50x50/28772_114592531904646_6681744_n.jpg?oh=3b3e926bff754f54b0063be4f32ba60d&oe=54D64EE3&__gda__=1427771457_e61b233fa6fa5446d3c4932ffbb0e65b"
	    return "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xpf1/v/t1.0-1/c2.0.50.50/p50x50/10177407_839821572703570_3363226913857924213_n.jpg?oh=82b709d4e4130d4b4fa2c2d5013a9242&oe=551F5CF9&__gda__=1423660972_967de75eaa114a961cfc2145cea0cc8a"

class COMMENT(models.Model):
    author = models.ForeignKey(User)
    post = models.ForeignKey(POST)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def get_image(self):
	    if self.author.username == "vohien":
	        return "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/v/t1.0-1/c0.8.50.50/p50x50/28772_114592531904646_6681744_n.jpg?oh=3b3e926bff754f54b0063be4f32ba60d&oe=54D64EE3&__gda__=1427771457_e61b233fa6fa5446d3c4932ffbb0e65b"
	    return "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xpf1/v/t1.0-1/c2.0.50.50/p50x50/10177407_839821572703570_3363226913857924213_n.jpg?oh=82b709d4e4130d4b4fa2c2d5013a9242&oe=551F5CF9&__gda__=1423660972_967de75eaa114a961cfc2145cea0cc8a"
