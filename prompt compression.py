import re

def compress(text):
  if not text:
    return text
  # Collapse repeated whitespace/newlines
  text = re.sub(r"[ \t]+", " ", text)
  text = re.sub(r"\n\s*\n+", "\n", text)
  # Strip leading/trailing whitespace on each line
  text = "\n".join(line.strip() for line in text.split("\n"))
  return text.strip()

def main(input):
  compressed_system_prompt = compress(input["system_prompt"])
  compressed_output_schema = compress(input["output_schema"])
  return {
    "system_prompt": compressed_system_prompt,
    "output_schema": compressed_output_schema
  }
