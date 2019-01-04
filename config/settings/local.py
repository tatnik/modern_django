from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='lvrnm2@#t+_bm7cereq*62@!2b5ou_gw$dg9jts%(4z7e#(sb7')
DEBUG = env.bool('DJANGO_DEBUG', default=True)
