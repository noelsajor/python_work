name = input("File name: ").lower().strip()

if name.endswith("gif"):
    print("image/gif")

if name.endswith("jpg"):
    print("image/jpg")

if name.endswith("jpeg"):
    print("image/jpeg")

if name.endswith("png"):
    print("image/jpeg")

if name.endswith(".txt"):
    print("text/plain")

if name.endswith(".zip"):
    print("application/zip")

elif name.endswith("pdf"):
    print("application/pdf")

else:
    print("application/octet-stream")