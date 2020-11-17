import os
from app import db
from app.models import Item, Category

# run flask commands to create app.db
os.system('flask db init')
os.system('flask db migrate -m \"items table\"')
os.system('flask db upgrade')

# fill app.db with some initial items
base_list = [
  {
    "category":'UNCATEGORIZED',
    "item":'popcorn'
  },
  {
    "category":'PRODUCE',
    "item":'apple'
  },
  {
    "category":'DAIRY / EGGS',
    "item":'cheese'
  },
]

for item in base_list:
  c = Category(name=item['category'])
  db.session.add(c)
  db.session.commit()

  i = Item(name=item['item'], category_id=c.id)
  db.session.add(i)
  db.session.commit()


print('Added initial list:')
for db_item in Item.query.all():
  print(db_item, db_item.category)

print("\nDo you want to create some initial items? (Y or N)")
while True:
 
  user_input = input(">> ")

  if user_input[0].lower() == 'y':
    item_name = input("\nEnter the name of an item: ")
    item = Item(name=item_name)
    db.session.add(item)
    db.session.commit()
    print(f"\nAdded {item}")
    print("\nAdd another? (Y or N)")
    
  elif user_input[0].lower() == 'n':
    break
  
  else:
    print("\nPlease enter valid input")
    print("\tY or N")
