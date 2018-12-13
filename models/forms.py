from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators

class ContactForm(FlaskForm):
    name = StringField("Your Name:", [validators.DataRequired()])
    email = StringField("Your e-mail address:", [validators.DataRequired(), validators.Email("your@email.com")])
    message = TextAreaField("Your message:", [validators.DataRequired()])
    submit = SubmitField("Send Message")
