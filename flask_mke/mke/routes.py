from flask import Blueprint, request, current_app, render_template

from DB.database import work_with_db
from DB.sql_provider import SQL_Provider
from mke.utils.mke import draw_mke, redraw_elem

mke_app = Blueprint('mke', __name__, template_folder='templates')
provider = SQL_Provider('sql/')


@mke_app.route('/', methods=['GET', 'POST'])
def plot_mke():
    items = work_with_db(current_app.config['DB_CONFIG'], provider.get('mke.sql'))

    if request.method == 'GET':
        plot_url = draw_mke(items)
        return render_template("mke.html", url=plot_url)

    else:
        x = int(request.form['sub.x'])
        y = int(request.form['sub.y'])
        plot_url = redraw_elem(items, x, y)
        return render_template("mke.html", url=plot_url)
