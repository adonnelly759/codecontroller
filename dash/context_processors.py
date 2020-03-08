from notifications.models import Notification
from badges.models import Award
from django.db.models import Count

# Context Processor for Notifcation Counting
def notification_count(request):
    # If request.user exists
    if(request.user.id):
        # Query notification model
        n = Notification.objects.filter(seen=False, user=request.user)
        n_count = 0

        # If count of notifications more than 0
        if n.count() > 0:
            # Set n_count to current notification number
            n_count = n.count()

        # If notifcation exceeds 9
        if n.count() > 9:
            # Set n_count to 
            n_count = "9+"

        # Return n_count
        return {
            'total_notification' : n_count
        }
    else:
        # Return empty object
        return {}

# Get previous five notifications
def get_five_notifications(request):
    if(request.user.id):
        # Notification filter object based on prevoiusly received notifcations
        n = Notification.objects.order_by('-sent').filter(seen=False, user=request.user)[:5]
        return {
            'prev_n': n
        }
    else:
        return {}

# Receive current leaderboard pos
def leaderboardPos(request):
    if(request.user.id):
        # Award object to retrieve the positions of each user
        l = Award.objects.values('user', 'user__first_name', 'user__last_name').order_by('-total').annotate(total=Count('id'))

        # Loop over the intances of each award
        for index, item in enumerate(l):
            # Check if the user = current user
            if item['user'] == request.user.id:
                return {
                    # Add 1 to the index of the indecies 
                    'lb_pos': index+1
                }
            else:
                return {
                    'lb_pos': '999'
                }
    else:
        return {'lb_pos': '999'}


    