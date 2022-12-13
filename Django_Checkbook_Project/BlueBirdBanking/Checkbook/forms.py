from django.forms import ModelForm
from .models import Account, Transaction


#account form
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


#transaction form
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

