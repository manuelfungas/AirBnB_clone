#!/usr/bin/python3
from datetime import datetime
import uuid


class BaseModel():
    """Base model for the data in the HBnB project"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __self__(self):
        """Returns a str representation of the model instance"""
        class_name = self.__class__.__name__
        attributes = ",".join(
                f"{key}='{value}'"
                for key, value in self.__dict__.items()
                if not key.startswith("_"))
        return f"[{class_name}] ({self.id}) - {attributes}"

    def save(self):
        """Update the update_at with the current time"""
        self.update_at = datetime.now()

    def to_dict(self):
        """Return the dict representation of the model"""
        data = self.__dict__.copy()
        data["__class__"] = self.__class__.__name__
        data["created_at"] = data["created_at"].isoformat()
        data["updated_at"] = data["updated_at"].isoformat()
        return data
