"""implement a program that prompts the user for the name of a file and then outputs that
file’s media type if the file’s name ends, case-insensitively"""
#str.endswith(suffix[, start[, end]])

def extensions(file_name):
    file_name = file_name.strip()  # Remove any leading/trailing whitespace

    #if statement to check if the file name ends with a specific extension and return the media type
    if not file_name:
        return "Not a valid file name"
    if file_name.lower().endswith(".gif"):
        return "image/gif"
    elif file_name.lower().endswith(".jpg") or file_name.lower().endswith(".jpeg"):
        return "image/jpeg"
    elif file_name.lower().endswith(".png"):
        return "image/png"
    elif file_name.lower().endswith(".pdf"):
        return "application/pdf"
    elif file_name.lower().endswith(".txt"):
        return "text/plain"
    elif file_name.lower().endswith(".zip"):
        return "application/zip"
    elif file_name.lower().endswith(".tar"):
        return "application/x-tar"
    elif file_name.lower().endswith(".mp3"):
        return "audio/mpeg"
    elif file_name.lower().endswith(".mp4"):
        return "video/mp4"
    else:
        return "application/octet-stream" #common default for unknown file types

def main():
    file_name = input("Enter the name of the file: ")
    media_type = extensions(file_name)
    print(media_type)

main()




