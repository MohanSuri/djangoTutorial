from django.shortcuts import render
from models import Question
from serializers import QuestionSerializer
from django.http import HttpResponse
from rest_framework.response import Response
import json
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
# Create your views here.


@api_view(['GET'])
def question_list(request, format=json):
	if request.method == 'GET':
		questions=Question.objects.all()
		serialized_questions=QuestionSerializer(questions, many=True)
		print serialized_questions.data
		print serialized_questions
		return Response(serialized_questions.data)



@csrf_exempt
def addQuestion(request, format=json):
	#Post an order
	if request.method=='POST':
		data = JSONParser().parse(request)
		serializer = QuestionSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=200)
    	else:
        	return JSONRenderer().render(serializer.errors)


class Greeting(APIView):
	def get(self, request):
		return Response('Hello')

	@method_decorator(csrf_exempt)
	def dispatch(self, *args, **kwargs):
		return super(Greeting, self).dispatch(*args, **kwargs)

	def post(self, request, format=json):
		print '----------------------------------------'
		data=JSONParser.parse(request)
		serializer=QuestionSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=200)