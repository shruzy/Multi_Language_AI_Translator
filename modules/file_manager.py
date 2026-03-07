import os
import time

def save_text(text, folder):

    filename = str(int(time.time())) + ".txt"

    path = os.path.join(folder, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    return path