"""
This file is for fake generated data for testing purposes.
"""
from api import create_app, db
from api.models import Canidate, Recruiter, InnovationChallenge
from faker import Faker
import random
from datetime import datetime
import bcrypt

faker = Faker()

def generate_users():
    def register_candidate(first_name, last_name, username, email, grad_date, location, password, linkedin, github):
        if not Canidate.query.filter_by(email=email).first() and not Canidate.query.filter_by(username=username).first():
            new_candidate = Canidate(
                firstName=first_name,
                lastName=last_name,
                username=username,
                email=email,
                linkedIn=linkedin,
                github=github,
                gradDate=grad_date,
                location=location,
                password_hash=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
                date_created=datetime.utcnow()
            )
            db.session.add(new_candidate)
            db.session.commit()
            print(f"Candidate {username} created successfully.")
        else:
            print(f"Candidate {username} already exists.")

    def register_recruiter(first_name, last_name, email, location, password):
        if not Recruiter.query.filter_by(email=email).first():
            new_recruiter = Recruiter(
                firstName=first_name,
                lastName=last_name,
                email=email,
                location=location,
                password_hash=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
                date_created=datetime.utcnow()
            )
            db.session.add(new_recruiter)
            db.session.commit()
            print(f"Recruiter {email} created successfully.")
        else:
            print(f"Recruiter {email} already exists.")

    # Generate 30 unique candidates
    for _ in range(100):
        first_name = faker.first_name()
        last_name = faker.last_name()
        username = faker.user_name()
        email = faker.email()
        grad_date = str(random.randint(2023, 2028))
        location = faker.city()
        password = faker.password()
        linkedin = f"linked.com/{first_name.lower()}-{last_name.lower()}"
        github = f"github.com/{first_name.lower()}"
        register_candidate(first_name, last_name, username, email, grad_date, location, password, linkedin, github)

    """    def generate_innovation_challenge():
        title = "Develop a way to distribute medicine for students amongst schools"
        description = faker.paragraph(nb_sentences=5)
        location = faker.city()
        team_size = 6
        date_started = datetime(2024, 11, 20)
        date_ended = datetime(2024, 11, 21)
        recruiter_id = 1

        new_challenge = InnovationChallenge(
            title=title,
            description=description,
            location=location,
            teamSize=team_size,
            date_started=date_started,
            date_ended=date_ended,
            recruiter_id=recruiter_id
        )
        db.session.add(new_challenge)
        db.session.commit()
        print(f"Innovation Challenge '{title}' created successfully.")"""

    #generate_innovation_challenge()

    # Generate 1 recruiter -. FAKE DATA    
    # for demo
    first_name = "Gustavo"
    last_name = "Garcia"
    email = f"{first_name.lower()}.{last_name.lower()}@jnj.com"
    location = "New Brunswick"
    password = "LetsGoJohnson!"
    #register_recruiter(first_name, last_name, email, location, password)

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        generate_users()