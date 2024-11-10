"""
This file is for fake generated data for testing purposes.
"""
from api import create_app, db
from api.models import Canidate, Recruiter, InnovationChallenge, canidateTeams, canidateToTeam
from faker import Faker
import random
from datetime import datetime
import bcrypt

faker = Faker()

def generate_users():
    def register_candidate(first_name, last_name, username, email, grad_date, location, password, linkedin, github, resumeUrl):
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
                resumeUrl=resumeUrl,
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
        resume_url = f"s3.amazonaws.com/{first_name}-{last_name}/resume.pdf"
        register_candidate(first_name, last_name, username, email, grad_date, location, password, linkedin, github, resumeUrl = resume_url)

    def generate_innovation_challenge():
        title = "Develop a way to distribute medicine for students amongst schools"
        description = faker.paragraph(nb_sentences=5)
        location = faker.city()
        team_size = 6
        date_started = datetime(2024, 11, 20)
        date_ended = datetime(2024, 11, 21)
        recruiter_id = 1
        # get recruiter email based off recruiter ID
        recruiter_email = Recruiter.query.get(recruiter_id).email
        # get first name / last name off recruiter ID
        recruiter_first_name = Recruiter.query.get(recruiter_id).firstName
        recruiter_last_name = Recruiter.query.get(recruiter_id).lastName

        new_challenge = InnovationChallenge(
            title=title,
            description=description,
            location=location,
            teamSize=team_size,
            date_started=date_started,
            date_ended=date_ended,
            recruiter_email=recruiter_email,
            recruiter_firstName=recruiter_first_name,
            recruiter_lastName=recruiter_last_name,
            recruiter_id=recruiter_id
        )
        db.session.add(new_challenge)
        db.session.commit()
        print(f"Innovation Challenge '{title}' created successfully.")

    first_name = "Gustavo"
    last_name = "Garcia"
    email = f"{first_name.lower()}.{last_name.lower()}@jnj.com"
    location = "New Brunswick"
    password = "LetsGoJohnson!"
    register_recruiter(first_name, last_name, email, location, password)

    generate_innovation_challenge()

    # Generate 1 recruiter -. FAKE DATA    
    # for demo
def generate_teams():
    """
    Generates randomized teams for CanidateToTeam and CanidateTeams using the current candidates' IDs.
    """
    candidates = Canidate.query.all()
    candidate_ids = [candidate.id for candidate in candidates]
    random.shuffle(candidate_ids)

    num_teams = max(1, len(candidate_ids) // 6)  # Assuming around 6 candidates per team
    teams = [candidate_ids[i::num_teams] for i in range(num_teams)]

    project_names = [
    "Project Lifeline", "Project MedConnect", "Project CareBridge", "Project VitalReach", 
    "Project HealthLink", "Project WellnessNet", "Project MedSphere", "Project StudentCare",
    "Project HealthHaven", "Project CurePath", "Project MedRelay", "Project MediCircle",
    "Project PharmaShare", "Project MedAssist", "Project CareHive", "Project HealthBridge",
    "Project VitalWave", "Project MedStream", "Project WellSprout", "Project SafeMeds",
    "Project CareLink", "Project SchoolMeds", "Project HealthAnchor", "Project MediChain",
    "Project StudentWellness", "Project VitalSteps", "Project MediHive", "Project CureNet",
    "Project WellnessBridge", "Project CarePulse", "Project HealthRipple", "Project MediFlow",
    "Project PharmaReach", "Project MedCircle", "Project VitalRoot", "Project HealthSeed",
    "Project SchoolCare", "Project MediTrack", "Project PharmaLink", "Project SafeHealth",
    "Project CareFlow", "Project MedAccess", "Project HealthPulse", "Project WellnessLink",
    "Project StudentHealth", "Project CureBridge", "Project MedTrail", "Project CareSpring",
    "Project PharmaStream", "Project VitalNetwork"  
    ]


    for team_id, team in enumerate(teams, start=1):
        user_ids = ";".join(map(str, team))
        user_emails = ",".join([Canidate.query.get(candidate_id).email for candidate_id in team])
        user_names = ",".join([f"{Canidate.query.get(candidate_id).firstName} {Canidate.query.get(candidate_id).lastName}" for candidate_id in team])
        project_name = random.choice(project_names)

        new_team = canidateTeams(
            projectName=project_name,
            user_ids=user_ids,
            user_emails=user_emails,
            user_names=user_names,
            innovation_challenge_id=1,  # Assuming the innovation challenge ID is 1
            github_link=f"https://github.com/team{team_id}",
            figmaLink=f"https://figma.com/team{team_id}",
            descriptionOfProject=faker.paragraph(nb_sentences=5),
        )
        db.session.add(new_team)
        db.session.commit()
        print(f"Team {team_id} created with users: {user_ids}")

        for candidate_id in team:
            new_candidate_to_team = canidateToTeam(
                user_id=candidate_id,
                team_id=new_team.id,  # Assuming CanidateToTeam has a team_id field that references CanidateTeams
            )
            db.session.add(new_candidate_to_team)
            db.session.commit()
            print(f"Candidate {candidate_id} added to team {new_team.id}")


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        generate_users()
        generate_teams()