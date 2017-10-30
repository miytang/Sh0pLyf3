# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from django.template import loader

from .models import Question, Recipe

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	return render(request, 'polls/index.html', context)
	# return HttpResponse(template.render(context, request))
	# output = ', '.join([q.question_text for q in latest_question_list])
	# return HttpResponse(output)

def detail(request, question_id):

	question = get_object_or_404(Question, pk=question_id)

	# try:
	# 	question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExist:
	# 	raise Http404("Question does not exist")
	return render(request, 'polls/detail.html', {'question': question})

	# return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
	# return HttpResponse("You're voting on question %s" % question_id)

def test(request, recipe_id):

	recipe = get_object_or_404(Recipe, pk=recipe_id)
	# ingredient = get_object_or_404(Ingredient, pk=recipe_id)

	return render(request, 'polls/test.html', {'recipe': recipe})

# Create your views here.