# generate_model.py -- generates a model for use with Flask apps

import sys

from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("."))

template = environment.get_template("model.py.template")

context = {
    "model_name": sys.argv[1],
    "model_table": sys.argv[1]
}

model_file = open(context["model_name"] + ".py", "w")
model_file.write(template.render(context))
model_file.close()

