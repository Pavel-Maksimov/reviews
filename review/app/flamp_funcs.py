import requests
import datetime
from lxml import html
from .settings import TIMEZONE


def extract_reviews(root):
    result = []
    for el in root.find_class('ugc-list__item js-ugc-list-item'):
        for e in el.find_class('ugc-item'):
            for n in e.findall('meta'):
                if n.attrib['itemprop'] == 'datePublished':
                    date_published = datetime.datetime.fromisoformat(
                        n.attrib['content']
                    )
            for n in e.find_class('l-inner l-inner--side-fixed author'):
                for i in n.findall('meta'):
                    if i.attrib['itemprop'] == 'name':
                        name = i.attrib['content']
            for n in e.find_class(
                'l-inner__column l-inner__column--side ugc-item__estimation'
            ):
                for k in n:
                    for i in k.findall('cat-brand-review-estimation'):
                        estimation = i.attrib['estimation']
            for n in e.find_class(
                't-text t-rich-text ugc-item__text ugc-item__text--full js-ugc-item-text-full'
            ):
                text = e.find_class('t-rich-text__p')[-1].text.strip()
            result.append((name, date_published, estimation, text))
    return result


def get_next_pages(root):
    result = []
    for i in root.find_class('list pagination__list pagination__list--pages'):
        for n in i.iter('a'):
            result.append('http:' + n.attrib['href'])
    return result


def get_places(strg):
    res = requests.get(strg)
    root = html.fromstring(res.content.decode())
    result = []
    for i in root.find_class('list-cards__item list-cards__item--card'):
        for n in i.iter('a'):
            if n.attrib['class'] == 'card__link':
                result.append('http:' + n.attrib['href'])
    return result


def scrape_flamp(url, last_visit_time=None):
    last_visit = last_visit_time or datetime.datetime(
        2000,
        1,
        1,
        hour=0,
        minute=0,
        tzinfo=datetime.timezone(
            datetime.timedelta(hours=TIMEZONE))
    )
    res = requests.get(url)
    root = html.fromstring(res.content.decode())
    places_urls = get_places(url)
    for page in get_next_pages(root):
        places_urls += get_places(page)
    extracted_data = []
    for url in places_urls:
        place_res = requests.get(url)
        place_root = html.fromstring(place_res.content.decode())
        for name, date, score, text in extract_reviews(place_root):
            if date > last_visit:
                extracted_data.append((url, name, date, score, text))
    return extracted_data
