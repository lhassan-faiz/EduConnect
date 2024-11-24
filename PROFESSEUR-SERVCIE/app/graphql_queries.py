import requests
from flask import current_app

GRAPHQL_URL = "http://localhost:4000/graphql"


def get_courses_by_professor(professor_id):
    graphql_query = """
    query GetCourses($professorId: Int!) {
        coursesByProfessor(professorId: $professorId) {
            id
            title
            description
        }
    }
    """
    variables = {"professorId": professor_id}
    response = requests.post(
        current_app.config["GRAPHQL_COURSE_SERVICE_URL"],
        json={"query": graphql_query, "variables": variables},
    )
    return response.json()
