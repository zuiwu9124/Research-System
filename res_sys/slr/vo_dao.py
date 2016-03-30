from slr import db_dao

def my_project_list():
	project_list = db_dao.get_projects()
	return project_list