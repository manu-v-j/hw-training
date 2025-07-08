import json
import re

def clean_warning(val):
    try:
        # Remove malformed entries like {"warning":"} or {"warning":"}] before parsing
        val = re.sub(r',?\s*\{"warning":"\}*"\}', '', val)

        # Now safely load the JSON
        json_val = json.loads(val.replace('""', '"'))

        # Extract and clean valid warning strings
        warnings = [w['warning'].strip() for w in json_val if 'warning' in w and w['warning'].strip()]
        return ' '.join(warnings) if warnings else None
    except Exception as e:
        return val



bad_json = '''[{"warning":"Do not use"},{"warning":"Ask a doctor before use if you have"},{"warning":"When using this product"},{"warning":"Ask a doctor or pharmacist before use if you are taking sedatives or tranquilizers"},{"warning":"If pregnant or breast-feeding, ask a health professional before use."},{"warning":"Keep out of reach of children. In case of overdose, get medical help or contact a Poison Control Center right away. (1-800-222-1222)"},{"warning":"}]'''
print(clean_warning(bad_json))