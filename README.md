# covid19CloudCRUDTool
Provides CRUD capabilities to a cloud mongoDB cluster(set up using Atlas service).

* Covid19 dataset is stored in the model directory
* model/CovidDB communicates directly with a mongoDB cluster(password and login available upon request).
* view/starter processes user inputs and passes them on to controller/covidController which talks directly to the model/covidDB
* model/datasetdf.py, and controller/controller.py are for CRUD only on the csv dataset (this was needed for an assignment)

APIs used
* pymongo
* pandas
* ssl
* numpy

Features
* Upload/reupload the dataset to the cloud
* CRUD on the dataset in the cloud
* CRUD on the local csv file
* Load data into memory and perform CRUD
* Save from memory to a new csv file
