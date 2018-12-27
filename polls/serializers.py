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


class OptionMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = (
            'id',
            'description'
        )


class NestedQuestionSerializer(serializers.ModelSerializer):
    options = OptionMinSerializer(many=True)

    class Meta:
        model = Question
        fields = (
            'id',
            'question',
            'options'
        )



class NestedPollSerializer(serializers.ModelSerializer):
    questions = NestedQuestionSerializer(many=True)

    def create(self, validated_data):
        print('data', validated_data)
        poll = Poll.objects.create(poll_name=validated_data['poll_name'])
        for each_question in validated_data['questions']:
            question = Question.objects.create(poll_id=poll.id, question=each_question.get('question'))
            for choices in each_question.get('options'):
                choice = Option.objects.create(count=0, description=choices.get('description'), question_id=question.id)
        
        return poll

    def update(self, instance, validated_data):
        for each_question in validated_data['questions']:
            question = Question.objects.create(poll_id=instance.id, question=each_question.get('question'))
            for choices in each_question.get('options'):
                choice = Option.objects.create(count=0, description=choices.get('description'), question_id=question.id)

        return instance
    
    class Meta:
        model = Poll
        fields = (
            'id',
            'poll_name',
            'questions'
        )
