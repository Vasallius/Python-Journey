# Vasallius

# Import necessary modules
import bs4
import datetime
import requests
import threading
import os


today = datetime.datetime.now()
timechecked = today.strftime('%B %d %Y')

# Open file containing last date checked and last website visited
fhand = open('data.txt', 'r')
lst = fhand.read().split()
date = ' '.join(lst[:3])
xkcd_number = int(lst[3])
lht_number = int(lst[4])
fhand.close()

os.makedirs('./xkcd', exist_ok=True)
os.makedirs('./lht', exist_ok=True)

# Check for current xkcd comic number
r1 = requests.get('https://xkcd.com')
r1.raise_for_status
soup1 = bs4.BeautifulSoup(r1.text,'html.parser')
current_xkcd_link = soup1.select('meta')[3].get('content')
current_xkcd_number = int(current_xkcd_link[17:-1])

# Check for current lht comic number
r2 = requests.get('http://www.lefthandedtoons.com/')
r2.raise_for_status
soup2 = bs4.BeautifulSoup(r2.text,'html.parser')
current_lht_link = soup2.find('div', class_ = 'comictitlearea').a.get('href')
current_lht_number = int(current_lht_link[31:-1])

def download_xkcd(start_comic,end_comic):
    # Download comic
    for i in range(start_comic,end_comic):
        response = requests.get(f'https://xkcd.com/{i}/') 
        response.raise_for_status
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        comic_elem = soup.select('div#comic img')
        try:
            image_url = comic_elem[0].get('src')
            response = requests.get(f'https:{image_url}')
            response.raise_for_status
            image_file = open(os.path.join('xkcd',os.path.basename(image_url)),'wb')
            for chunk in response.iter_content(100000):
                image_file.write(chunk)
            
        except:
            print(f'image cannot be found at https://xkcd.com/{i}/')

# Check if we are up to date         
if xkcd_number == current_xkcd_number:
    print((f'No updates have been made since {date}'))
else:
    download_threads = []
    # Start a thread per 10 comics to make download efficient
    for i in range (xkcd_number,current_xkcd_number+1,10):
        start = i
        end = i + 10
        if start == 0:
            start = 1
        # Each thread downloads 10 comics
        download_thread = threading.Thread(target=download_xkcd,args=(start,end))
        download_threads.append(download_thread)
        download_thread.start()
    # Wait for threads to finish
    for downloadThread in download_threads:
        downloadThread.join()

def download_lht(start_comic,end_comic):
    # Download comic
    for i in range(start_comic,end_comic):
        response = requests.get(f'http://www.lefthandedtoons.com/{i}/') 
        response.raise_for_status
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        try:
            image_url = soup.find('img' , class_='comicimage').get('src')
            response = requests.get(image_url)
            response.raise_for_status
            image_file = open(os.path.join('lht',os.path.basename(image_url)),'wb')
            for chunk in response.iter_content(100000):
                image_file.write(chunk)

        except:
            print(f'image cannot be found at http://www.lefthandedtoons.com/{i}/')

if lht_number == current_lht_number:
    print((f'No updates have been made since {date}'))
else:
    download_threads = []
    # Start a thread per 10 comics to make download efficient
    for i in range (lht_number,current_lht_number+1,10):
        start = i
        end = i + 10
        if start == 0:
            start = 1
        # Each thread downloads 10 comics
        download_thread = threading.Thread(target=download_lht,args=(start,end))
        download_threads.append(download_thread)
        download_thread.start()
    # Wait for threads to finish
    for downloadThread in download_threads:
        downloadThread.join()

fhand = open('data.txt', 'w')
fhand.write(f'{timechecked} ')
fhand.write(f'{str(current_xkcd_number)} ')
fhand.write(f'{str(current_lht_number)} ')
fhand.close()
print('Done.')