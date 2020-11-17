import os
from app import db
from app.models import Item

# run flask commands to create app.db
os.system('flask db init')
os.system('flask db migrate -m \"items table\"')
os.system('flask db upgrade')

# fill app.db with some initial items
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
