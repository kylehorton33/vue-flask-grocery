from app import db
from datetime import datetime

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    category = db.Column(db.String(30), default='UNCATEGORIZED')
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Item {self.id}: {self.name}>'