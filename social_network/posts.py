from datetime import datetime as dt


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text.lstrip('text=')
        self.timestamp = timestamp
        self.user = None

    def set_user(self, user):
        self.user = user




class TextPost(Post):

    def __str__(self):
        return '@{first} {last}: "{text}"\n\t{timestamp}'.format(
            first = self.user.first_name,
            last = self.user.last_name,
            text = self.text,
            timestamp = self.timestamp.strftime('%A, %b %d, %Y'))


class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
        self.text = text.lstrip('text=')
        self.url = image_url
        self.timestamp = timestamp
        self.user = None

    def __str__(self):
        return '@{first} {last}: "{text}"\n\t{url}\n\t{timestamp}'.format(
            first = self.user.first_name,
            last = self.user.last_name,
            url = self.url,
            text = self.text,
            timestamp = self.timestamp.strftime('%A, %b %d, %Y'))


class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        self.text = text.lstrip('text=')
        self.lat = latitude
        self.lon = longitude
        self.timestamp = timestamp
        self.user = None

    def __str__(self):
        coordinates = '{lat}, {lon}'.format(lat=self.lat, lon=self.lon)
        print(coordinates)
        return '@{first} Checked In: "{text}"\n\t{lat_lon}\n\t{timestamp}'.format(
            first = self.user.first_name,
            text = self.text,
            lat_lon = coordinates,
            timestamp = self.timestamp.strftime('%A, %b %d, %Y'))
