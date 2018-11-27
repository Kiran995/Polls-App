from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from polls.models import Poll, Question, Option
from polls.serializers import PollSerializer, QuestionSerializer, OptionSerializer

class PollAPIViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('poll_name', 'id')

class QuestionAPIViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'poll')

class OptionAPIViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('question', 'id')