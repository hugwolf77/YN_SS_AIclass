import uuid
from typing import (Any, list)
from typing import Optional
from sqlalchemy import (Column, String, Integer, ForeignKey, Table)
from sqlalchemy.orm import (Mapped, mapped_column)
# from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.sqlite import UUID
# from sqlalchemy.dialects.postgresql import UUID

# Base = declarative_base()

class Base(DeclarativeBase):
    """Base database model."""
    pk: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

base_association_table = Table(
    "BASE_ASSOCIATION_TABLE",
    Base.metadata,
    Column("CSCIDS2017_id", UUID(as_uuid=True), ForeignKey("CSCIDS2017.pk")),
    # Column("test_id", UUID(as_uuid=True), ForeignKey("test.pk"))
)
