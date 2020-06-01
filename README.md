# Scraping Real Estate Properties in Cape Town, South Afria with Scrapy


- **residential_people**: Scrapy spider folder
    - spiders/rp.py: the spider
    - base/**base_residential_people.py**: the base spider. Here's the **_ham_**!
- **CapeTown.ipynb**: Jupyter Notebook
- **rp.csv**: the data crawled



The spider goes to [Residential People](https://www.residentialpeople.com/za/) and crawls the following data:
- title: the title of the listed property
- offering: if the property is for sale or to let
- price
- bedrooms: number of bedrooms
- bathrooms: number of bathrooms
- latitude
- longitude
- floor_size
- property_type: apartment, house, townhouse, etc.
- url: url of the listing

