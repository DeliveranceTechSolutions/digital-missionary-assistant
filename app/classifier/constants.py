SVM = 'SVM'
MODEL_TO_USE = SVM 
FINAL_ONLY = False
HF_MODEL = bertCreate.CHECKPOINT
CSV_IS_CLEANED = False
CSV_TO_EVALUATE = pre.CSV_OUTPUT_FOLDER + pre.COMBINED_CSV_FILE
CSV_EVALUATED = pre.CSV_OUTPUT_FOLDER + f'Evaluated - {bertCreate.CHECKPOINT_NAME if MODEL_TO_USE == HF_MODEL else SVM} - {pre.COMBINED_CSV_FILE}' 
FIELD_TO_TRAIN_ON = pre.FIELD_TO_TRAIN_ON
LABEL_FIELD = pre.LABEL_FIELD
ISOLATED_LABEL_ORDER = pre.LIST_OF_LABELS
DEFAULT_LABEL = "5 Various"

SAVE_UNPROCESSED_DATA = False
FOLDER_PATH_TO_MAILBOX_FILES = "TakeOutData/"
CSV_OUTPUT_FOLDER = "CSV_Output/"
COMBINED_CSV_FILE = 'Manually Tagged Data UTF8 2nd Label Revision.csv'
CLEANED_CSV_FILE = CSV_OUTPUT_FOLDER + 'Cleaned - ' + COMBINED_CSV_FILE
IMPORT_FIELD_TO_TRAIN_ON = 'EmailBody'
FIELD_TO_TRAIN_ON = 'EmailBody'
IMPORT_LABEL_FIELD = 'New Labels' # this will be changed to 'labels' for Hugging Face
LABEL_FIELD = 'labels'
INBOX_OWNER_EMAIL = "Inspiracion@carypalmon.org"
MESSAGE_ID = 'MessageID'
UNKNOWN_LABEL = "Unknown Label"
LIST_OF_LABELS = ['2 Book Request','3 Prayer Request','5 Various','1 No Response Needed']
SIGNATURES_TO_REMOVE_AFTER = [
    '-------- Mensaje original --------',
    'Enviado desde Yahoo',
    '<inspiracion+carypalmon.org@ccsend.com>',
    INBOX_OWNER_EMAIL,
    "<\n" + INBOX_OWNER_EMAIL + "\n>",
    'Inspiracion Cary Palmon Ministries (',
    'reaccionó a través de\nGmail',
    'Cary Palmón Ministries (',
    ', Cary Palmón Ministries',
    'Enviado desde mi',
    'Obtener\nOutlook para Android',
    'De:\nCary',
    'De:\n<',
    ', Cary Palmon Ministries',
    'Outlook para Android',
    'Sent from my iPhone',
    '" Send For Moto g 8 Power"',
    '---------- Forwarded message ---------',
    'Enviado desde HUAWEI',
    'Libre de virus',
    'Enviado desde\nOutlook',
    'Sent from my MetroPCS'
]


# For removing outlier data
MESSAGE_IDS_TO_REMOVE = [
    # '<CALbQTR2URxjCmE7tuVC+maV7R8n1XM9D3OuTU5BE2erHvYOxjg@mail.gmail.com>',
    # '<CALbQTR3BT3rc8_3wAE+WuDXJ0UgX4Hc8_DQajoC2sENQXvAvDg@mail.gmail.com>',
    # '<CAJDEu3Oi=ZbJaLjPTqMMTOcRM3_Jm1inSFk8wbE2UJmdGFzOWg@mail.gmail.com>',
    # '<CAO8B5JbgrZasAMNV4vLaPm6xsoKV_Sr5pF1-D80Vkb=WQ76CCQ@mail.gmail.com>',
    # '<CANXk2nYDOOxWdvDbYgQv4N9-5A8KB+XukCNemcmOCV4_D1kisA@mail.gmail.com>',
    # '<CAOAbZTwGnHZRWvO9cwxEOpNTbdzTS0dho=nUy8rCkKnsbed8Rg@mail.gmail.com>',
]
