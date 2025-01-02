from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class User(models.Model):
    ROLE_CHOICES = [
        ('Police', 'Police'),
        ('Driver', 'Driver'),
        ('Admin', 'Admin'),
    ]

    firstname = models.CharField(null=True, max_length=255)
    lastname = models.CharField(null=True, max_length=255)
    username = models.CharField(null=True, max_length=255, unique=True)
    password = models.CharField(null=True, max_length=755)
    mobile_number = models.CharField(null=True, max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.role})"


class Violation(models.Model):
    name = models.CharField(max_length=255, null=True)
    penalty_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.name if self.name else "Unnamed Violation"

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Resolved', 'Resolved'),
        ('Disputed', 'Disputed'),
    ]

    license_no = models.CharField(max_length=20, null=True)
    plate_number = models.CharField(max_length=20, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='tickets_as_user')
    violation_details = models.ForeignKey(Violation, on_delete=models.CASCADE, null=True)
    fine_amount = models.CharField(max_length=255, null=True)
    issued_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='tickets_as_issuer')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True)

    def __str__(self):
        return f"Ticket {self.id} - {self.user_id} - {self.violation_details}"


class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ]
    
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='payments')
    receipt_image = models.ImageField(upload_to='payment_receipts/', null=True, blank=True)
    status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Payment for Ticket {self.ticket.id} by {self.paid_by.firstname} {self.paid_by.lastname}"



class Dispute(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='disputes')
    filed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='disputes')
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dispute for Ticket {self.ticket.id} by {self.filed_by.firstname}"


