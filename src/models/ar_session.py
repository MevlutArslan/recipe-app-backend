from typing import Any
from .base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.dialects.postgresql import UUID
import qrcode
import os

class ARSession(Base):
    __tablename__ = 'ar_session'
    id= Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    host_id= Column("host_id", String, unique=True)
    qr_code= Column("qr_code", String)

def generate_qrcode(device_identifier):
    qr_code = qrcode.make(device_identifier)
    file_name = device_identifier + ".png"
    file_path = os.path.join(os.path.dirname(__file__), "../qr_codes", file_name)
    qr_code.save(file_path)
    
    return file_path