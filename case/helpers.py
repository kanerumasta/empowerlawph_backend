import uuid
import hashlib
import re

def generate_unique_case_id(decision_date, case_number, case_exists_func):
    """
    Generate a unique case ID using metadata:
    - Prefix from case number (G.R., A.M., etc.)
    - Last 2 digits of the decision year
    - Hash of the case number
    """

    # Extract prefix (e.g., "G.R.", "A.M.") using regex
    match = re.match(r"([A-Z.]+)\s+NO\.\s+([\d-]+)", case_number.upper())
    if match:
        prefix = match.group(1).replace(".", "")  # Remove dots (e.g., "GR")
    else:
        prefix = "CASE"  # Default if no prefix found

    # Extract last 2 digits of the year
    year_suffix = str(decision_date.year)[-2:]

    # Hash the case number (ensures uniqueness)
    case_hash = hashlib.sha256(case_number.encode()).hexdigest()[:8].upper()

    # Construct unique ID
    unique_id = f"{prefix}{year_suffix}{case_hash}"

    # Ensure uniqueness using the passed function
    while case_exists_func(unique_id):
        unique_id = f"{prefix}{year_suffix}{uuid.uuid4().hex[:8].upper()}"

    return unique_id


