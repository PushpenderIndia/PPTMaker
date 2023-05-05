from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import History
from django.contrib import messages
from home.GeneratePPT import GeneratePPT

# Create your views here.

from django.shortcuts import render, redirect
from .tasks import generate_ppt_task
from django.http import JsonResponse

def index(request):
    if request.method == 'POST':
        print(request.POST)
        topic = request.POST['topic']
        slide_count = int(request.POST['slider'])
        print("[*] Topic: ", topic)
        print("[*] Slide Count: ", slide_count)

        # Call the Celery task and get the task ID
        task_result = generate_ppt_task.delay(topic, slide_count)
        task_id = task_result.id

        # Redirect to the waiting page with the task ID
        return redirect('waiting', task_id=task_id)

    return render(request, 'index.html')

def waiting(request, task_id=None):
    return render(request, 'waiting.html', {'task_id': task_id})

def check_task_progress(request):
    task_id = request.GET.get('task_id')

    # Get the Celery task result and return its status
    task_result = generate_ppt_task.AsyncResult(task_id)
    if task_result.ready():
        return JsonResponse({'status': task_result.status, 'output_filepath': task_result.get()})
    else:
        return JsonResponse({'status': task_result.status})
