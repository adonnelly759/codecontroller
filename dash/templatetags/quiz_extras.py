from django import template
#from dash.models import Quiz, QuizAnswer, QuizQuestion 

register = template.Library()

@register.filter
def split_answers(answer_obj, question_id):
    return answer_obj.filter(question = question_id)