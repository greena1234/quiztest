from django.shortcuts import render
from quizapp.models import Question, Choice
from django.views import generic
#from django.views.generic TemplateView


# Create your views here.
class QuestionView(generic.TemplateView):
	template_name='question.html'
	model=Question

	def get_context_data(self,**kwargs):
		context = super(QuestionView,self).get_context_data(**kwargs)

		try:
			context['questions']=Question.objects.all()
			print(context)
		except:
			return None
		else:
			return context