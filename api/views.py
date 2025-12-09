"""
CarePoint Health System - API Module

This is a demo version with core business logic removed.
For the complete, fully functional version, please contact:

Bimal Jayakumar
bimaljayakumar18@gmail.com

The full version includes:
- Complete REST API endpoints
- Authentication and authorization
- Data serialization
- API documentation
- And much more...
"""

from django.http import HttpResponse
from rest_framework.decorators import api_view

# Core API logic removed - Contact: Bimal Jayakumar (bimaljayakumar18@gmail.com)

@api_view(['GET'])
def api_overview(request):
    return HttpResponse("API unavailable. Contact: bimaljayakumar18@gmail.com for full version")
