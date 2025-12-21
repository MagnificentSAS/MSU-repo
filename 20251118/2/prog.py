import sys

text = sys.stdin.read()

corrected_text = (text.encode('latin1', errors='replace').decode('cp1251', errors='replace')
                  .encode('utf-8').decode('utf-8'))
print(corrected_text)