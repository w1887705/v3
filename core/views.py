from __future__ import annotations

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Task, Progress, Attempt

def _seed_tasks_if_needed() -> None:
    if Task.objects.exists():
        return
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

@login_required
def home(request: HttpRequest) -> HttpResponse:
    return redirect("core:tasks")

def logout_view(request: HttpRequest) -> HttpResponse:
    """Log the user out and send them back to the login screen with a friendly message."""
    logout(request)
    messages.success(request, "✅ You have been logged out.")
    return redirect("login")



@login_required
def tasks(request: HttpRequest) -> HttpResponse:
    _seed_tasks_if_needed()

    # Difficulty filter (stored in session so it stays selected)
    # Easy = tasks 1–5, Medium = 6–11, Hard = 12–16, All = everything
    difficulty = request.GET.get("difficulty")
    if difficulty in {"easy", "medium", "hard", "all"}:
        request.session["difficulty"] = difficulty
    difficulty = request.session.get("difficulty", "all")

    all_tasks = Task.objects.order_by("order")

    if difficulty == "easy":
        shown_tasks = all_tasks.filter(order__gte=1, order__lte=5)
    elif difficulty == "medium":
        shown_tasks = all_tasks.filter(order__gte=6, order__lte=11)
    elif difficulty == "hard":
        shown_tasks = all_tasks.filter(order__gte=12, order__lte=16)
    else:
        shown_tasks = all_tasks

    progress = {p.task_id: p for p in Progress.objects.filter(user=request.user, task__in=shown_tasks)}
    completed_count = sum(1 for t in shown_tasks if progress.get(t.id) and progress[t.id].completed)
    total = shown_tasks.count() or 1
    percent = int((completed_count / total) * 100)

    items = []
    for t in shown_tasks:
        p = progress.get(t.id)
        items.append({"task": t, "completed": bool(p and p.completed)})

    return render(request, "core/tasks.html", {
        "items": items,
        "percent": percent,
        "completed_count": completed_count,
        "total": total,
        "difficulty": difficulty,
    })


@login_required
def task_detail(request: HttpRequest, slug: str) -> HttpResponse:
    task = get_object_or_404(Task, slug=slug)
    if slug == "task-10-ribbon":
        return redirect("/ribbon/")
    return render(request, "core/task_placeholder.html", {"task": task})

@login_required
def api_complete_task(request: HttpRequest, slug: str) -> JsonResponse:
    if request.method != "POST":
        return JsonResponse({"ok": False, "error": "POST required"}, status=405)
    task = get_object_or_404(Task, slug=slug)
    prog, _ = Progress.objects.get_or_create(user=request.user, task=task)
    prog.completed = True
    prog.last_score = 100
    prog.save()
    Attempt.objects.create(user=request.user, task=task, score=100, notes="Completed in prototype")
    return JsonResponse({"ok": True})