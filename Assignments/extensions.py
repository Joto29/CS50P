def main():
    # prompt the user for file
    file_inp = input("File name: ").lower()

    # check conditions
    if file_inp.endswith(".gif"):
        print("image/gif")
    elif file_inp.endswith(".jpg") or file_inp.endswith(".jpeg"):
        print("image/jpeg")
    elif file_inp.endswith(".png"):
        print("image/png")
    elif file_inp.endswith(".pdf"):
        print("application/pdf")
    elif file_inp.endswith(".txt"):
        print("text/plain")
    elif file_inp.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


main()
