from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Sign(MethodView):
    def get(self):
        return render_template('sign.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.insert(request.form['building_name'], request.form['building_code'], request.form['building_floor'], request.form['room_number'], request.form['rating'])
        return redirect(url_for('index'))
