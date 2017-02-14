# question.py -- the Question model

from end_statement import end

from abstract_model import Model, db

class Question(Model):
  __tablename__ = "questions"

  id = db.Column(db.Integer, primary_key=True, index=True, unique=True, autoincrement=True)
  text = db.Column(db.String, nullable=False)

  def __init__(self, **kwargs):
    Model.__init__(self, **kwargs)
  end

  def __repr__(self):
    return self.text
  end
end
