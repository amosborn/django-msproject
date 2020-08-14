from django import forms
from .models import Bid


class BidForm(forms.ModelForm):
    """Form for placing a bid"""

    class Meta:
        model = Bid
        fields = ('bid_amount',)
