# OfferID-Fixer
 This is a simple Python script that takes your Item ID in FurnitureData.json and copies it into the Offer ID, spitting out a file called new_FurnitureData.json. Replace your existing FurnitureData with this one, and purge your personal & Cloudflare Cache

**Please install Python before continuing!**
https://www.python.org/downloads/

**Running OfferId.py**
> 1) Place your FurnitureData.json file in the same directory as the OfferId.py script
> 2) Open CMD Prompt in Script directory
> 3) Type OfferId.py and hit Enter

**Once you have done so, it's important to run this SQL:**
```
UPDATE Catalog_pages
SET offer_id = item_ids
WHERE item_ids NOT LIKE '%;%';
```

