from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Hardcoded username dan password
USERNAME = "admin"
PASSWORD = "12345"

# Simpan token di memory sederhana (contoh sederhana, tidak disarankan untuk produksi)
TOKENS = set()

@csrf_exempt
def login(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            username = body.get("username")
            password = body.get("password")

            if username == USERNAME and password == PASSWORD:
                # Buat token (di sini sekadar hardcoded contoh sederhana)
                token = "dummy-token-12345"
                TOKENS.add(token)
                return JsonResponse({"message": "Login successful", "token": token}, status=200)
            else:
                return JsonResponse({"message": "Invalid credentials"}, status=401)
        except Exception as e:
            return JsonResponse({"message": "Invalid request", "error": str(e)}, status=400)
    return JsonResponse({"message": "Method not allowed"}, status=405)

@csrf_exempt
def logout(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            token = body.get("token")

            if token in TOKENS:
                TOKENS.remove(token)
                return JsonResponse({"message": "Logout successful"}, status=200)
            else:
                return JsonResponse({"message": "Invalid token"}, status=401)
        except Exception as e:
            return JsonResponse({"message": "Invalid request", "error": str(e)}, status=400)
    return JsonResponse({"message": "Method not allowed"}, status=405)

def login_page(request):
    return render(request, "login.html")
