from app.data.user_db import users


def get_all_users(role=None, is_active=None):

    filtered_users = users

    if role is not None:
        filtered_users = [
            user for user in filtered_users
            if user["role"] == role
        ]

    if is_active is not None:
        filtered_users = [
            user for user in filtered_users
            if user["is_active"] == is_active
        ]

    return filtered_users


def get_user_by_id(user_id: int):

    for user in users:
        if user["id"] == user_id:
            return user

    return None


def create_new_user(user_data: dict):

    new_user = {
        "id": len(users) + 1,
        **user_data
    }

    users.append(new_user)

    return new_user