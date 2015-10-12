#package top level
import requests
from pyrser.get_text import *
import re

def get_site_HTML(link):
    htmlstr = openers.open_site(link)
    return htmlstr

def get_site_text(link):
    htmlstr = openers.open_site(link)
    pure_text = modifiers.split_from_brackets(htmlstr)
    return pure_text


