# from django.contrib.auth.backends import ModelBackend
# from reviewer.models import Reviewer_data

# class ReviewerEmailBackend(ModelBackend):
#     def authenticate(self, request, email=None, password=None, **kwargs):
#         print(f"Attempting to authenticate with email: {email}")
#         try:
#             user = Reviewer_data.objects.get(email=email)
#             if user.check_password(password):
#                 print("Authentication successful.")
#                 return user
#         except Reviewer_data.DoesNotExist:
#             print("User not found.")
#             return None
