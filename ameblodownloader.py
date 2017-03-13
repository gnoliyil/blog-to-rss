# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs
from pymongo import MongoClient
import urllib2
from downloader import Downloader

class AmebloDownloader(Downloader):
    def __init__(self, db, url, config):
        self.db = db
        self.url = url
        self.config = config

    def fetch_article_list(self):
        """
        Fetch a list of latest articles in a certain blog
        :return: a list with [ {title, datetime, url}, {title, datetime, url} ]
        """
        pass

    def fetch_article(self, article_url):
        """
        Fetch article contents (and images) from a certain url
        :param article_url: url of that article
        :return:
        { contents: <html>,
          images: [a list of image url, which can be replaced later]
        }
        """
        pass

    def fetch_images(self, response):
        """
        Fetch all images to a folder
        :param response: response from fetch_article
        :return: new response with
        { contents: <html> with url of images replaced,
          images: [ {url, path} ]
        }
        """
        pass

    def update_db(self):
        """
        fetch article list, filter those who are not in the database and add them
        :return:
        """
        pass