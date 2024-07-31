



# Rocketbot Xperience
  
Module to work with forms of Rocketbot Xperience  

*Read this in other languages: [English](Manual_Xperience.md), [Português](Manual_Xperience.pr.md), [Español](Manual_Xperience.es.md)*
  
![banner](imgs/Banner_Xperience.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Login NOC
  
Login to NOC using one of the options, API Key, noc.ini file, or credentials.
|Parameters|Description|example|
| --- | --- | --- |
|URL Server|Server URL|https://roc.myrb.io/|
|Select a method to connect to the Orchestrator|Options to login to R.O.C, you can use user credentials, API Key or by selecting noc.ini file|API Key|
|Proxies|Proxies with which the session will be configured. Indicate the protocol followed by the server|http://00.00.000.000:0000|
|User proxie|Optional. Complete if required to configure proxies.|user/user|
|Password proxie|Optional. Complete if required to configure proxies.|#Aa000000.Aa0000000a#|
|Assign result to a Variable|Variable where the state of the connection will be stored, returns True if it is successful or False otherwise|Variable|

### Get Form queue
  
Get queues
|Parameters|Description|example|
| --- | --- | --- |
|Form Token|Form Token|8YWUW8AXAV3UPNKY|
|Set to var|Variable to store result without {}|var|

### Get Form queue locked
  
Get queues locked
|Parameters|Description|example|
| --- | --- | --- |
|Form Token|Form Token|8YWUW8AXAV3UPNKY|
|Set to var|Variable to store result without {}|var|

### Get all Form queue data
  
Get all Form data from queue. The command returns the data in dictionary format
|Parameters|Description|example|
| --- | --- | --- |
|Queue ID|Queue ID|1|
|Form Token|Form Token|8YWUW8AXAV3UPNKY|
|Autocomplete variables|The result will be assigned to the variables already created|True|
|Set to var|Variable to store result without {}|var|

### Download Form File
  
Download a file uploaded in a form
|Parameters|Description|example|
| --- | --- | --- |
|Queue ID|Queue ID|1|
|File|Var that contains file path of queue|file.pdf|
|Save file to|Path where file will be saved|C:\Rocketbot\file.ini|

### Update Form queue status
  
Change status to form queue
|Parameters|Description|example|
| --- | --- | --- |
|Status|Select the status of the queue|Done|
|Queue ID|Enter the ID of the queue|1|
|Set to var|Var without {} where the result will be saved|variable|

### Return Message to Xperience
  
Returns a message to the Xperience form
|Parameters|Description|example|
| --- | --- | --- |
|Xperience Token|Xperience Token|{xperience}|
|Message to return|Message to return|This is a message|

### Send a file to Xperience
  
Send a file whenever the Form's SEND API option is active
|Parameters|Description|example|
| --- | --- | --- |
|Xperience Token|Token {xperience} that is generated with the 'Get data from Form' command|{xperience}|
|File to upload|File path to send to the orchestrator|C:/Users/pc/Downloads/img.png|
|Set to var|Var where the result will be saved|variable|

### Search data in form
  
This command allows you to search for data in an Xperience form
|Parameters|Description|example|
| --- | --- | --- |
|Form Token|Form Token|8YWUW8AXAV3UPNKY|
|ID of the element|ID of the element to search|User|
|Value to search|Value to search in the selected input|Rocketbot|
|Autocomplete variables|The result will be assigned to the variables already created|True|
|Lock form queue|The form queue will be locked in the Orchestrator|True|
|Assign results to variable|Variable to store result without {}|var|
|Set id of the form queue to variable|Variable to store id of the form queue|var|
