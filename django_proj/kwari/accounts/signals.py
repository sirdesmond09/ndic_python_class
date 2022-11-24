import random
from django.dispatch import receiver
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from kwari import settings
from djoser.signals import user_registered, user_activated

from .models import ActivationOtp
from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string


User = get_user_model()
site_name = "#"
url="#"

def generate_otp(n):
    return "".join([str(random.choice(range(10))) for _ in range(n)])


@receiver(post_save, sender=User)
def send_details(sender, instance, created, **kwargs):
    if created and instance.is_superuser!=True and instance.is_admin==True:
        # print(instance.password)
        subject = f"YOUR ADMIN ACCOUNT FOR #".upper()
        
        message = f"""Hi, {str(instance.first_name).title()}.
You have just been onboarded on the # platform. Your login details are below:
E-mail: {instance.email} 
password: {instance.password}    

Regards,
# Support Team   
"""   
        # msg_html = render_to_string('signup_email.html', {
        #                 'first_name': str(instance.first_name).title(),
        #                 'code':code,
        #                 'url':url})
        
        email_from = settings.DEFAULT_FROM_EMAIL
        recipient_list = [instance.email]
        send_mail( subject, message, email_from, recipient_list)
        
        instance.set_password(instance.password)
        instance.save()
        return
    
    
    

            
@receiver(user_registered)
def activate_otp(user, request, *args,**kwargs):
    user.is_active = False
    user.save()
    
    code = generate_otp(6)
    expiry_date = timezone.now() + timezone.timedelta(minutes=10)
    ActivationOtp.objects.create(code=code, expiry_date=expiry_date, user=user)
    
    
    subject = "ACCOUNT VERIFICATION FOR #"
        
    message = f"""Hi, {str(user.first_name).title()}.
Thank you for signing up!
Complete your verification on the {site_name} with the OTP below:

                {code}        

Expires in 5 minutes!

Cheers,
{site_name} Team            
"""   
    msg_html = render_to_string('email/activation.html', {
                    'first_name': str(user.first_name).title(),
                    'code':code,
                    'site_name':site_name,
                    "url":url})
    
    email_from = settings.Common.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    send_mail( subject, message, email_from, recipient_list, html_message=msg_html)
    
    return


@receiver(user_activated)
def comfirmaion_email(user, request, *args,**kwargs):
    
    
    subject = "VERIFICATION COMPLETE"
        
    message = f"""Hi, {str(user.first_name).title()}.
Your account has been activated and is ready to use!

Cheers,
{site_name} Team            
"""   
    msg_html = render_to_string('email/confirmation.html', {
                    'first_name': str(user.first_name).title(),
                    'site_name':site_name,
                    "url":url})
    
    email_from = settings.Common.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    send_mail( subject, message, email_from, recipient_list, html_message=msg_html)
    
    return
        