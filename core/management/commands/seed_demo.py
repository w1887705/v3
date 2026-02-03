from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from core.models import Task

class Command(BaseCommand):
    help = "Create demo tasks and a demo student account for the IPD prototype."

    def handle(self, *args, **options):
        titles = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "Ribbon bows",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
        ]

        created_count = 0
        for i, title in enumerate(titles, start=1):
            slug = f"task-{i}"
            if i == 10:
                slug = "task-10-ribbon"
                title = "Ribbon Bows"

            _, created = Task.objects.get_or_create(
                slug=slug,
                defaults={"order": i, "title": title, "is_available": True},
            )
            if created:
                created_count += 1

        if created_count:
            self.stdout.write(self.style.SUCCESS(f"✅ Seeded {created_count} tasks (idempotent)."))
        else:
            self.stdout.write("Tasks already seeded.")

        User = get_user_model()
        user, created = User.objects.get_or_create(username="demochild")
        user.set_password("demo12345")  # always ensure correct password
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS("✅ Created demo user demochild / demo12345"))
        else:
            self.stdout.write(self.style.SUCCESS("🔁 Updated demo user password to demo12345"))
