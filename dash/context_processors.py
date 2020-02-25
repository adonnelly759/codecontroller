from notifications.models import Notification
from badges.models import Award
from django.db.models import Count

def notification_count(request):
    if(request.user.id):
        n = Notification.objects.filter(seen=False, user=request.user)
        n_count = 0

        if n.count() > 0:
            n_count = n.count()

        if n.count() > 9:
            n_count = "9+"

        return {
            'total_notification' : n_count
        }
    else:
        return {}

def get_five_notifications(request):
    if(request.user.id):
        n = Notification.objects.order_by('-sent').filter(seen=False, user=request.user)[:5]
        return {
            'prev_n': n
        }
    else:
        return {}

def leaderboardPos(request):
    if(request.user.id):
        l = Award.objects.values('user', 'user__first_name', 'user__last_name').order_by('-total').annotate(total=Count('id'))

        for index, item in enumerate(l):
            if item['user'] == request.user.id:
                return {
                    'lb_pos': index+1
                }
            else:
                return {
                    'lb_pos': '999'
                }
    else:
        return {'lb_pos': '999'}


    