
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.db.models import Base
from datetime import datetime

class Objectmismatch(Base):
    __tablename__ = "objectmismatch"

    id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(Integer)
    site_id = Column(Integer)
    camera_id= Column(Integer)
    video_id = Column(Integer)
    image_id = Column(String(255))
    location= Column(String(255))
    alert_sent = Column(String(255))
    current_count = Column(String(255))
    previous_count = Column(String(255))

    mismatch_count = Column(Boolean, default=False)  # Assuming it's a status flag
    create_date = Column(DateTime, default=datetime.utcnow)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    stat