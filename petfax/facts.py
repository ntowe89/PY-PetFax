from flask import ( Blueprint, render_template )


bp = Blueprint(
    "facts",
    __name__,
    url_prefix="/facts"
)

@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('facts/index.html')


@bp.route('/new')
def new():
    return render_template('facts/new.html')