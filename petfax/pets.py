from flask import ( Blueprint, render_template )
import json

pets = json.load(open("pets.json"))

bp = Blueprint(
    "pets",
    __name__,
    url_prefix="/pets"
)

@bp.route("/")
def index():
    return render_template(
        'pets/index.html',
        title="This is PetFax",
        pets=pets
    )

@bp.route('/<int:id>')
def show(id):
    return render_template(
        'pets/show.html', 
        pets=pets[id - 1]
    )

@bp.route("/adopt")
def adopt():
    return "I have adopted a pet!"