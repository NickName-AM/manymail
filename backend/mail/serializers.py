from rest_framework import serializers


# List of dynamic fields: ["<<name>>", "<<address>>"]
class EmailBodyDynamicFieldsListField(serializers.ListField):
    child = serializers.CharField()

# List of dynamic data to replace dynamic fields: ["John Doe", "Street X"]
class EmailBodyDynamicDataListField(serializers.ListField):
    child = serializers.CharField()

# Holds email recipeint and list of dynamic data to replace with the dynamic fields
# {"email_to": "somemail@gmail.com", "email_change_data": ["data1", "data2"]}
class EmailRecipientDynamicDataSerializer(serializers.Serializer):
    email_to = serializers.EmailField()
    email_change_data = EmailBodyDynamicDataListField()

# The format for this serializer is given below this class
class EmailSerializer(serializers.Serializer):
    email_from = serializers.EmailField(required=True)
    email_passw = serializers.CharField()
    email_to = serializers.ListField(child=EmailRecipientDynamicDataSerializer())
    email_dynamic_fields = EmailBodyDynamicFieldsListField()
    email_subject = serializers.CharField()
    email_body = serializers.CharField()


# The following is a json data example
"""
{
    "email_from": "some@gmail.com",
    "email_passw": "password123",
    "email_to": [
        {
            "email_to": "someemail@gmail.com",
            "email_change_data": ["data1,", "data2", ...]
        },
        ...
    ],
    "email_dynamic_fields": ["<<name>>", "<<address>>"],
    "email_subject": "This is test subject",
    "email_body": "This is my email body, <<name>> needs to be replaced for every recipient. The recipient's known address is <<address>>",
}
"""