from django.shortcuts import render

from .models import Question, Choice

# get questions and display them 
def index (request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# show specific questions and choices 
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=questin_id)
    except Question.DoesNotExist:
        raise Http404("Question Does not Exist")
    return render(request, 'polls/results.html', { 'question': question })

# to show the results of the votes
def results(request, question_id):
    question = get_object_or_404(Question, pk=question.id)
    return render(request, 'polls/results.html', { 'question': question })