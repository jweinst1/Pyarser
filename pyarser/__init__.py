#package top level
import requests
from pyarser.get_text import *
import re

def get_site_HTML(link):
    htmlstr = openers.open_site(link)
    return htmlstr

def get_site_text(link):
    htmlstr = openers.open_site(link)
    pure_text = modifiers.split_from_brackets(htmlstr)
    pure_text = ''.join(pure_text)
    return pure_text

def search_by_phrase(phrase, link):
    htmlstr = openers.open_site(link)
    pure_text = modifiers.split_from_brackets(htmlstr)
    results = filters.contains_phrase(phrase, pure_text)
    return results

def search_for_words(words, link):
    htmlstr = openers.open_site(link)
    pure_text = modifiers.split_from_brackets(htmlstr)
    result_words = filters.contains_words_spaced(pure_text)
    return result_words

def word_count(link):
    htmlstr = openers.open_site(link)
    pure_text = modifiers.split_from_brackets(htmlstr)
    pure_text = ''.join(pure_text)
    return len(pure_text.split())

def get_HTML_tags(link):
    htmlstr = openers.open_site(link)
    taglist = harvestors.tag_lst(htmlstr)
    return taglist

def HTML_to_TXT(link, name):
    text = get_site_text(link)
    filename = "%s.txt" %(name)
    file = open(filename, "a")
    file.write(text)
    file.close()



