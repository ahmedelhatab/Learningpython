from exchangelib import Credentials, Account

credentials = Credentials('ahmad.ali', 'Areyouready@Home')
account = Account('ahmad.ali@te.eg', credentials=credentials, autodiscover=True)

for item in account.inbox.all().order_by('-datetime_received')[:100]:
    print(item.subject, item.sender, item.datetime_received)