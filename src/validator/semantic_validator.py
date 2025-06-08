from src.topology.torsion_checker import check_torsion_violation
from src.utils.logger import log

def validate_semantics(text):
    log(f"Validating: {text}")
    return not check_torsion_violation(text)
