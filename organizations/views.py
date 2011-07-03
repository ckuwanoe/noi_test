from organizations.models import Organization
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    orgs = Organization.objects.all()
    return render_to_response('organizations/index.html', {'orgs': orgs})
    
def detail(request, organization_id):
    p = get_object_or_404(Poll, pk=organization_id)
    return render_to_response('organizations/detail.html', {'organization': p})