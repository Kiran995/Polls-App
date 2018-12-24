from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from polls.models import Poll, Question, Option
from polls.serializers import PollSerializer, QuestionSerializer, OptionSerializer, NestedPollSerializer, NestedQuestionSerializer

class PollAPIViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = {
        'poll_name' : ['icontains'],
        'id' : ['exact']
        }
  
class QuestionAPIViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = {
        'id' : ['exact'],
        'question' : ['icontains'],
        'poll' : ['exact']
        }

class OptionAPIViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    filter_backends = (DjangoFilterBackend,)

class NestedPollAPIViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Poll.objects.all()
    serializer_class = NestedPollSerializer
    filter_backends = (DjangoFilterBackend,)