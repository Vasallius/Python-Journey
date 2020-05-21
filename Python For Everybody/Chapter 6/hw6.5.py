text = "X-DSPAM-Confidence:    0.8475"

index = text.find(':')

int = text[index+1:]

int = float(int)
print(int)