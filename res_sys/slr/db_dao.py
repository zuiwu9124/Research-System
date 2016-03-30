from slr.models import *

def get_projects():
	projects = Projects.objects.all()
	return projects