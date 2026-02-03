from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from core.models import Task

class Command(BaseCommand):
    help = "Create demo tasks and a demo student account for the IPD prototype."

    def handle(self, *args, **options):
        if not Task.objects.exists():
            titles = [
                "Giannis multiplies fractions",
                "Maria’s division rule",
                "Half a kilo problem",
                "Fix the chart",
                "Shade the fraction product",
                "What is 2/5 of 30?",
                "Division as measurement match",
                "Variable divisor method",
                "What do students need first?",
                "Ribbon bows",
                "What maths is in Task 10?",
                "120 cm ribbon division",
                "Change the unit, find a rule",
                "Times three / divide by three",
                "Explaining division by 1/3",
                "Is 3 ÷ 5/10 really 6?",
            ]
            for i, title in enumerate(titles, start=1):
                slug = f"task-{i}"
                if i == 10:
                    slug = "task-10-ribbon"
                    title = "Ribbon Bows"
                Task.objects.create(order=i, title=title, slug=slug, is_available=True)
            self.stdout.write(self.style.SUCCESS("✅ Seeded 16 tasks."))

        User = get_user_model()
        if not User.objects.filter(username="demochild").exists():
            User.objects.create_user(username="demochild", password="demo12345")
            self.stdout.write(self.style.SUCCESS("✅ Created demo user demochild / demo12345"))
        else:
            self.stdout.write("Demo user already exists.")