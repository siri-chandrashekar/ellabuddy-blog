from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    email =EmailField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    name = StringField("Author's Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up")

# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email =EmailField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In")

# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment_text = CKEditorField("Leave your comments below", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")