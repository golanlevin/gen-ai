# This is Version 3 of a scraper for the "Books to Scrape" demo site (http://books.toscrape.com/)
# This script will scrape the site for book cover images. 
# The images will be saved in a directory called 'book_covers' in the current working directory.
# The images will be named after the book title and will be saved in .jpg format.
# The script will also create a TSV file called 'book_covers.tsv' in the current working directory.
# The TSV file will contain the book title, image URL, and image file name.
#
# This version of the script includes the following improvements:
# - The script now includes a function to scrape the details of a book item: the high-resolution image jpg.
# - The script now allows the saved image files to be named using consecutive numbers instead of book titles.
# - The script now includes a brief delay between requests to avoid overwhelming the server.
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

# Here is the HTML structure of a book item as listed in the "store", including its cover image thumbnail:
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

# Although the small thumbnail image is located at: 
# http://books.toscrape.com/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg
# The high-resolution image (which we want) is located at:
# http://books.toscrape.com/media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg
# The address of the *high-resolution* image is provided in the "product_gallery" div of the book's own page,
# whose URL is provided as a link in the "a" element of the book item:
# http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
'''
<div id="product_gallery" class="carousel">
    <div class="thumbnail">
        <div class="carousel-inner">
            <div class="item active">
                <img src="../../media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg" alt="A Light in the Attic" />
            </div>
        </div>
    </div>
</div>
'''

import time
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save the book cover images     
book_covers_dir = 'book_covers' 
os.makedirs(book_covers_dir, exist_ok=True)

# Create a TSV file to store the image URL, and image file name
tsv_file = open('book_covers.tsv', 'w')
tsv_file.write('Image URL\tImage File Name\n') # Write the header row

# Scrape the site for book cover images
site_url = 'http://books.toscrape.com/'
response = requests.get(site_url)
response.raise_for_status() # Raise an exception if the response is not successful
soup = BeautifulSoup(response.text, 'html.parser')      


# Find the total number of pages
page_number = 1
book_item_count_total = 0
# Set to True to use the book title for the image file name
b_use_book_title_for_image_file_name = False 


while True:

    # Find all the book items on the page 
    book_items = soup.find_all('article', class_='product_pod')
    book_item_count_on_page = 0; # Count the number of book items processed on this page. 

    for book_item in book_items:
        book_item_count_on_page += 1

        # Construct the filename of the image we will save, using the book title.
        book_title = book_item.find('h3').find('a').get('title')

        if b_use_book_title_for_image_file_name:
            image_file_name = book_title
            # Delete (remove) the following characters altogether from the image file name:
            remove_characters = ['\'','/',':','?','!','"','<','>','|','*','\\','\'',')','(',',','.','#','$','@','&','^','%','+','=','~','`',';','[',']','{','}']    
            for char in remove_characters:
                image_file_name = image_file_name.replace(char, '')
            # Replace the following characters with underscores in the image file name:
            replace_characters = [' ','-','\t','\n','\r']
            for char in replace_characters:
                image_file_name = image_file_name.replace(char, '_')
            # Remove characters outside the 7-bit ASCII charset:
            image_file_name = ''.join([i if ord(i) < 128 else '' for i in image_file_name])
            # Convert the image file name to lowercase and limit the length to 60 characters
            image_file_name = image_file_name.lower();
            image_file_name = image_file_name[:60] # Limit the length of the file name to 60 characters
        else:
            # Format with padded zeros to ensure the images are sorted in the correct order
            image_file_name = f'book_cover_{book_item_count_total:05d}'

        image_file_name = image_file_name + '.jpg'
        image_file_path = os.path.join(book_covers_dir, image_file_name)

        # Find the URL of the book's own page. 
        # Deal with the case where the book's own page is on the first page of the site.
        if page_number == 1:
            book_page_url = site_url + book_item.find('h3').find('a').get('href')
        else: 
            book_page_url = site_url + 'catalogue/' + book_item.find('h3').find('a').get('href')
        
        # Open the book's own page to find the high-resolution image URL
        # book_page_url = site_url + book_page_url.replace('../', '') # Construct the full page URL (?)
        response = requests.get(book_page_url)
        # If the response is not successful, skip this book item. 
        if not response.ok:
            print(f'Failed to download book {book_item_count_on_page} on page {page_number}: ' + book_page_url)
            continue

        book_page_soup = BeautifulSoup(response.text, 'html.parser')   
        # Find the high-resolution image URL from within the "product_gallery" div
        image_url = book_page_soup.find('div', id='product_gallery').find('img').get('src')
        # Note that this has the form "../../media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg"
        # Construct the full image URL:
        image_url = site_url + image_url.replace('../', '') # Construct the full image URL
        
        # Download the image
        response = requests.get(image_url)
        # If the response is not successful, skip this book item. 
        if not response.ok:
            print(f'Failed to download image for book {book_item_count_on_page} on page {page_number}: ' + image_file_name)
            continue
        # Save the image to the book_covers directory
        with open(image_file_path, 'wb') as image_file:
            image_file.write(response.content)
            book_item_count_total += 1
        
        # Write the image URL, and image file name to the TSV file
        tsv_file.write(f'{image_url}\t{image_file_name}\n')

        # Print out the count of book items processed (book_item_count_on_page)
        print(f'Processed book {book_item_count_on_page} on page {page_number}: ' + image_file_name)

        # Add a short delay of 400 milliseconds, to avoid overwhelming the server.
        time.sleep(0.4)

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
print('The book cover images have been saved in the ' + book_covers_dir + ' directory.')
print('The book cover details have been saved in the "book_covers.tsv" file.')

# End of script