import asyncio
import logging

from sqlalchemy.ext.asyncio import create_async_engine
from core.config import Settings
from DW.DB.db_models.base_model import Base

logger = logging.getLogger()