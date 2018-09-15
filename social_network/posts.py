from datetime import datetime as dt

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text.lstrip('text=')
        if timestamp is None:
            self.timestamp = dt.now()
        else:
            self.timestamp = timestamp
        self.set_user(None)

    def __str__(self):
        name_txt = '@' + self.user.first_name + ' ' + self._extra_name_text()
        post_txt = '"{base_post}"\n\t'.format(base_post=self.text) + self._extra_post_text()
        timestamp_txt = self.timestamp.strftime('%A, %b %d, %Y')
        return name_txt + post_txt + timestamp_txt

    # Use to enable sorting of posts by timestamp in User.get_timeline()
    def __lt__(self, other):
        return self.timestamp < other.timestamp

    def set_user(self, user):
        self.user = user


class TextPost(Post):
    def _extra_name_text(self):
        return self.user.last_name + ': '

    def _extra_post_text(self):
        return ''


class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
        super().__init__(text, timestamp)
        self.url = image_url

    def _extra_name_text(self):
        return self.user.last_name + ': '

    def _extra_post_text(self):
        return self.url + '\n\t'


class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        super().__init__(text, timestamp)
        self.lat = latitude
        self.lon = longitude

    def _extra_name_text(self):
        return 'Checked In: '

    def _extra_post_text(self):
        return '{lat}, {lon}\n\t'.format(lat=str(self.lat), lon=str(self.lon))


