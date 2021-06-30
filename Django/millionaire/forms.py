# from flask_wtf import FlaskForm
# from wtforms import StringField,SubmitField
# from wtforms.validators import DataRequired
#
# class PLAY_Form(FlaskForm):
#     fnum = StringField("Your Answer:",validators = [DataRequired()])
#     play = SubmitField("Ok")

from django import forms


class PlayForm(forms.Form):
    answer = forms.CharField()


class AddQuestionForm(forms.Form):
    question = forms.CharField(widget=forms.Textarea)
    answer1 = forms.CharField(max_length=20)
    answer2 = forms.CharField(max_length=20)
    answer3 = forms.CharField(max_length=20)
    answer4 = forms.CharField(max_length=20)
    right_answer = forms.CharField(max_length=20)