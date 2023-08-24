from flask import render_template
from flask.views import MethodView
import gbmodel

class details(MethodView):
    def get(self):
        model = gbmodel.get_model()
        entries = [dict(building_name=row[0],building_code=row[1],building_floor=row[2],room_number=row[3],rating=row[4]) for row in model.select()]
        return render_template('details.html', entries=entries)
