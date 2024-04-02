import os
dirname = os.path.dirname(__file__)
ff = [os.path.join(dirname, "transcripts", f) for f in os.listdir(os.path.join(dirname, "transcripts")) if os.path.isfile(
    os.path.join(dirname, "transcripts", f))]

for file in ff:
    with open(file, "r") as f:
        content = f.read()
    content = content.replace("Cathy", "Kathy")
    with open(file, "w") as f:
        f.write(content)
