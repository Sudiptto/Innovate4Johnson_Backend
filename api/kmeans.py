from flask import Blueprint, render_template, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from .models import *
from . import db
import boto3
import requests
from io import BytesIO
from PyPDF2 import PdfFileReader

import implementations.getListing as getListing 
import implementations.getvector as getvector
import implementations.kmean as kmean

import users


project = Blueprint("kmean", __name__)

def makeTeam(idx, team):
    team_data = {
        "id": idx,
        "projectName": "Placeholder Project Name",
        "user_ids": team,
        "user_emails": ["placeholder@example.com" for _ in team],
        "user_names": ["Placeholder Name" for _ in team],
        "innovation_challenge_id": "Placeholder Challenge ID",
        "github_link": "https://github.com/placeholder",
        "figma_link": "https://figma.com/placeholder",
        "descriptionOfProject": "Placeholder description of the project"
    }
    team =  Team(**team_data)

    db.session.add(team)
    db.session.commit()
    
    


def extract_text_from_pdf(pdf_content):
    pdf_reader = PdfFileReader(BytesIO(pdf_content))
    text = ""
    for page_num in range(pdf_reader.getNumPages()):
        text += pdf_reader.getPage(page_num).extract_text()
    return text

def main():
    # Call the function to get all users
    all_users = users.getAllUsers()

    # Initialize the S3 client
    s3_client = boto3.client('s3')

    # Array to store the extracted text and corresponding user ID
    extracted_texts = []

    for user in all_users:
        # Extract the S3 bucket name and key from the resume URL
        resume_url = user['resume']
        bucket_name = resume_url.split('/')[2]
        key = '/'.join(resume_url.split('/')[3:])

        # Download the resume from the S3 bucket
        response = s3_client.get_object(Bucket=bucket_name, Key=key)
        pdf_content = response['Body'].read()

        # Extract the text from the resume
        extracted_text = extract_text_from_pdf(pdf_content)

        # Append the extracted text and user ID to the array
        extracted_texts.append([extracted_text, user['id']])

    #print(extracted_texts)
    vectors = []
    listing_info = getListing.getListing()

    for text, user_id in extracted_texts:
        vector = getvector.get_vector(listing_info, text, user_id)
        vectors.append(vector)
    
    results = kmean.kmean(vectors)

    for idx, team in enumerate(results):   
        maketeam(idx, team)
            
            



    # Print the extracted texts for verification
    #for text in extracted_texts:
    #    vector = get_vector(listing_info)
    #    vectors.append(vector)
        



