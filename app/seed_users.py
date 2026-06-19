from sqlalchemy.orm import Session

from app.models.loan_model import Loan
from app.models.device_model import Device
from app.models.user_model import User


from app.database.connection import SessionLocal
from app.models.user_model import User


def seed_users():

    db: Session = SessionLocal()

    users = [
        User(
            name="Juan Perez",
            email="juan.perez@example.com",
            role="admin",
            is_active=True
        ),
        User(
            name="Maria Gomez",
            email="maria.gomez@example.com",
            role="support",
            is_active=True
        ),
        User(
            name="Carlos Rodriguez",
            email="carlos.rodriguez@example.com",
            role="user",
            is_active=True
        ),
        User(
            name="Laura Martinez",
            email="laura.martinez@example.com",
            role="user",
            is_active=True
        ),
        User(
            name="Andres Torres",
            email="andres.torres@example.com",
            role="support",
            is_active=True
        ),
        User(
            name="Sofia Ramirez",
            email="sofia.ramirez@example.com",
            role="user",
            is_active=True
        ),
        User(
            name="Daniel Castro",
            email="daniel.castro@example.com",
            role="user",
            is_active=True
        ),
        User(
            name="Valentina Ruiz",
            email="valentina.ruiz@example.com",
            role="user",
            is_active=True
        ),
        User(
            name="Miguel Herrera",
            email="miguel.herrera@example.com",
            role="support",
            is_active=True
        ),
        User(
            name="Camila Moreno",
            email="camila.moreno@example.com",
            role="user",
            is_active=True
        ),
        User(
            name="Sebastian Vargas",
            email="sebastian.vargas@example.com",
            role="user",
            is_active=True
        ),
        User(
            name="Natalia Rojas",
            email="natalia.rojas@example.com",
            role="user",
            is_active=True
        ),
        User(
            name="Felipe Medina",
            email="felipe.medina@example.com",
            role="admin",
            is_active=True
        ),
        User(
            name="Paula Jimenez",
            email="paula.jimenez@example.com",
            role="support",
            is_active=True
        ),
        User(
            name="Jorge Alvarez",
            email="jorge.alvarez@example.com",
            role="user",
            is_active=True
        ),
        User(
            name="Diana Castillo",
            email="diana.castillo@example.com",
            role="user",
            is_active=True
        ),
        User(
            name="Kevin Muñoz",
            email="kevin.munoz@example.com",
            role="user",
            is_active=True
        ),
        User(
            name="Juliana Peña",
            email="juliana.pena@example.com",
            role="support",
            is_active=True
        ),
        User(
            name="Esteban Lozano",
            email="esteban.lozano@example.com",
            role="user",
            is_active=True
        ),
        User(
            name="Karen Navarro",
            email="karen.navarro@example.com",
            role="user",
            is_active=True
        ),
    ]

    db.add_all(users)
    db.commit()

    print("✅ 20 usuarios creados correctamente")

    db.close()


if __name__ == "__main__":
    seed_users()