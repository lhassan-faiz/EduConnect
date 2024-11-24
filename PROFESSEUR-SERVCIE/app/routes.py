from flask import Blueprint, jsonify, request
from app.services import get_all_professors, get_professor_by_id, create_professor, delete_professor
from app.graphql_queries import get_courses_by_professor

professor_bp = Blueprint("professor", __name__)

@professor_bp.route("/", methods=["GET"])
def list_professors():
    professors = get_all_professors()
    return jsonify([{"id": p.id, "name": p.name, "email": p.email} for p in professors])

@professor_bp.route("/<int:professor_id>/courses", methods=["GET"])
def list_courses_by_professor(professor_id):
    courses = get_courses_by_professor(professor_id)
    return jsonify(courses)

@professor_bp.route("/", methods=["POST"])
def add_professor():
    data = request.json
    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and email are required"}), 400
    professor = create_professor(data["name"], data["email"])
    return jsonify({"id": professor.id, "name": professor.name, "email": professor.email}), 201

@professor_bp.route("/<int:professor_id>", methods=["DELETE"])
def remove_professor(professor_id):
    if delete_professor(professor_id):
        return jsonify({"message": "Professor deleted"}), 200
    return jsonify({"error": "Professor not found"}), 404


@professor_bp.route("/<int:professor_id>", methods=["GET"])
def get_professor(professor_id):
    """Get professor by ID"""
    professor = get_professor_by_id(professor_id)
    if professor:
        return jsonify({"id": professor.id, "name": professor.name, "email": professor.email})
    return jsonify({"error": "Professor not found"}), 404
