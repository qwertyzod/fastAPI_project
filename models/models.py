from sqlalchemy import MetaData, Integer, String, ForeignKey, Table, Column, JSON, TIMESTAMP
from datetime import datetime


metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
    Column("permissions", JSON),
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(100), nullable=False),
    Column("email", String, nullable=False),
    Column("password", String, nullable=False),
    Column("role_id", Integer, ForeignKey("roles.id")),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
)