from app.database import db

class Taxi(db.Model):
    __tablename__="taxis"
    id=db.Column(db.Integer, primary_key=True)
    chofer=db.Column(db.String(50), nullable=False)
    color=db.Column(db.String(50), nullable=False)
    frec=db.Column(db.Boolean, nullable=False)
    ingresos=db.Column(db.Float(), nullable=False)
    
    def __init__(self, chofer, color , frec, ingresos):
        self.chofer=chofer
        self.color=color
        self.frec=frec
        self.ingresos=ingresos
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod    
    def get_all():
        return Taxi.query.all()
    
    @staticmethod
    def get_id(id):
        return Taxi.query.get(id)
        
    def update(self,  chofer=None, color=None , frec=None, ingresos=None):
        if chofer is not None:
            self.chofer=chofer
        if color is not None:
            self.color=color
        if frec is not None:
            self.frec=frec
        if ingresos is not None:
            self.ingresos=ingresos
        db.session.commit()
        
        