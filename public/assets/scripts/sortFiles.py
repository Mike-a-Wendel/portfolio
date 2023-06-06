# ----------------------------------------------
# sortFiles.py - mikeawendel@gmail.com 
# Sort files into folders based on map topicrefs.
# 
# See commit history for change details
# -----------------------------------------------

import os
import shutil
from bs4 import BeautifulSoup

def sort_files(ditamap, source_folder, target_folder):
    # parse ditamap file
    with open(ditamap, 'r') as file:
        soup = BeautifulSoup(file, 'xml')

    # create target folder if it doesn't exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # get map info and topicrefs
    mapinfos = {}
    for topicref in soup.find_all('topicref'):
        mapinfo = topicref.find_parent('map')
        if mapinfo:
            mapinfos.setdefault(mapinfo.get('id'), []).append(topicref.get('href'))

    # iterate through mapinfos dictionary
    for mapid, hrefs in mapinfos.items():
        # create folder for file copies if it doesn't exist
        mapinfo_folder = os.path.join(target_folder, mapid)
        if not os.path.exists(mapinfo_folder):
            os.makedirs(mapinfo_folder)

        # copy source files to new folder
        for href in hrefs:
            source_file = os.path.join(source_folder, href)
            target_file = os.path.join(mapinfo_folder, href)
            shutil.copy2(source_file, target_file)

if __name__ == '__main__':
    ditamap = input('Enter the path to the DITA map file: ')
    source_folder = input('Enter the path to the source folder: ')
    target_folder = input('Enter the path to the target folder: ')
    sort_files(ditamap, source_folder, target_folder)
