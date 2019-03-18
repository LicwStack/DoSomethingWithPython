import base64


def convert_image():
    # Picture ==> base64 encode
    with open('E:\GitHub\DoSomethingWithPython\opencv-python\messi5.jpg', 'rb') as fin, open('E:\GitHub\DoSomethingWithPython\opencv-python\messi5.txt', 'w') as fout:
        fout.write(base64.b64encode(fin.read()).decode())

    # base64 encode ==> Picture
    with open('E:\GitHub\DoSomethingWithPython\opencv-python\messi5.txt', 'r') as fin, open('E:\GitHub\DoSomethingWithPython\opencv-python\messi52.jpg', 'wb') as fout:
        fout.write(base64.b64decode(fin.read()))


if __name__ == '__main__':
    convert_image()
