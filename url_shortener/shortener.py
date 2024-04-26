#!/usr/bin/python3
# written by: atholcomb
# minimize_url.py
# Takes a given URL and redirects it to a shorter URL

import random
import time
from tqdm import tqdm

# generate hex_code value as subdomain
def generate_subdomain():
  subdomain = ""               # hex formatted string
  hex_code = "ABCDEF12345678"  # hexidecimal 
  for count in range(9):
    subdomain += random.choice(hex_code)
  
  return subdomain

# minimize the URL for the given endpoints
def minimize_url():
  # shortened URL domain
  domain = ".cognishn.io" 
  
  # target endpoints
  endpoints = ['android', 'calendar', 'chromebook',
               'drawings', 'finance', 'drive',
               'contacts', 'chrome', 'gdocs',
               'forms', 'gboard', 'gmail',
               'assistant', 'google_fi',
               'google_fit', 'meet', 'classroom',
               'groups', 'photos', 'home',
               'wallet', 'shopping', 'store',
               'workspace', 'keep', 'lens', 'store'
               'nest', 'news', 'pixel',
               'protect', 'podcasts', 'scholar',
               'search', 'sheets', 'sites', 'slides',
               'translate', 'travel', 'voice', 'waze',
               'youtube'
              ] 
  URL = ""
  print("Endpoint\t\t\tStatus\t\tNew URL")
  for endpoint in endpoints:
    redirect_url = generate_subdomain().lower() + domain
    URL = "google.com/" + endpoint
    print(f"{URL} \t\t\t\thttps://{redirect_url}", end="\t")
    pbar = tqdm(total=25, bar_format="\t\t\t\t{l_bar}")
    for i in range(5):
      time.sleep(0.1)
      pbar.update(5)
    pbar.close()
