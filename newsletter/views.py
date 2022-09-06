from django.shortcuts import render, HttpResponseRedirect, reverse
from blog.views import sitewide
from newsletter import validation_utility
from newsletter.models import Subscriber

import utility
import email_utility
from assets import constants
# Create your views here.

def subscribeForm(request):
    context = {
        'sitewide': sitewide
    }
    return render(request, 'newsletter/subscribe_form.html', context)

def subscribe(request):
    post_data = request.POST.copy()
    email = post_data.get("email", None)

    error_msg = validation_utility.validate_email(email)
    if error_msg:
        print(error_msg)
        return HttpResponseRedirect(reverse('blog:recentPostList'))

    if save_email(email):
        token = encrypt(email + constants.SEPARATOR + str(time.time()))
        subscription_confirmation_url = request.build_absolute_uri(reverse('newsletter:subscription_confirmation')) + "?token=" + token
        status = email_utility.send_subscription_email(email, subscription_confirmation_url)
    else:


def save_email(email):
    try:
        subscribe_model_instance = Subscriber.objects.get(email=email)
    except ObjectDoesNotExist as e:
        subscribe_model_instance = Subscriber()
        subscribe_model_instance.email = email
    except Exception as e:
        # logging.getLogger("error").error(traceback.format_exc())
        return False

    # does not matter if already subscribed or not...resend the email
    subscribe_model_instance.status = constants.SUBSCRIBE_STATUS_SUBSCRIBED
    subscribe_model_instance.created_date = utility.now()
    subscribe_model_instance.updated_date = utility.now()
    subscribe_model_instance.save()
    return True