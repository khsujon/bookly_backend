from passlib.context import CryptContext


password_context = CryptContext(schemes=["bcrypt"])


# Utility function to hash passwords
def generate_password_hash(password: str) -> str:
    hash= password_context.hash(password)
    return hash