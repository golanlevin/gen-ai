# This is Version 2 of a scraper for the "Books to Scrape" demo site (http://books.toscrape.com/)
# This script will scrape the site for book cover thumbnails. 
# The images will be saved in a directory called 'book_cover_thumbnails' in the current working directory.
# The images will be named after the book title and will be saved in .jpg format.
# The script will also create a TSV file called 'book_covers.tsv' in the current working directory.
# The TSV file will contain the book title, image URL, and image file name.
#
# This version of the script includes the following improvements:
# - Instead of just getting the book cover images from the first page, the script now scrapes all the pages of the site
# - The image filenames are scrubbed to remove problematic characters, such as colons, slashes, and question marks.
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

# Create a directory to save the book cover images
book_cover_thumbnail_dir = 'book_cover_thumbnails'    
os.makedirs(book_cover_thumbnail_dir, exist_ok=True)

# Create a TSV file to store the image URL, and image file name
tsv_file = open('book_covers.tsv', 'w')
tsv_file.write('Image URL\tImage File Name\n') # Write the header row

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

# Furthermore: to scrape all the pages of the site, we need to find the total number of pages. 
# The total number of pages is indicated at the bottom of the page, in the following HTML structure.
# Note that there may be NO such element on the page, in which case we can assume there is only one page.
# Also note that the NEXT button does not exist on the last page, so we can use that to determine when to stop. 
# Also note that the page numbering is 1-based, not 0-based.
# Also note that the number of pages is stored in the "li" element with the class "current".
# Pages have URLs in the form: http://books.toscrape.com/catalogue/page-2.html
# Here is the HTML structure of the page navigation:
'''
<div>
    <ul class="pager">
        <li class="previous"><a href="page-1.html">previous</a></li>
        <li class="current">
            Page 2 of 50
        </li>
        <li class="next"><a href="page-3.html">next</a></li>
    </ul>
</div>
'''

# Find the total number of pages
page_number = 1
while True:

    # Find all the book items on the page 
    book_items = soup.find_all('article', class_='product_pod')
    book_item_count = 0; # Count the number of book items processed

    for book_item in book_items:
        book_title = book_item.find('h3').find('a').get('title')
        image_url = book_item.find('img').get('src')
        image_url = site_url + image_url.replace('../', '') # Construct the full image URL
        image_file_name = book_title

        # Delete (remove) the following characters altogether from the image file name:
        remove_characters = ['\'','/',':','?','!','"','<','>','|','*','\\','\'',')','(',',','.','#','$','@','&','^','%','+','=','~','`',';','[',']','{','}']    
        for char in remove_characters:
            image_file_name = image_file_name.replace(char, '')
        # Replace the following characters with underscores in the image file name:
        replace_characters = [' ','-','\t','\n','\r']
        for char in replace_characters:
            image_file_name = image_file_name.replace(char, '_')
        # Remove characters outside of 7-bit ASCII:
        image_file_name = ''.join([i if ord(i) < 128 else '' for i in image_file_name])
        # Convert the image file name to lowercase and limit the length to 60 characters
        image_file_name = image_file_name.lower();
        image_file_name = image_file_name[:60] # Limit the length of the file name to 60 characters
        image_file_name = image_file_name + '.jpg'
        image_file_path = os.path.join(book_cover_thumbnail_dir, image_file_name)
        
        # Download the image
        response = requests.get(image_url)
        response.raise_for_status() # Raise an exception if the response is not successful
        with open(image_file_path, 'wb') as image_file:
            image_file.write(response.content)
        
        # Write the image URL, and image file name to the TSV file
        tsv_file.write(f'{image_url}\t{image_file_name}\n')

        # Print out the count of book items processed (book_item_count)
        book_item_count += 1
        print(f'Processed {book_item_count} book items on page {page_number}.')

    # Find the next page URL
    next_page = soup.find('li', class_='next')
    if next_page:
        page_number += 1
        next_page_url = site_url + 'catalogue/page-' + str(page_number) + '.html'
        response = requests.get(next_page_url)
        response.raise_for_status() # Raise an exception if the response is not successful
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        break


tsv_file.close()

print('Scraping complete!')
print('The book cover images have been saved in the ' + book_cover_thumbnail_dir + ' directory.')
print('The book cover details have been saved in the "book_covers.tsv" file.')

# End of script