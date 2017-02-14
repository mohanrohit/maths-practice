from end_statement import end

from flask import request, render_template, url_for, redirect
from flask_classy import FlaskView, route

from app.models import Question

class QuestionsController(FlaskView):
  route_base = "/"

  @route("/questions")
  def index(self):
    questions = Question.query.all()

    return render_template("questions/index.html", questions = questions)
  end

  @route("/questions/<int:id>")
  def get(self, id):
    q = Question.find(id)

    return render_template("questions/get.html", question = q)
  end

  @route("/questions", methods=["POST"])
  def post(self):
    text = request.values.get("text")
    if not text:
      return render_template("error.html")
    end

    q = Question(text=text)
    q.save()

    return redirect(url_for("QuestionsController:index"))
  end
end
