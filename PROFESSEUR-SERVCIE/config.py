import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:123456@host.docker.internal:5432/professors")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GRAPHQL_COURSE_SERVICE_URL = os.getenv("COURSE_SERVICE_URL", "http://localhost:4000/graphql")
