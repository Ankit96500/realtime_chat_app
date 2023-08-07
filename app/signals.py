from django.dispatch import receiver,Signal

# create signals
notification=Signal()

# recevier function

@receiver(notification)
def show_notification(sender,**kwargs):
    print('notification signal=====================')
    print('sender:',sender)
    print(f'kwargs:{kwargs}')
