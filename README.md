# Ip_restriction_django
A middleware to filter ip address of request and make decision which ip to block or which not.

First make middleware class inside any app and register it in MIDDLEWARE array in settings.py file, you are done.

In middleware class i just get the request ip and check with my ip array. for big projects you can store ip in database and get them from database and check.
