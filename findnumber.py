text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(':')
output= text[18+4:]

print(float(output))
