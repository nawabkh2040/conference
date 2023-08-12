
# from .models import singup
# from django.contrib.auth.backends import BaseBackend

# class CustomBackend(BaseBackend):
#     def authenticate(self, request, email=None, password=None):
#         try:
#             users = singup.objects.filter(email=email)
#             for user in users:
#                 if user.password == password:
#                     return user
#         except singup.DoesNotExist:
#             return None

#     def get_user(self, user_id):
#         try:
#             return singup.objects.get(pk=user_id)
#         except singup.DoesNotExist:
#             return None

