import requests

class openers(object):
    #functions to open websites in raw form of different formats
    def open_site(link):
        portal = requests.get(link)
        try:
            assert type(portal.text) == str
            return portal.text
        except AssertionError:
            return str(portal.text)

    def site_charlst(link):
        return list(openers.open_site(link))

