# -*- coding: utf-8 -*-
"""This module contains all the author routes."""
from flasgger import swag_from
from flask import Blueprint, jsonify, request
from .controller import (
    handle_list_authors,
    handle_delete_author,
    handle_get_author,
    handle_update_author
)

author = Blueprint("author", __name__)


@swag_from("./docs/get_author.yml", endpoint="author.get_author", methods=["GET"])
@author.route("/", methods=["GET"])
def get_author():
    """Get a an author by id."""
    return handle_get_author(request.args.get('id'))


@swag_from("./docs/update_author.yml", endpoint="author.update_author", methods=["PUT"])
@author.route("/", methods=["PUT"])
def update_author():
    """Update the author with given id."""
    return handle_update_author(request.args.get("id"), request.form, request.files)


@swag_from(
    "./docs/delete_author.yml", endpoint="author.delete_author", methods=["DELETE"]
)
@author.route("/", methods=["DELETE"])
def delete_author():
    """Delete the author with given id."""
    return handle_delete_author(request.args.get('id'))


@swag_from("./docs/follow_author.yml", endpoint="author.follow_author", methods=["GET"])
@author.route("/follow", methods=["GET"])
def follow_author():
    """Follow the author with given id."""
    return jsonify({"author": "follow"}), 200


@swag_from(
    "./docs/get_all_authors.yml", endpoint="author.get_all_authors", methods=["GET"]
)
@author.route("/authors", methods=["GET"])
def get_all_authors():
    """List all authors."""
    return handle_list_authors()
