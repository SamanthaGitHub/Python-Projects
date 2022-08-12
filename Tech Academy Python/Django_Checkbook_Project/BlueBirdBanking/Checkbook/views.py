from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


# renders Home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == "POST":
        pk = request.POST['account'] # when submitted, retrieve user's account
        return balance(request, pk) # calls balance function for that account's balance sheet
    content = {'form': form}
    return render(request, 'checkbook/index.html', content)


# renders Create New Account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None)  # retrieves the account form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index') # returns user back to Home page
    content = {'form': form} # save content to the template as a dictionary
    # adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)


# renders Balance page when requested
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)  # retrieves account using pk
    transactions = Transaction.Transactions.filter(account=pk)  # retrieves all account's transactions
    current_total = account.initial_deposit
    table_contents = {}  # creates dictionary to hold transaction info
    for t in transactions:  # loops to differentiate withdrawls and deposits
        if t.type == 'Deposit':
            current_total += t.amount
            table_contents.update({t: current_total})
        else:
            current_total -= t.amount
            table_contents.update({t: current_total})
        # passes account, account total balance, and transaction info to the template
        content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
        return render(request, 'checkbook/BalanceSheet.html', content)


# renders Transaction page when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None) # retrieves the transaction form
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['account'] # retrieves which account the transaction was for
            form.save()
            return balance(request, pk) # renders the balance of the account's Balance Sheet
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)
