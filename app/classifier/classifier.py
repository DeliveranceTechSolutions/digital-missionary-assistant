# Classifier is a controller for the Evaluator and PreProcessor classes
class Classifier:
    def __init__(
        self, 
        db_driver, 
        processor_driver, 
        evaluator_driver, 
        model_driver
    ):
      self.db       = db_driver 
      self.pre      = processor_driver
      self.eval     = evaluator_driver
      self.model    = set_model(model_driver)
      self.test = "testing if main has been protected"

    
    def set_model(model_driver):
        if model_driver == SVM:
            self.model = SVMModel()
        elif model_driver == BERT:
            self.model = BERTModel()
        else:
            print("Error incorrect model type")

class SVMModel: 
    def __init__():
        self.encode = ""
        self.vect = ""
        self.model = ""

    def load(self, label):
        modelsFolderTemplate = "".join([svmCreate.SVM_MODELS_FOLDER, label])
        self.encode = pickle.load(open(
            "".join([modelsFolderTemplate, 'encode.pkl']),
            'rb',
        ))

        self.vect = pickle.load(open(
            "".join([modelsFolderTemplate, 'vect.pkl']), 
            'rb',
        ))

        self.model = pickle.load(open(
            "".join([modelsFolderTemplate, 'model.sav']),
            'rb',
        ))

class BERTModel:
    def __init__():
        self.BertModel = ""
        self.BertTokenizer = ""
        self.BertClassifier = ""

    def load(self, label):
        self.BertModel = AutoModelForSequenceClassification.from_pretrained(
            "".join(['./', bertCreate.BERT_FOLDER_PATH, label, '/'])
        )

        self.BertTokenizer = AutoTokenizer.from_pretrained(
            "".join(['./' + bertCreate.BERT_FOLDER_PATH + label + '/'])
        )

        self.BertClassifier = pipeline(
            task='text-classification', 
            model=self.BertModel, 
            tokenizer=self.BertTokenizer, 
            truncation=True, 
            max_length=bertCreate.MAX_LENGTH_OF_EMAIL
        )
