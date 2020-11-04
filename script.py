
from CrowdFund.models import NewProject
path = r"D:\Bitnami\djangostack-3.1.2-0\apps\django\django_projects\Project\MOCK_DATA.csv"


 with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = NewProject.objects.get_or_create(
                Name=row[0],
                Gender=row[1],
                Age=row[2],
                username = row[3],
                password = row[4]
                )
