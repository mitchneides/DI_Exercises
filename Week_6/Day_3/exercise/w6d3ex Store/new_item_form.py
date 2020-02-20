import flask_wtf
import wtforms
from wtforms import validators


class New_Item_Form(flask_wtf.FlaskForm):
    name = wtforms.StringField("Item Name", [validators.data_required()])
    price = wtforms.StringField("Price", [validators.data_required()])
    amount = wtforms.StringField("Qty", [validators.data_required()])
    image = wtforms.StringField("Image file", [validators.data_required()])
    submit = wtforms.SubmitField("Submit")