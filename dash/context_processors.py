from notifications.models import Notification
from badges.models import Award
from django.db.models import Count

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

def leaderboardPos(request):
    l = Award.objects.values('user', 'user__first_name', 'user__last_name').order_by('-total').annotate(total=Count('id'))

    for index, item in enumerate(l):
        if item['user'] == request.user.id:
            return {
                'lb_pos': index+1
            }

    