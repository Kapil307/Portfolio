from project.wsgi import application
from vercel_wsgi import handle

def handler(request, context):
    return handle(request, application)
