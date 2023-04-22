text = "X-DSPAM-Confidence: 0.8475"
start_index = text.find(":") + 1
number = float(text[start_index:].strip())
print(number)
