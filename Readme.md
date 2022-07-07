# griffinsteffy.com

## Installation
    1. download as git repository
    2. start virtual environment
    3. install requirements.txt via pip
    4. 'export DEVELOPMENT_MODE=False'
    5. 'export DEBUG=True'
    6. 'python manage.py runserver'

## Environment Variables
    DEBUG -> enables debug mode on server (local or remote)
    DEVELOPMENT_MODE -> points to local or remote media/static server

### DEVELOPMENT_MODE
    The site is setup to use digital ocean spaces to host media/static files
    To do this locally, get neccessary environment variables and place them in dev.py located in the same folder as settings.py
```
griffinsteffy.com   
│
└───griffinsteffy
│   │   settings.py
│   │   dev.py*
│   │   ..
│   
└───blog
│   │   ...
│   
└───about
│   │   ...
│   
└───base
│   │   ...
│
...
```


## Future Features
    - Search Results accross post content, and aditional media on site
        - [django haystack](https://django-haystack.readthedocs.io/en/master/)
    - Resume Page
