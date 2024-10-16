from django.db import models

class Customer(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)  
    phone_no = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)

class Cake(models.Model):
    name = models.CharField(max_length=100)
    flavour = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='cakes/')
    available = models.BooleanField(default=True)

class CakeCustomization(models.Model):
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    message = models.CharField(max_length=200, blank=True)
    egg_version = models.BooleanField()
    toppings = models.CharField(max_length=100)
    shape = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cakes = models.ManyToManyField(Cake, through='CartItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)


class CakeCustomization(models.Model):
    message = models.CharField(max_length=200, blank=True)
    egg_version = models.BooleanField()
    toppings = models.CharField(max_length=100)
    shape = models.CharField(max_length=50)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    customization = models.ForeignKey(CakeCustomization, null=True, on_delete=models.SET_NULL)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_address = models.TextField()
    order_status = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
