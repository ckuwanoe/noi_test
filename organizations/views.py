from organizations.models import Organization
from organizations.models import Person
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    org_list = Organization.objects.all()
    paginator = Paginator(org_list, 15)
    page = request.GET.get('page')
    try:
        orgs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        orgs = paginator.page(1)
    except TypeError:
        # If page is not an integer, deliver first page.
        orgs = paginator.page(1)        
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        orgs = paginator.page(paginator.num_pages)
    return render_to_response('organizations/index.html', {'orgs': orgs})
    
def detail(request, organization_id):
    org = get_object_or_404(Organization, pk=organization_id)
    return render_to_response('organizations/detail.html', {'org': org})

def people_detail(request, person_id):
    p = get_object_or_404(Person, pk=person_id)
    return render_to_response('organizations/person_detail.html', {'person': p})