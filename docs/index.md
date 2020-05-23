> ## 🛠 Status: In Development
> MLRecruiters is currently in development. So we encourage you to use it and give us your feedback, but there are things that haven't been finalized yet and you can expect some changes.
>
> See the list of Known Issues and TODOs, below, for updates.

## Overview
Every person needs help from other professionals be it electricians, plumbers, mechanics or any other. This project is a quick and easy way for people(recruiters) to connect with skilled people who think are a good fit and hire them


## Getting Started

* [Fork repository][MLRecruiters] and clone it.

```shell tab="Shell or CMD"

git clone https://github.com/Strategy-Tap/MLRecruiters-BackEnd
```

* install dependence:

```shell tab="Poetry"
poetry install
```

```shell tab="pip"
pip install -r requirements.txt  # for production
pip install -r full_requirements.txt  # for dev
```

* serve the app:

1. create .env in the root of the project or set your ENV add the following line into .env file or set your ENV:
    
    
    DEBUG=True  # change this in production
    ALLOWED_HOSTS=example.com, localhost, 0.0.0.0, 127.0.0.1  # change this in production
    SECRET_KEY=w86k@*ash*z)dsxsoz+o*ne*ugb08(4nu13%8!m*+2_e@@7hnx  # change this in production and never put the production key here
    DATABASE_URL=sqlite:///db.sqlite3
    EMAIL_USER=example@example.com  # for production
    EMAIL_PASSWORD=''  # for production 
    DROPBOX_OAUTH2_TOKEN=''  # for production

2. create `media`, `static`, and `static_root` folder if you don't have them 


```shell tab="shell or CMD"

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

enjoy :)

# License: MIT


[MLRecruiters]: https://github.com/Strategy-Tap/MLRecruiters-BackEnd

