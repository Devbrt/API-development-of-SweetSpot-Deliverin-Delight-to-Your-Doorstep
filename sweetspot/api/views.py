from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets,status,permissions
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout
from .models import *
from .serializers import *

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            customer = Customer.objects.get(email=email, password=password)
            return Response({"message": "Login Successful!"})
        except Customer.DoesNotExist:
            return Response({"message": "Invalid credentials"}, status=400)
        
class TokenLogoutView(APIView):
    """Token-based Logout."""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            # Delete the user's token to log them out
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({"message": "Logout successful."}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"error": "Token not found."}, status=status.HTTP_400_BAD_REQUEST)


class SessionLogoutView(APIView):
    """Session-based Logout."""
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful."}, status=status.HTTP_200_OK)        

class CakeCustomizationViewSet(viewsets.ModelViewSet):
    queryset = CakeCustomization.objects.all()
    serializer_class = CakeCustomizationSerializer

    def create(self, request, *args, **kwargs):
        """Handle custom validation for Cake Customization."""
        cake_id = request.data.get('cake')
        customer_id = request.data.get('customer')

        # Check if the cake and customer exist
        try:
            cake = Cake.objects.get(id=cake_id)
            customer = Customer.objects.get(id=customer_id)
        except (Cake.DoesNotExist, Customer.DoesNotExist):
            return Response(
                {"error": "Invalid Cake or Customer ID"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create the customization object
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CakeViewSet(viewsets.ModelViewSet):
    queryset = Cake.objects.all()
    serializer_class = CakeSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
