from rest_framework.views import APIView
from rest_framework.response import Response

from mail.serializers import EmailSerializer
from mail.utils import CustomMassMail

# Create your views here.

class EmailSendAPIView(APIView):
    def post(self, request, *args, **kwargs):
        """
        Send Multiple Emails
        """

        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        email = data["email_from"]
        passw = data["email_passw"]
        recipient_list = data["email_to"]
        fields = data["email_dynamic_fields"]
        subject = data["email_subject"]
        body = data["email_body"]

        c_mail = CustomMassMail(email, passw, subject, body, fields, recipient_list)
        c_mail.custom_send_mass_mail()

        return Response(serializer.validated_data)