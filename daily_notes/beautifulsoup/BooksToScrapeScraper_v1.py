# A scraper for the "Books to Scrape" demo site (http://books.toscrape.com/)
# This script will scrape the site for book cover images. 
# The images will be saved in a directory called 'book_cover_thumbnails' in the current working directory.
# The images will be named after the book title and will be saved in .jpg format.
# The script will also create a TSV file called 'book_covers.tsv' in the current working directory.
# The TSV file will contain the book title, image URL, and image file name.
# ------------------------------------------------------------
'''
The script uses the requests and BeautifulSoup libraries to scrape the site.
Change directory to the folder in which you'd like to create your virtual environment(s). 
In my case, that looks something like: 
    cd /Users/golan/Documents/dev/python_virtual_environments
Create a new virtual environment in that directory: 
    python3 -m venv myScrapeVenv 
This will create a subdirectory (myScrapeVenv) containing various files.
Activate the newly created virtual environment: 
    source myScrapeVenv/bin/activate
(You can exit the virtual environment later by typing deactivate.)
Install the required libraries: 
    pip install requests beautifulsoup4

# To execute the script, run the following command in the terminal:
# python3 BooksToScrapeScraper.py
'''

import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save the book cover thumbnail images      
os.makedirs('book_cover_thumbnails', exist_ok=True)

# Create a TSV file to store the book title, image URL, and image file name
tsv_file = open('book_covers.tsv', 'w')
tsv_file.write('Title\tImage URL\tImage File Name\n') # Write the header row

# Scrape the site for book cover images
site_url = 'http://books.toscrape.com/'
response = requests.get(site_url)
response.raise_for_status() # Raise an exception if the response is not successful
soup = BeautifulSoup(response.text, 'html.parser')      
   
# Here is the HTML structure of a book item in the "store", including its cover image:
'''
<article class="product_pod">
    <div class="image_container">
        <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
    </div>
    <p class="star-rating Three">
        <i class="icon-star"></i>
        <i class="icon-star"></i>
        <i class="icon-star"></i>
        <i class="icon-star"></i>
        <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
    <div class="product_price">
        <p class="price_color">£51.77</p>
        <p class="instock availability">
            <i class="icon-ok"></i>
            In stock 
        </p>
        <form>
            <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
        </form>
    </div>
</article>
'''

# Find all the book items on the page 
book_items = soup.find_all('article', class_='product_pod')
for book_item in book_items:
    book_title = book_item.find('h3').find('a').get('title')
    image_url = book_item.find('img').get('src')
    image_url = site_url + image_url.replace('../', '') # Construct the full image URL
    image_file_name = book_title + '.jpg'
    image_file_path = os.path.join('book_cover_thumbnails', image_file_name)
    
    # Download the image
    response = requests.get(image_url)
    response.raise_for_status() # Raise an exception if the response is not successful
    with open(image_file_path, 'wb') as image_file:
        image_file.write(response.content)
    
    # Write the book title, image URL, and image file name to the TSV file
    tsv_file.write(f'{book_title}\t{image_url}\t{image_file_name}\n')

tsv_file.close()

print('Scraping complete!')
print('The book cover images have been saved in the "book_cover_thumbnails" directory.')
print('The book cover details have been saved in the "book_covers.tsv" file.')

# End of script