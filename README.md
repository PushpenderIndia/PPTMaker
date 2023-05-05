# PPTMaker
Django Powered Web Application which takes Topic &amp; Slide Count &amp; Automatically Generates a Presentable PPT

Project was developed in a Hackathon where we able to qualify the 1st round.

## Technologies Used
- Django
- Celery
- Redis
- HTML
- CSS
- Bootstrap
- Javascript
- OpenAi API
- Unsplash API

## Installation
```
cd PPTMaker
python -m pip install -r requirements.txt
# Install Redis
# Update OPENAI_KEY & OpenAI's ACCESS_KEY in PPTMaker/home/tasks.py
python manage.py makemigrations
python manage.py migrate
```

## How to Run
```
python manage.py runserver 
celery -A PPTMaker.celery worker -l info --pool=eventlet
```

## Hackathon Teammate
<table>
<tr>

<td align="center">
    <a href="https://github.com/arushi167">
        <kbd><img src="https://avatars3.githubusercontent.com/arushi167?size=400" width="100px;" alt=""/></kbd><br />
        <sub><b>Arushi Jain</b></sub>
    </a><br />
</td>

<td align="center">
    <a href="https://github.com/PushpenderIndia">
        <kbd><img src="https://avatars3.githubusercontent.com/PushpenderIndia?size=400" width="100px;" alt=""/></kbd><br />
        <sub><b>Pushpender Singh</b></sub>
    </a><br />
</td>

<td align="center">
    <a href="https://github.com/Ayushi0405">
        <kbd><img src="https://avatars3.githubusercontent.com/Ayushi0405?size=400" width="100px;" alt=""/></kbd><br />
        <sub><b>Ayushi Gupta</b></sub>
    </a><br />
</td>

<td align="center">
    <a href="https://github.com/Yuvraj0208">
        <kbd><img src="https://avatars3.githubusercontent.com/Yuvraj0208?size=400" width="100px;" alt=""/></kbd><br />
        <sub><b>Yuvraj Singh</b></sub>
    </a><br />
</td>

</tr>
</tr>
</table>
