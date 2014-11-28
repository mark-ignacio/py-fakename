# noinspection PyUnresolvedReferences
from six.moves.html_parser import HTMLParser

# noinspection PyUnresolvedReferences
from six.moves.urllib import request
# noinspection PyUnresolvedReferences
from six.moves.urllib.parse import urljoin
import six
import datetime
from fakename import __version__

DOMAIN = 'https://fakena.me/'

# construct a whole bunch of other urls
RANDOM_URL = urljoin(DOMAIN, 'random/')

opener = request.build_opener()
opener.addheaders = [('User-Agent', 'py-fakename-' + __version__)]


# noinspection PyAttributeOutsideInit
class PageParser(HTMLParser):
    # whole lotta' state
    # noinspection PyCompatibility,PyArgumentList
    def reset(self):
        if six.PY3:
            super().reset()
        else:
            # old style invocation for an old style class
            HTMLParser.reset(self)
        self.in_tr = False
        self.in_td = False
        self.tr_key = None
        self.tr_value = None
        self.in_anchor = False
        self.anchor_href = None
        self.identity = {}

    # essentially, we're waiting until we reach the table body to scrape data
    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            self.in_tr = True
        elif tag == 'td':
            self.in_td = True
        elif tag == 'a':
            self.in_anchor = True
            self.anchor_href = dict(attrs)['href']

    def handle_data(self, data):
        # handle_data will only be called once per textNode since we receive the entire page beforehand
        if self.in_td:
            if self.tr_key is None:
                self.tr_key = data.strip()
            elif self.tr_key and self.tr_value is None:
                self.tr_value = data.strip()
        elif self.in_anchor and data.strip() == 'Permalink for this profile':
            self.identity['permalink'] = urljoin(DOMAIN, self.anchor_href)

    def handle_endtag(self, tag):
        if tag == 'td':
            self.in_td = False
        elif tag == 'tr':
            self.in_tr = False
            if self.tr_key and self.tr_value:
                self.identity[self.tr_key] = self.tr_value
                self.tr_key = None
                self.tr_value = None
        elif tag == 'a':
            self.in_anchor = False
            self.anchor_href = None


PARSER = PageParser()


def gen_identity(processed=True):
    page = opener.open(RANDOM_URL).read()
    if six.PY3:
        page = page.decode('utf8')

    PARSER.reset()
    PARSER.feed(page)

    ugly = PARSER.identity

    # no processing whatsoever - even includes the colons!
    if not processed:
        return ugly

    # make it pythonic and parse it out a bit for normal wrapper output
    # namely, work on the DOB + city/state/zip

    # sample: "Malone, KY 41451"
    city, state, zip_code = ugly['City, State, ZIP:'].split(' ', 2)
    city = city.rstrip(',')
    dob = datetime.datetime.strptime(ugly['Date of Birth:'], '%Y-%m-%d')

    identity = {
        'name': ugly['Name:'],
        'dob': dob,
        'address': ugly['Street Address:'],
        'city': city,
        'state': state,
        'zip': zip_code,
        'phone': ugly['Phone Number:'],
        'username': ugly['Username:'],
        'password': ugly['Password:'],
        'temp_email': ugly['Temporary Email Address:'],
        'permalink': ugly['permalink']
    }

    return identity