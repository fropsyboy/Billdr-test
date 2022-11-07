import uuid
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class Homeowner:
    name: str = None
    email: str = None
    created_at: str = None


class Contractor:
    name: str = None
    email: str = None
    created_at: str = None
    is_active = None


class Project:
    id: str
    homeowner: Homeowner
    contractor: Contractor
    name: str = None
    minBudget: float = None
    maxBudget: float = None
    total_number = int

    def display_budget(self):
        if self.minBudget > 5000 and self.maxBudget < 10000:
            return '$5K to $10k'

        if self.minBudget > 10000 and self.maxBudget < 20000:
            return '$10K to $20k'

        if self.minBudget > 20000 and self.maxBudget < 30000:
            return '$20K to $30k'

        if self.minBudget > 30000:
            return 'More than $30k'

    def __init__(self, homeowner: Homeowner, contractor: Contractor):
        self.id = str(uuid.uuid4())
        self.homeowner = homeowner
        self.contractor = contractor


class APIProject:
    @action(detail=False, methods=['post'])
    def create(self, request):
        homeowner_1 = Homeowner.objects.get(id__exact=request.data.homeowner_id)
        contractor_1 = Contractor.objects.get(id__exact=request.data.contractor_id)

        project = Project(contractor_1, homeowner_1)
        project.name = request.data.name
        project.minBudget = request.data.min_budget
        project.maxBudget = request.data.max_budget
        project.save()

        return Response(status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'])
    def get(self, id):
        project = Project.objects.get(id__exact=id)

        data = {
            'id': project.id,
            'name': project.name,
            'homeowner_name': project.homeowner.name,
            'contractor_name': project.contractor.name,
            'budget': project.display_budget(),
            'total_number': project.total_number,
        }

        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['put'])
    def update(self, request, id):
        project = Project.objects.get(id__exact=id)
        project.name = request.data.name
        project.minBudget = request.data.min_budget
        project.maxBudget = request.data.max_budget
        project.save()

        data = {
            'id': project.id,
            'name': project.name,
            'homeowner_name': project.homeowner.name,
            'contractor_name': project.contractor.name,
            'budget': project.display_budget(),
            'total_number': project.total_number,
        }

        return Response(data, status=status.HTTP_201_CREATED)

    # Function to delete the project
    @action(detail=True, methods=['post'])
    def destroy(self, id):

        project = Project.objects.get(id__exact=id)
        project.delete()

        return Response(status=status.HTTP_201_CREATED)




