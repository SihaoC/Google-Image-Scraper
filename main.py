# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
from GoogleImageScrapper import GoogleImageScraper
import os

webdriver_path = os.getcwd()+"\\webdriver\\chromedriver.exe"
image_path = os.getcwd()+"\\photos"
search_key= "cat"
number_of_images = 10 
image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images)
image_urls = image_scrapper.find_image_urls()
image_scrapper.save_images(image_urls)
