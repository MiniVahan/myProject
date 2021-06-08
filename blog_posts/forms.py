# blog_posts/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed


class BlogPostForm(FlaskForm):
    picture = FileField('Add a picture', validators=[FileAllowed(['jpg', 'png'])])
    title = StringField('Car name',validators=[DataRequired()])
    text = TextAreaField('Description', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    submit = SubmitField('Post')