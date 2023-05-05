from celery import shared_task
from home.GeneratePPT import GeneratePPT

OPENAI_KEY  = "sk-u7yHvgNXXXXXXXXXXXXXXXXXXXX0hpTuBs8Z9"
ACCESS_KEY = "YRx46BWsIXXXXXXXXXXXXXXXXXXXXXXrNA6jecP0-91Syw"

@shared_task
def generate_ppt_task(topic, slide_count):
    output_filepath = f'static/generated_ppt_{topic}.pptx'
    ppt_generator = GeneratePPT(OPENAI_KEY, topic, slide_count, output_filepath, ACCESS_KEY)
    ppt_generator.start()
    return output_filepath