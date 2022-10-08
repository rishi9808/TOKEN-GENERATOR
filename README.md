# TOKEN-GENERATOR


## Stack used :: PYTHON , MYSQL DATABASE


**CLIENT SIDE**

Our Program takes the patient details such as Patient name, Age, Phone Number and the Doctor to be consulted.Once the data is entered for a patient a unique token number will be generated for that patient. 
The Token is generated sequentially in such a way that each patient gets unique token and each token corresponds to the patient details.

**SERVER SIDE**

This part of the program is accessible to the Hospital system.
For each data of patient received from the client side, is stored in the database.
For this we used Mysql server which is connected to our Python program.
Once a patient detail is entered a token in generated in the sql table. 
This token value is displayed at the client side.

**PRESENTATION LINK**

[presentation link](https://www.canva.com/design/DAFOcmRsQ6A/EwZrMv0AdzjyINqqjCGrvA/edit?utm_content=DAFOcmRsQ6A&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)


![output](https://user-images.githubusercontent.com/81485622/194708073-69d46270-3864-4b48-a7cd-69e2af7cf55c.jpg)
![sql table](https://user-images.githubusercontent.com/81485622/194708078-8daa26cf-2311-44f8-83ea-01596f3c27d6.jpg)
![table desc](https://user-images.githubusercontent.com/81485622/194708083-b7ef0bd6-6f5b-4129-8345-5cae8050bc27.jpg)
