text = "X-DSPAM-Confidence:    0.8475";
found = text.find("0")
num=float(text[found:])
print(num)