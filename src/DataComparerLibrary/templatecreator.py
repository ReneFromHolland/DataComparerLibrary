import os
import re
import yaml
from datetime import datetime
from dateutil.relativedelta import relativedelta

class TemplateCreator:
    # Pattern used for conversion.
    DATE_PATTERNS = [
        (re.compile(r"\b[A-Z]{3}\d{4}\b"), "{SKIP}.{NOW():YY}"),       
        (re.compile(r"\b([A-Z]{3}).(\d{4})\b"), "{SKIP}.{NOW():YY}"),
        # YYYYMMDD
        (re.compile(r"\b(\d{4})(\d{2})(\d{2})\b"), "{NOW():YYYYMMDD}"),
        # YYYY-MM-DD
        (re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b"), "{NOW():YYYY-MM-DD}"),
        # DD-MM-YYYY
        (re.compile(r"\b(\d{2})-(\d{2})-(\d{4})\b"), "{NOW():DD-MM-YYYY}"),
        # DD-Month-YYYY (Month name)
        (re.compile(r"\b(\d{2})-([A-Za-z]{3})-(\d{4})\b"), "{NOW():DD}-{SKIP}-{NOW():YYYY}"),
        # DD-Month-YY (Month name)
        (re.compile(r"\b(\d{2})[-‑–—]([A-Za-z]{3})[-‑–—](\d{2})\b"), "{NOW():DD}-{SKIP}-{NOW():YY}"),
        (re.compile(r"\b(\d{2})[-‑–—](\w{3})[-‑–—](\d{2})\b"), "{NOW():DD}-{SKIP}-{NOW():YY}"),
        (re.compile(r"\b\d{2}-[A-Z]{3}-\d{2}\b"), "{NOW():DD}-{SKIP}-{NOW():YY}"),
        (re.compile(r"\b\d{2}[A-Z]{3}\d{2}\b"), "{NOW():DD}{SKIP}{NOW():YY}"),
        (re.compile(r"\b\d{2}.(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC).\d{2}\b"), "{NOW():DD}-{SKIP}-{NOW():YY}")
     
    ]

#02-JUN-26 13.19.01.466133000 

    TIMESTAMP_PATTERN_1 = re.compile(r"\b\d{2}:\d{2}:\d{2}\.\d{6}\b")
    TIMESTAMP_PATTERN_2 = re.compile(r"\b\d{2}:\d{2}:\d{2}\.\d{9}\b")
    TIMESTAMP_PATTERN_3 = re.compile(r"\b\d{2}:\d{2}:\d{2}\b")
    TIMESTAMP_PATTERN_4 = re.compile(r"\b\d{2}.\d{2}.\d{2}\.\d{9}\b")



    AMPM_PATTERN = re.compile(r"\b(AM|PM)\b")

    def convert_data_file_into_template_file(self, input_path, yaml_file=None, yaml_extra=None):
        # --- Load YAML variables ---
        variables = {}
        if yaml_file and os.path.exists(yaml_file):
            with open(yaml_file, "r") as f:
                variables.update(yaml.safe_load(f) or {})

        if yaml_extra and os.path.exists(yaml_extra):
            with open(yaml_extra, "r") as f:
                variables.update(yaml.safe_load(f) or {})

        # --- Process file or directory ---
        if os.path.isdir(input_path):
            for root, _, files in os.walk(input_path):
                for file in files:
                    self.__process_file(os.path.join(root, file), variables)
        else:
            self.__process_file(input_path, variables)


    def __process_file(self, file_path, variables):
        if not os.path.exists(file_path):
            return

        with open(file_path, "r") as f:
            content = f.read()

        # --- Replace YAML variable values ---
        for key, value in variables.items():
            if isinstance(value, str):
                pattern = re.escape(value)
                content = re.sub(pattern, f"{{{key}}}", content)

        # --- Replace timestamps ---
        content = self.TIMESTAMP_PATTERN_1.sub("{SKIP}", content)
        content = self.TIMESTAMP_PATTERN_2.sub("{SKIP}", content)
        content = self.TIMESTAMP_PATTERN_3.sub("{SKIP}", content)
        content = self.TIMESTAMP_PATTERN_4.sub("{SKIP}", content)

        # --- Replace AM/PM ---
        content = self.AMPM_PATTERN.sub("{SKIP}M", content)

        # --- Replace dates ---
        #now = datetime.now()

        def __replace_date(match, template):
            now = datetime.now()

            original = match.group(0)
            parsed_date = self.__parse_date(original)

     #       print("parsed_date: ", parsed_date)

            if not parsed_date:
     #           print("origineel")
                return original

            delta = relativedelta(parsed_date, now)

            if delta.years == 0 and delta.months == 0 and delta.days == 0:
                return template

            # Build relative expression
            parts = []
            if delta.years != 0:
                parts.append(f"{abs(delta.years)}Y")
            if delta.months != 0:
                parts.append(f"{abs(delta.months)}M")
            if delta.days != 0:
                parts.append(f"{abs(delta.days)}D")

            sign = "+" if parsed_date > now else "-"

            return f"{{NOW(){sign}{''.join(parts)}:{template[7:-1]}}}"

   #     print("hier")
        for pattern, template in self.DATE_PATTERNS:
   #         print("hier2")
  #          print(pattern)
  #          print(template)
            content = pattern.sub(lambda m: __replace_date(m, template), content)

 #       print("===========")
        # --- Write back ---
        with open(file_path, "w") as f:
            f.write(content)


    # --- Helper: parse date in multiple formats ---
    def __parse_date(self, text):
#        formats = ["%Y%m%d", "%Y-%m-%d", "%d-%m-%Y"]
        formats = ["%Y%m%d", "%Y-%m-%d", "%d-%m-%Y", "%d-%b-%Y", "%d-%b-%y"]
        for fmt in formats:
            try:
                return datetime.strptime(text, fmt)
            except ValueError:
                pass
        return None





