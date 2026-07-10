from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_registration_otp(otp, fname, recipient):
    """
    Send OTP email for registration asynchronously
    """
    subject = 'Verification Code for Registration'
    content = f'''Dear {fname},
    Your 6 digit otp to register Nightshow OTT account is {otp}.
    In case you have not requested to OTP, Ignore or contact Nightshow support team
    We kindly request not to share the otp with anyone. 
    
    Thanks,
    Nightshow OTT'''
    try:
        send_mail(
            subject,
            content,
            'pavanpannati5@gmail.com',
            [recipient],
            fail_silently=False
        )
        return f"OTP email sent successfully to {recipient}"
    except Exception as e:
        return f"Failed to send OTP email: {str(e)}"


@shared_task
def send_login_otp(fname, otp, recipient):
    """
    Send OTP email for login asynchronously
    """
    subject = 'One Time Code for Login'
    content = f'''Dear {fname},
    One Time Password (OTP) to verify your email is {otp}
    In case you have not requested to OTP, Ignore or contact Nightshow support team
    
    Thanks,
    Nightshow OTT'''
    try:
        send_mail(
            subject,
            content,
            'pavanpannati5@gmail.com',
            [recipient],
            fail_silently=False
        )
        return f"Login OTP email sent successfully to {recipient}"
    except Exception as e:
        return f"Failed to send login OTP email: {str(e)}"


@shared_task
def send_password_reset_otp(fname, otp, recipient):
    """
    Send OTP email for password reset asynchronously
    """
    subject = 'Password Reset'
    content = f'''Dear {fname}
    You requested to reset the password for your Nightshow account
    The requested OTP is {otp}. 
    In case you have not requested to OTP, Ignore or contact Nightshow support team
    If you did not request a password reset, please ignore this email or reply to us. 
    
    Thanks,
    Nightshow'''
    try:
        send_mail(
            subject,
            content,
            'pavanpannati5@gmail.com',
            [recipient],
            fail_silently=False
        )
        return f"Password reset OTP email sent successfully to {recipient}"
    except Exception as e:
        return f"Failed to send password reset OTP email: {str(e)}"


@shared_task
def send_successful_registration_email(fname, recipient):
    """
    Send successful registration email asynchronously
    """
    subject = 'Successful registration for your Nightshow account'
    content = f'''Dear {fname}
    You are Successfully registered into Nightshow-OTT account and you won your free membership. valid for a month
    
    Thanks,
    Nightshow'''
    try:
        send_mail(
            subject,
            content,
            'pavanpannati5@gmail.com',
            [recipient],
            fail_silently=False
        )
        return f"Registration confirmation email sent successfully to {recipient}"
    except Exception as e:
        return f"Failed to send registration confirmation email: {str(e)}"
