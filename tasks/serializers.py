from decimal import Decimal
from rest_framework import serializers
from .models import Task, Category
from rest_framework.validators import UniqueValidator,UniqueTogetherValidator
import bleach


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']


class TaskSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    name = serializers.CharField(source="title", max_length=100)

    class Meta:
        model = Task
        fields = ['id', 'name', 'status','priority','category','description','due_date']
        validators = [
            UniqueTogetherValidator(
                queryset=Task.objects.all(),
                fields=['name', 'status']
            ),
        ]
        extra_kwargs = {

            'name': {
                'validators': [
                    UniqueValidator(
                        queryset=Task.objects.all()
                    )]}
        }

        def validate(self, data):
            if "name" in data:
                data["name"] = bleach.clean(data["name"])
            if "category" in data:
                data["category"] = bleach.clean(data["category"])
            return data
