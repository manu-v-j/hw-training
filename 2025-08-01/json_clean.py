import json
import re

unwanted = ["\u00e2", "\u0080", "\u0099", "\u00ae", "\u00c2", "\u0094", "\u0093", "💯"]
cleaned_data = []

with open('/home/user/Hashwave/2025-08-01/robertsbrothers.json', 'r', encoding='utf-8') as f:
    for line in f:
        record = json.loads(line)

        for key, value in record.items():
            if isinstance(value, str):
                for item in unwanted:
                    value = value.replace(item, "")

                value = re.split(r'Testimonials', value, maxsplit=1)[0].strip()

                record[key] = value

        cleaned_data.append(record)

with open('robertsbrothers_clean.json', 'w', encoding='utf-8') as f:
    for record in cleaned_data:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

