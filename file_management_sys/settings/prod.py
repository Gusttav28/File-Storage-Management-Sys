from .base import *
import dj_database_url

DATABASE = {
    'default': dj_database_url.config(env='DATABASE_URL', conn_max_age=600)
}