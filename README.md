# Crowd-Funding Platform

A Django-based crowdfunding platform designed to help users create, discover, and support fundraising projects in Egypt.

## Project Overview

The platform allows users to create fundraising campaigns, upload project images, add tags and categories, receive donations, interact through comments and ratings, and discover other projects.

## Main Features

### Authentication & User Profiles

* User registration
* Email activation
* Login and logout
* Egyptian mobile number validation
* Profile picture
* User profile
* Edit profile information
* Account deletion
* Password reset

### Projects

* Create fundraising projects
* Project categories
* Tags
* Multiple project images
* Donation target
* Start and end dates
* Project details
* Similar projects

### Donations & Interaction

* Donate to projects
* Track project funding progress
* Add comments
* Rate projects
* Report inappropriate projects and comments
* Cancel eligible projects

### Homepage & Search

* Highest-rated running projects
* Latest projects
* Featured projects
* Browse projects by category
* Search by project title or tag

## Technologies

* Python
* Django
* HTML
* CSS
* JavaScript
* SQLite

## Project Structure

```text
Crowd-Funding/
│
├── crowdfunding/
├── manage.py
├── templates/
├── static/
├── media/
├── .gitignore
└── README.md
```

## Team Workflow

The project is developed collaboratively using Git and GitHub.

Each team member works on a separate feature branch and submits a Pull Request before merging changes into `main`.

```text
main
├── feature/auth
├── feature/projects
├── feature/donations
└── feature/homepage
```

## How to Run the Project

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the required dependencies.
4. Apply database migrations.
5. Run the Django development server.

```bash
python manage.py migrate
python manage.py runserver
```

## Project Status

Under Development
