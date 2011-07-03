from organizations.models import Organization
from organizations.models import Person
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    orgs = Organization.objects.all()
    return render_to_response('organizations/index.html', {'orgs': orgs})
    
def detail(request, organization_id):
    org = get_object_or_404(Organization, pk=organization_id)
    return render_to_response('organizations/detail.html', {'org': org})

def people_detail(request, person_id):
    p = get_object_or_404(Person, pk=person_id)
    return render_to_response('organizations/person_detail.html', {'person': p})