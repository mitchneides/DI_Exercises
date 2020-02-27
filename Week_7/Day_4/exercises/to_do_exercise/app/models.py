from app import db


class ToDoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(90))
    
    def __repr__(self):
        return f"<id: {self.id}> | <task: {self.todo}>"
