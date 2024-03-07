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
