# Water's Quality Check Project - If it is potable or not ?

## Description of the Problem :
- Access to safe drinking-water is essential to health, a basic human right and a component of effective policy for health protection. This is important as a health and development issue at a national, regional and local level. In some regions, it has been shown that investments in water supply and sanitation can yield a net economic benefit, since the reductions in adverse health effects and health care costs outweigh the costs of undertaking the interventions.

(For more information read this dataset on Kaggle - https://www.kaggle.com/datasets/adityakadiwal/water-potability )
(The downloaded data is already available in `data` directory and trained model in `model` directory)

**We used different Machine Learning algorithms(Logistic Regression, Decision Trees, Random Forest Classifier, Gradient Bossting Decision Trees etc to predict if the given water sample is potable or not? and also deploy that service to EC2 instance in Docker container**

- Libaries/Language Used : Python3, Sklearn, Numpy, Pandas, Matplotlib, Seaborn, flask, gunicorn, pipenv etc
- Technologies/Cloud : AWS cloud for workspace or/and Deployment 

### Content of the dataset 

The water_potability.csv file contains water quality metrics for 3276 different water bodies.

**1. pH value:**

PH is an important parameter in evaluating the acid–base balance of water. It is also the indicator of acidic or alkaline condition of water status. WHO has recommended maximum permissible limit of pH from 6.5 to 8.5. The current investigation ranges were 6.52–6.83 which are in the range of WHO standards.

**2. Hardness:**

Hardness is mainly caused by calcium and magnesium salts. These salts are dissolved from geologic deposits through which water travels. The length of time water is in contact with hardness producing material helps determine how much hardness there is in raw water. Hardness was originally defined as the capacity of water to precipitate soap caused by Calcium and Magnesium.

**3. Solids (Total dissolved solids - TDS):**

Water has the ability to dissolve a wide range of inorganic and some organic minerals or salts such as potassium, calcium, sodium, bicarbonates, chlorides, magnesium, sulfates etc. These minerals produced un-wanted taste and diluted color in appearance of water. This is the important parameter for the use of water. The water with high TDS value indicates that water is highly mineralized. Desirable limit for TDS is 500 mg/l and maximum limit is 1000 mg/l which prescribed for drinking purpose.

**4. Chloramines:**

Chlorine and chloramine are the major disinfectants used in public water systems. Chloramines are most commonly formed when ammonia is added to chlorine to treat drinking water. Chlorine levels up to 4 milligrams per liter (mg/L or 4 parts per million (ppm)) are considered safe in drinking water.

**5. Sulfate:**

Sulfates are naturally occurring substances that are found in minerals, soil, and rocks. They are present in ambient air, groundwater, plants, and food. The principal commercial use of sulfate is in the chemical industry. Sulfate concentration in seawater is about 2,700 milligrams per liter (mg/L). It ranges from 3 to 30 mg/L in most freshwater supplies, although much higher concentrations (1000 mg/L) are found in some geographic locations.

**6. Conductivity:**

Pure water is not a good conductor of electric current rather’s a good insulator. Increase in ions concentration enhances the electrical conductivity of water. Generally, the amount of dissolved solids in water determines the electrical conductivity. Electrical conductivity (EC) actually measures the ionic process of a solution that enables it to transmit current. According to WHO standards, EC value should not exceeded 400 μS/cm.


**7. Organic_carbon:**

Total Organic Carbon (TOC) in source waters comes from decaying natural organic matter (NOM) as well as synthetic sources. TOC is a measure of the total amount of carbon in organic compounds in pure water. According to US EPA < 2 mg/L as TOC in treated / drinking water, and < 4 mg/Lit in source water which is use for treatment.

**8. Trihalomethanes:**

THMs are chemicals which may be found in water treated with chlorine. The concentration of THMs in drinking water varies according to the level of organic material in the water, the amount of chlorine required to treat the water, and the temperature of the water that is being treated. THM levels up to 80 ppm is considered safe in drinking water.

**9. Turbidity:**

The turbidity of water depends on the quantity of solid matter present in the suspended state. It is a measure of light emitting properties of water and the test is used to indicate the quality of waste discharge with respect to colloidal matter. The mean turbidity value obtained for Wondo Genet Campus (0.98 NTU) is lower than the WHO recommended value of 5.00 NTU.

**10. Potability:**

Indicates if water is safe for human consumption where 1 means Potable and 0 means Not potable.


## Instructions on how to run the project
- Note - Preferred Environment (Linux Based - Ubuntu, Redhat, CentOS etc ), also we used the AWS Cloud for the deployment.

### To Run/Deploy the Project in Docker Container on EC2 Machine - 
- Note : You can create the AWS account and use the free tier for 12 months (check the website for more details)

1 ) Create the EC2 instance (t2.micro eligible for free tier) (Specs -- Amazon AMI -- Allow the ports-> http, https, custom tcp port 9696, ssh in Security Group of your EC2 instance )

2 ) Go to Security Group --> Edit Inbound SG Rules --> Custom TCP --> allow port 9696 ---> Source: anywhere IPv4

3 ) shh into the EC2 instance from your local machine using the key which was generated during the EC2 creation
- After SSH into your remote EC2 machine, run these commands

4 ) `sudo su -` 

5 ) `yum update -y` 

6 ) `yum install docker`

7 ) `systemctl start docker`

8 ) `systemctl enable docker`

9 ) `systemctl status docker`   (# it must show the status as enable/start with green color font)

10 ) `yum install git -y`

11 ) Clone the repository using --> `git clone https://github.com/modfa/Water_Quality_Check_ML_Project.git`


12 ) `cd Water_Quality_Check_ML_Project`

13 ) To build the image for running the container

        `docker build -t projectimage .`
        
     Command to run the docker container
     
        `docker run -it -p 9696:9696 --rm projectimage:latest`
        
14 ) update the `predict_test.py` file and change it to 

`url = 'http://{your_ec2_instance_public_ip_address}:9696/predict'`  # {43.204.148.161} This is the public IP for your EC2 instance and you have to change it your assigned public IP address

15 ) Now run the python `predict_test.py` file from your local system (terminal) using `python predict_test.py` and you will see the prediciton from the model which has been deployed on Docker Container on EC2


### To Run/Deploy the Project Locally on docker container -

1 ) Make sure your system has python > 3.9 version installed

2 ) Docker installed and running/active

3 ) Git installed

4 ) Clone the repository using --> `git clone https://github.com/modfa/Water_Quality_Check_ML_Project.git` 

5 ) `cd Water_Quality_Check_ML_Project`

6 ) To build the image for running the container
        `docker build -t projectimage .`
        
7 ) Command to run the docker container
        `docker run -it -p 9696:9696 --rm projectimage:latest`
        
8 ) Update the `predict_test.py` file and change it to localrun on local host/uncomment the line (read the file for more)

9 ) Now run the python `predict_test.py` file from your local system using `python predict_test.py` and you will see the prediciton from the model which has been deployed on Docker Container on EC2


###  Note: This repository include the `notebook.ipynb` , `train.py` , `predict.py` , `Dockerfile` etc if you want to explore the project in much more details.
