from distutils.core import setup
setup(
  name = 'Pyarser',
  packages = ['Pyarser'], # this must be the same as the name above
  version = '0.1.0',
  description = 'A Nifty HTML Parser written in Python',
  long_description= """Pyarser is a simple, straight forward HTML parser that allows you to easily harvest text
  inside an HTML document from a link to that website. Examples:\n
  get_site_HTML(link): returns a string of HTML content from a link\n
  get_site_text(link): returns a string of text from a link. This string has all the HTML tags <> removed, along
  with there contents.\n
  search_by_phrase(phrase, link): returns the fragments of text from a link that contain the continuous string phrase.\n
  search_for_words(words, link): returns the fragments of text from a link that contain ANY of the strings in words.\n
  word_count(link): counts the number of text words from a link.\n
  get_HTML_tags(link): returns a list of the tags used in an HTML document from a link.\n
  HTML_to_TXT(link, name): writes a TXT file with the text content from a link. All HTML brackets and tags are moved.\n""",
  author = 'Joshua Weinstein',
  author_email = 'jweinst1@berkeley.edu',
  url = 'https://github.com/jweinst1/Pyarser', # use the URL to the github repo
  download_url = 'https://github.com/jweinst1/Pyrser/tarball/0.1', # I'll explain this in a second
  keywords = ['data_science, web, data, harvesting'], # arbitrary keywords
  classifiers = [],
)

