# streaming-03-bonus-kamalini
Created by Kamalini Pradhan
Date: 16 May 2024
Northwest Missouri State University
Data Streaming 44671-80/81
Dr. Case

# Overview:
Demonstrating the use of a message broker software, specifically RabbitMQ with student data csv Data file. 

# Table of Contents:
1. [File List](File_List)
2. [Machine Specs & Terminal Information](Machine_Specs_&_Terminal_Information)
3. [Prerequisites](Prerequisites)
4. [Data Source](Data_Source)
5. [Creating Environment & Installs](Creating_an_Enviroment_&_Installs)
6. [Method](Method)
    - [The Emitter/Producer](The_Emitter/Producer)
    - [The Listener/Consumer](The_Listener/Consumer)



# File List
| File Name | Repo location | Type |
| ----- | ----- | -----|
| util_logger.py | utils folder | python script |
| producer_of_message.log | logs | log |
| consumer_of_message.log | logs | log |
| requirements.txt | main repo | text |
| student_details.csv | main repo | csv |
| producer_of_message.py | main repo | python script |
| consumer_of_message.py | main repo | python script |
| EmittingListeningSplit1 | image folder | PNG |


# Machine Specs & Terminal Information

    * Date and Time: 2024-05-16 at 07:50 AM
    * Operating System: nt Windows 10
    * System Architecture: 64bit
    * Number of CPUs: 12
    * Machine Type: AMD64
    * Python Version: 3.11.4
    * Python Build Date and Compiler: main with Jul  5 2023 13:47:18
    * Python Implementation: CPython
    * Terminal Environment:        VS Code
    * Terminal Type:               cmd.exe
    * Preferred command:           python

# Prerequisites
1. Git
2. Python 3.7+ (3.11+ Preferred)
3. VS Code Editor
4. VS Code Extension: Python (by Microsoft)
5. RabbitMQ Server installed and running locally

Be sure that RabbitMQ is installed and running. For more information on RabbitMQ and its installation please see [RabbitMQ Home Page](https://www.rabbitmq.com/).

# Data Source

Here i am generating data ussing studentdatacreate.py script . This will generate student_details.csv file which i have used in producer_of_message script to add each row in csv file as a message .


# Creating an Enviroment & Installs
RabbitMQ requires the Pika Library to function, this is addressed through the creation of an environment and installing it. Use the following command to create an environment, when prompted in VS Code set the .env to a workspace folder, and select yes.

```
python -m venv .venv # Creates a new environment
.\Scripts\activate # activates the environment
```

Once the environment is created install the following:
```
python -m pip install -r requirements.txt
```
For more information on Pika see the [Pika GitHub](https://github.com/pika/pika)

# Method 
To stream data utilizing RabbitMQ architecture we need to build both a Producer and Consumer. The Producer publishes the message, which in this case is being pulled from the MTA file that is in the repository. The Consumer decodes and receives these messages. Both of these are essential to the process and in this case, are structured to read from a csv and output a text file that can be stored later. 

## The Emitter/Producer
The Emitter/Producer is a script that allows us to publish data to a queue, that the Consumer can receive. In this particular case, to properly stream the student_details.csv file. These are as follows:
    1. Get the Data
    2. Read the Data
    3. Prepare the data to publish to the queue
    4. Send the Data

Obtaining the data that would be streamed is a series of steps, the first is establishing the input_file and defining which columns would be used. 

```
studentdata = "student_details.csv"

```
# CSV Read
    with open(studentdata, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
    
        # get the headers (first row)
        headers = next(csvreader)
    
        # iterate over each row in the CSV
        for row in csvreader:
            # construct the message from the row
            message = ', '.join(f"{header}: {value}" for header, value in zip(headers, row))
        
            # print a message to the console for the user
            print(f" [x] Sent '{message}'")
            
```
```
# Send the data 
send_message("localhost", "student", message)
```

```
Durability was turned on to save a copy of the message to the drive, by doing this it makes receiving the message and creating an output file possible. Handling exceptions and interruptions is important - especially when streaming a large amount of data. This was addressed utilizing the following Exceptions:

```
except KeyboardInterrupt:
        logging.info("KeyboardInterrupt. Stopping the program.")
    except pika.exceptions.AMQPConnectionError as e:
        logger.error(f"Error: Connection to RabbitMQ server failed: {e}")
        sys.exit(1)
finally:
        # Closing the connection
        logging.info("\nclosing connection. Goodby\n")
        conection.close()
```

![Initial Run of Producer and Consumer](/images/EmittingListeningSplit1.PNG)

## The Listener/Consumer
The Listener/Consumer serves to receive data from the queue. In this instance, the objective is to produce an output text file with the data from the MTAHourlyData50.csv. Several steps must occur:
    
    1. Function to Process Messages from Queue
    2. Handling Exceptions/FailuresRetrieving the Messages from the queue
    3. Retrieving the Messages from the queue
    5. Executing the Script and Getting them


```
def main(hn: str = "localhost"):
    try:
        # Creating block connection to RabbitMQ server
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    except Exception as e:
        logger.error()
        logger.error("ERROR: connection to RabbitMQ server failed.")
        logger.error(f"Verify the server is running on host={connection}.")
        logger.error(f"The error says: {e}")
        logger.error()
        sys.exit(1)
```

# Resources
1. Pika Information: https://github.com/pika/pika
2. RabbitMQ documentation: https://www.rabbitmq.com/docs
3. RabbitMQ Tutorials: https://www.rabbitmq.com/tutorials