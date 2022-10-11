# -*- coding: utf-8 -*-
"""This module contains all the bussiness logic for the author."""
from ..model import Author, authors_schema, author_schema
from flask import jsonify
from ...extensions import db


def handle_list_authors():
    """List all authors."""
    return authors_schema.dump(Author.all_users()), 200

def delete_author(author_id: str):
    """Delete an author."""
    if not author_id:
        raise ValueError('The author id has to be provided')
    if not isinstance(author_id, str):
        raise TypeError('The author id has to be a string')
    if not Author.user_with_id_exists(int(author_id)):
        raise ValueError(f'Their is no author with id {author_id}')
    return author_schema.dump(Author.delete_user(int(author_id))), 200

def handle_delete_author(author_id: str):
    """List all authors."""
    try:
        deleted_author = delete_author(author_id)
    except (ValueError, TypeError) as e:
        return jsonify({'error': str(e)})
    else:
        return deleted_author
    

def get_author(author_id: str) -> dict:
    """Get the user with the given id."""
    if not author_id:
        raise ValueError("The author_id has to be provided.")
    if not isinstance(author_id, str):
        raise TypeError("The author_id has to be a string.")
    if not Author.user_with_id_exists(int(author_id)):
        raise ValueError(f"The user with id {author_id} does not exist.")

    return author_schema.dump(Author.get_user(int(author_id))), 200   

    
def handle_get_author(author_id: str):
    """Get a single author."""
    try:
        author = get_author(author_id)
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400
    else:
        return author

def update_author(author_id: str, author_data: dict, profile_pic):
    """Handle the post request to create a new author."""
    if not author_id:
        raise ValueError("The author_id has to be provided.")
    if not isinstance(author_id, str):
        raise ValueError("The author_id has to be a string.")
    if not Author.user_with_id_exists(int(author_id)):
        raise ValueError(f"The user with id {author_id} does not exist.")
    if not author_data:
        raise ValueError("The user data cannot be empty.")
    if not isinstance(author_data, dict):
        raise TypeError("user_data must be a dict")
    valid_keys = [
        "First Name",
        "Last Name",
        "Email Address",
        "Nickname",
        "Bio"
    ]
    for key in author_data.keys():
        if key not in valid_keys:
            raise ValueError(f"The only valid keys are {valid_keys}")
    
    author = Author.get_user(int(author_id))
    
    if "First Name" in author_data.keys():
        Author.validate_name(author_data['First Name'])
        author.first_name = author_data['First Name']
    if "Last Name" in author_data.keys():
        Author.validate_name(author_data['Last Name'])
        author.last_name = author_data['Last Name']
    if "Email Address" in author_data.keys():
        Author.validate_email(author_data['Email Address'])
        if Author.user_with_email_exists(author_data["Email Address"]):
            raise ValueError(f'The user with email address {author_data["Email Address"]} exists')
        author.email_address = author_data['Email Address']
    if "Nickname" in author_data.keys():
        Author.validate_screen_name(author_data['Nickname'])
        author.screen_name = author_data['Nickname']
    if "Bio" in author_data.keys():
        Author.validate_bio(author_data['Bio'])
        author.bio = author_data['Bio']
    # db.session.add(author)
    # db.session.commit()

    return author_schema.dumps(author), 201


def handle_update_author(author_id: str, author_data: dict, profile_pic):
    """Handle the post request to create a new author."""
    try:
        author = update_author(author_id, author_data, profile_pic)
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400
    else:
        return author


def get_author_followers(author_id: str) -> dict:
    """Get the authors followers."""
    if not author_id:
        raise ValueError("The author_id has to be provided.")
    if not isinstance(author_id, str):
        raise TypeError("The author_id has to be a string.")
    if not Author.user_with_id_exists(int(author_id)):
        raise ValueError(f"The user with id {author_id} does not exist.")

    return jsonify({'followers': Author.get_followers(int(author_id))}), 200   

    
def handle_get_author_followers(author_id: str):
    """Get an author's followers."""
    try:
        author_followers = get_author_followers(author_id)
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400
    else:
        return author_followers

def get_author_follows(author_id: str) -> dict:
    """Get the authors follows."""
    if not author_id:
        raise ValueError("The author_id has to be provided.")
    if not isinstance(author_id, str):
        raise TypeError("The author_id has to be a string.")
    if not Author.user_with_id_exists(int(author_id)):
        raise ValueError(f"The user with id {author_id} does not exist.")

    return jsonify({'followers': Author.get_follows(int(author_id))}), 200   

    
def handle_get_author_follows(author_id: str):
    """Get an author's follows."""
    try:
        author_follows = get_author_follows(author_id)
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400
    else:
        return author_follows