import os

# run flask commands to create app.db
os.system('flask db init')
os.system('flask db migrate -m \"items table\"')
os.system('flask db upgrade')
