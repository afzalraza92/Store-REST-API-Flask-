from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.String(80))
    
    items = db.relationship('ItemModel',lazy='dynamic') #Tells that store has a relationship with ItemModel

    def __init__(self,name):
        self.name=name
        

    def json(self):
        return {'name':self.name,'items':[item.json() for item in self.items.all() ]}
    
    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first() #This is inbuilt in sqlalchemy
        #The above line is equivalent to select * from items where name = name limit 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()