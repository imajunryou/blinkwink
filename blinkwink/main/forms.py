from flask_wtf import Form
from wtforms import FormField, HiddenField, SubmitField, StringField


class KindOfCategoricalForm(Form):

    option_1 = SubmitField("Universal Affirmative")
    option_2 = SubmitField("Universal Negative")
    option_3 = SubmitField("Particular Affirmative")
    option_4 = SubmitField("Particular Negative")


class QuestionForm(Form):
    question = StringField()
    statement = StringField()
    options = FormField(KindOfCategoricalForm)
    answer = HiddenField()
