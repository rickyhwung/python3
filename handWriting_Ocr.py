from aip import AipOcr

APP_ID = '16212043'
API_KEY = 'RyGkApu52Z6GFcaPsMVDvDIe'
SECRET_KEY = 'jLfKLdHX3P4QfYTWYXrC6yhHEgdlukdi'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

filepath = 'example.jpg'
image = get_file_content(filepath)

options = {}
options["recognize_granularity"] = "big"

res_ocr = client.handwriting(image, options)
print(res_ocr)