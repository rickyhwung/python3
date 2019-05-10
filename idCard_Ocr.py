from aip import AipOcr

APP_ID = '16212043'
API_KEY = 'RyGkApu52Z6GFcaPsMVDvDIe'
SECRET_KEY = 'jLfKLdHX3P4QfYTWYXrC6yhHEgdlukdi'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

filepath = 'idCard1.jpg'
image = get_file_content(filepath)
idCardSide = "front"

options = {}
options["detect_direction"] = "true"
options["detect_risk"] = "false"

res_ocr = client.idcard(image, idCardSide, options)

idArray = ['住址','出生','姓名','公民身份号码','性别','民族']

res_ocr_words_res = res_ocr['words_result']
for i in range(0,res_ocr_words_res.__len__()):
    print('{}: {}'.format(idArray[i],res_ocr_words_res[idArray[i]]['words']))