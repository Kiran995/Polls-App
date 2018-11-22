from rest_framework import viewsets
from polls.models import Poll, Question, Option
from polls.serializers import PollSerializer, QuestionSerializer, OptionSerializer

class PollAPIViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class QuestionAPIViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class OptionAPIViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Option.objects.all()
    serializer_class = OptionSerializer