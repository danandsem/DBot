def valid_image(f):
    for extension in [".jpg", ".jpeg"]:
        if f.endswith(extension):
            return True
    return False