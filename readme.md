# Week 11 - Secure Coding

## Instructions for use

Userlist_App is a Chat box display where contributers must be added to the Member list.
- Click "View Users" to view the member list
- Click "Add User" to add yourself to the list of chatters
- Fill in the form and click "Add"
- Click "View Chat Box" to start chatting

Environment Variable "DJANGO_SECRET_KEY" needs to be set
Admin account details:
username: testuser
password: testuser

## Portfolio Tasks:

- Amend existing code so that secrets are loaded in through environment variables e.g. Django SECRET_KEY variable in settings.py (commit to repo and evidence)
- Run code through both Bandit and Safety tools to identify any issues with code or dependencies (get evidence)
- Write a security code review checklist for future projects, include at least 8 checks e.g. do all forms have a csrf token
