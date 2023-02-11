from .models import JungBo
from rest_framework import serializers

class JungBoSerializer(serializers.ModelSerializer):
   # user = serializers.ReadOnlyField(source = 'user.nickname')
   # notebook = serializers.ChoiceField(choices=['O','X'])
   # track = serializers.ChoiceField(choices=['UI/UX', 'Front-end', 'Back-end'])
   # session = serializers.ChoiceField(choices=['O', 'X'])

   class Meta:
      model = JungBo
      #  fields = ['name', 'Department', 'studentid', 'grade', 'phone', 'email', 'content', 'track', 'cooperation', 'spend_time', 'created_at']
      fields = '__all__'