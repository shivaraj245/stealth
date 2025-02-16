from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import logging
from .models import SustainabilityAction

# Configure logging
logger = logging.getLogger(__name__)

# ✅ Home route to check API status
def home(request):
    return JsonResponse({"message": "Welcome to the Sustainability API"})

# ✅ Get all sustainability actions
@api_view(["GET"])
def list_actions(request):
    try:
        actions = SustainabilityAction.objects.all().values()
        return Response(actions, status=200)
    except Exception as e:
        logger.error(f"❌ Error fetching actions: {e}")
        return Response({"error": "Internal Server Error"}, status=500)

# ✅ Add a new sustainability action
@api_view(["POST"])
def create_action(request):
    try:
        data = request.data
        action_name = data.get("action")
        action_date = data.get("date")
        action_points = data.get("points")

        # Validate required fields
        if not action_name or not action_date or action_points is None:
            return Response({"error": "Missing required fields"}, status=400)

        # Validate points is an integer
        try:
            action_points = int(action_points)
        except ValueError:
            return Response({"error": "Points must be an integer"}, status=400)

        action = SustainabilityAction(action=action_name, date=action_date, points=action_points)
        action.save()

        return Response({"message": "Action added successfully"}, status=201)

    except Exception as e:
        logger.error(f"❌ Error adding action: {e}")
        return Response({"error": "Internal Server Error"}, status=500)

# ✅ Delete an action
@api_view(["DELETE"])
def remove_action(request, action_id):
    try:
        action = get_object_or_404(SustainabilityAction, id=action_id)
        action.delete()
        return Response({"message": "Action deleted successfully"}, status=200)

    except Exception as e:
        logger.error(f"❌ Error deleting action: {e}")
        return Response({"error": "Internal Server Error"}, status=500)
