from sqlalchemy import MetaData, Integer, String, ForeignKey, Table, Column, JSON

metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
    Column("permissions", JSON),
)
