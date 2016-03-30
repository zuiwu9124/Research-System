from slr.forms import * 


def add_project(form, request):
    cd = form.cleaned_data
    project_title = cd['project_title']
    project_objective = cd['project_objective']

    project = Projects(project_title=project_title,
                       project_objective=project_objective)
    project.save()

def add_project_form():
    form = AddProject()
    return form