from django.db import models
from django.utils.translation import gettext_lazy as _

class Listing(models.Model):
    """
    Model representing a travel listing.
    """
    LISTING_STATUS = (
        ('active', _('Active')),
        ('pending', _('Pending')),
        ('inactive', _('Inactive')),
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=LISTING_STATUS, default='pending')
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title
