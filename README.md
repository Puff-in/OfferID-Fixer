# OfferID-Fixer
 This is a simple Python script that takes your Item ID in FurnitureData.json and copies it into the Offer ID, spitting out a file called new_FurnitureData.json. Replace your existing FurnitureData with this one, and purge your personal & Cloudflare Cache

**Please install Python before continuing!**
https://www.python.org/downloads/

**Running OfferId.py**
> 1) Place your FurnitureData.json file in the same directory as the OfferId.py script
> 2) Open CMD Prompt in Script directory
> 3) Type OfferId.py and hit Enter

**Once you have done so, it's important to run these SQL's in order:**
```
UPDATE catalog_items
SET offer_id = (
    SELECT sprite_id
    FROM items_base
    WHERE items_base.id = catalog_items.item_ids
    LIMIT 1
)
WHERE item_ids NOT LIKE '%;%';
```
```
UPDATE catalog_items AS ci
JOIN items_base AS ib
  ON ci.item_ids = ib.sprite_id
SET ci.offer_id = LEFT(CONCAT(ib.sprite_id, '97'), 10)
WHERE ib.type = 'i'
  AND ci.item_ids NOT LIKE '%;%';
  ```

After executing these SQL Queries, simply run your :update_catalog command

