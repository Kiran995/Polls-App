from polls.models import Poll, Question, Option
from rest_framework import serializers

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class NestedQuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = (
            'id',
            'question',
            'poll',
            'options'
        )

class NestedPollSerializer(serializers.ModelSerializer):
    questions = NestedQuestionSerializer(many=True)
        
    class Meta:
        model = Poll
        fields = (
            'id',
            'poll_name',
            'questions'
        )
