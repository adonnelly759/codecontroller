from notifications.models import Notification

def notification_count(request):
    try:
        n = Notification.objects.filter(seen=False, user=request.user)

        if n.count() > 0:
            n_count = n.count()

        if n.count() > 9:
            n_count = "9+"

        return {
            'total_notification' : n_count
        }
    except Exception:
        return {
            'total_notification' : 0
        }

def get_five_notifications(request):
    try:
        n = Notification.objects.order_by('-sent').filter(seen=False, user=request.user)[:5]
        return {
            'prev_n': n
        }
    except Notification.DoesNotExist:
        return {
            'prev_n': None
        }

    