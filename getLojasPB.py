from bs4 import BeautifulSoup
import requests
import sys

lojas = open("lojas.html", 'r')
site = BeautifulSoup(lojas, "html.parser")
#site.encode("utf-8")
mydivs = site.findAll("p", { "class" : "address" })
print mydivs