import sys
import os
import django

sys.path.append("d:\Desktop\sechack\sechack365_0603-master")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SecHack365_0603.settings')


def call():
    django.setup()
    from sample.models import Usb

    usb_list = Usb.objects.all()
    for obj in usb_list:
        print(obj)


if __name__ == '__main__':
    call()