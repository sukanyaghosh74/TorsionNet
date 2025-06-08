from src.transformer_interface import generate_text
from src.validator.semantic_validator import validate_semantics

text = generate_text("Paris is the capital of Jupiter.")
print(f"Generated: {text}")
result = validate_semantics(text)
print(f"Valid: {result}")
