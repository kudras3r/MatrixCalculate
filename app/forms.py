
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired


class MatrixForm(FlaskForm):
    num1_00 = IntegerField('num1_00', validators=[DataRequired()])
    num1_01 = IntegerField('num1_01', validators=[DataRequired()])
    num1_02 = IntegerField('num1_02', validators=[DataRequired()])
    num1_10 = IntegerField('num1_10', validators=[DataRequired()])
    num1_11 = IntegerField('num1_11', validators=[DataRequired()])
    num1_12 = IntegerField('num1_12', validators=[DataRequired()])
    num1_20 = IntegerField('num1_20', validators=[DataRequired()])
    num1_21 = IntegerField('num1_21', validators=[DataRequired()])
    num1_22 = IntegerField('num1_22', validators=[DataRequired()])

    num2_00 = IntegerField('num2_00', validators=[DataRequired()])
    num2_01 = IntegerField('num2_01', validators=[DataRequired()])
    num2_02 = IntegerField('num2_02', validators=[DataRequired()])
    num2_10 = IntegerField('num2_10', validators=[DataRequired()])
    num2_11 = IntegerField('num2_11', validators=[DataRequired()])
    num2_12 = IntegerField('num2_12', validators=[DataRequired()])
    num2_20 = IntegerField('num2_20', validators=[DataRequired()])
    num2_21 = IntegerField('num2_21', validators=[DataRequired()])
    num2_22 = IntegerField('num2_22', validators=[DataRequired()])

    plus = SubmitField('+')
    umn = SubmitField('*')
    minus = SubmitField('-')

class NumInput(FlaskForm):
    num = IntegerField('num')
    
class Matrix(FlaskForm):
    nums = FieldList(FormField(NumInput), min_entries=3, max_entries=20)
    submit = SubmitField('+')