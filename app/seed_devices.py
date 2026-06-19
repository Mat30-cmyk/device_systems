from app.database.connection import SessionLocal

from app.models.user_model import User
from app.models.loan_model import Loan
from app.models.device_model import Device

db = SessionLocal()

devices = [
    Device(
        name="ThinkPad T14",
        serial_number="LEN001",
        device_type="laptop",
        brand="Lenovo",
        is_available=True
    ),
    Device(
        name="ThinkPad E15",
        serial_number="LEN002",
        device_type="laptop",
        brand="Lenovo",
        is_available=True
    ),
    Device(
        name="Dell Latitude 5420",
        serial_number="DEL001",
        device_type="laptop",
        brand="Dell",
        is_available=True
    ),
    Device(
        name="HP ProBook 450",
        serial_number="HP001",
        device_type="laptop",
        brand="HP",
        is_available=True
    ),
    Device(
        name="MacBook Air M2",
        serial_number="APP001",
        device_type="laptop",
        brand="Apple",
        is_available=True
    ),
    Device(
        name="Samsung Galaxy Tab S9",
        serial_number="SAM001",
        device_type="tablet",
        brand="Samsung",
        is_available=True
    ),
    Device(
        name="iPad Air",
        serial_number="APP002",
        device_type="tablet",
        brand="Apple",
        is_available=True
    ),
    Device(
        name="Canon EOS Rebel T7",
        serial_number="CAM001",
        device_type="camera",
        brand="Canon",
        is_available=True
    ),
    Device(
        name="Nikon D3500",
        serial_number="CAM002",
        device_type="camera",
        brand="Nikon",
        is_available=True
    ),
    Device(
        name="Epson PowerLite X49",
        serial_number="PRO001",
        device_type="projector",
        brand="Epson",
        is_available=True
    )
]

db.add_all(devices)
db.commit()

print("✅ Dispositivos insertados correctamente")

db.close()