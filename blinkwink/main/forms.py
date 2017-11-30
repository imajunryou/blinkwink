from flask_wtf import Form
from wtforms import SelectField


class WhichTransformUsedForm(Form):

    answer = SelectField(
        'Answer',
        choices=[(x, x) for x in range(1, 11)]
    )
