from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PhoneDirectoryEntry, SimCardData, LeakedIdentityData
from .serializers import PhoneDirectoryEntrySerializer, SimCardDataSerializer, LeakedIdentityDataSerializer
from django.conf import settings
import requests
from backend.scraper.api_connector import NumVerifyAPIConnector

class MobileNumberLookupView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        recaptcha_token = request.data.get('recaptcha_token')

        # Verify reCAPTCHA
        if not self.verify_recaptcha(recaptcha_token):
            return Response({'error': 'Invalid reCAPTCHA'}, status=status.HTTP_400_BAD_REQUEST)

        if not phone_number:
            return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Lookup data from models
        phone_entry = PhoneDirectoryEntry.objects.filter(number=phone_number).first()
        sim_entry = SimCardData.objects.filter(number=phone_number).first()
        leaked_entry = LeakedIdentityData.objects.filter(phone=phone_number).first()

        # External API lookup for location detection and carrier info
        numverify_api_key = settings.NUMVERIFY_API_KEY
        numverify_connector = NumVerifyAPIConnector(api_key=numverify_api_key)
        external_data = numverify_connector.validate_number(phone_number) if numverify_api_key else None

        # Intelligence score calculation (simple heuristic)
        score = 0
        if phone_entry:
            score += 30
        if sim_entry:
            score += 30
        if leaked_entry:
            score += 20
        if external_data:
            score += 20

        # Social profile linking placeholder (to be implemented)
        social_profiles = {
            'telegram': None,
            'whatsapp': None,
            'facebook': None,
        }

        data = {
            'phone_number': phone_number,
            'name': phone_entry.name if phone_entry else (external_data.get('name') if external_data else None),
            'region': phone_entry.region if phone_entry else (external_data.get('location') if external_data else None),
            'sim_provider': sim_entry.provider if sim_entry else (external_data.get('carrier') if external_data else None),
            'carrier_type': sim_entry.carrier_type if sim_entry else (external_data.get('line_type') if external_data else None),
            'leaked_info': {
                'name': leaked_entry.name if leaked_entry else None,
                'address': leaked_entry.address if leaked_entry else None,
            },
            'intelligence_score': score,
            'social_profiles': social_profiles,
        }

        return Response(data)

    def verify_recaptcha(self, token):
        if not token:
            return False
        secret_key = settings.RECAPTCHA_SECRET_KEY
        url = 'https://www.google.com/recaptcha/api/siteverify'
        payload = {
            'secret': secret_key,
            'response': token
        }
        response = requests.post(url, data=payload)
        result = response.json()
        return result.get('success', False)
