# Data Owner Domain Tools

## Dataset Specification Tool
    <TODO>

## InitializerTool
There are two formats supported to run the initialization tool:

1. Create one or more Virtual Machine(s) attached with a single digital contract and it's corresponding dataset. (Note that one digital contract holds access to one and only one dataset)
2. Create one or more Virtual Machine(s) each with a digital contract and a dataset. The contract and dataset in each virtual machine can be defined in a config file. This is for interrnal use only.

### Prerequisites
    - The Public IP Address of the WebServer running the SAIL WebServices aka the RestApiPortal.
    - Azure Credentials:
        * Application Id
        * Password
        * Tenant Id
    - Dataset (*.csvp) created using the SAIL Dataset Specification Tool.
    - The SAIL login credentials of the user.
    - The packaged binaries to be installed on the Virtual Machine i.e. SecureComputationalVirtualMachine.binaries

### Steps to run
#### Virtual Machines with same dataset
    Run the Initializer tool:
        1. './InitializarTool'
        2. Enter the Public IP address of the WebService
        3. Enter the SAIL login credentials
        4. Enter the Azure Credentials
        5. Select the Relevant Digital Contract listed on the Screen
        6. Provide the path to the dataset linked with that Digital Contract.
        7. Process to create the Virtual Machines.

#### Virtual Machines with different datasets

Create a configuration file to provide the InitializarTool with the digital Contract and the dataset file path. Each line of the config file represents one Virtual Machine to be created has the following format:

    <DigitalContract Guid> <Dataset file path>

One example of a config file(Initializer.conf) is:
```
{9489CF70-FF12-4E9F-A990-183CE28A0FB7} Dataset1.csvp
{98252BA2-7D29-47A9-AFCB-9B3CE153332F} Dataset2.csvp
{81F3083C-12BF-4CB2-AE59-0C5BBF07E34A} Dataset3.csvp
{81F3083C-12BF-4CB2-AE59-0C5BBF07E34A} Dataset3.csvp
```
This kind of a config file will create 4 Virtual Machines, the first 3 will have different datasets while the 4th will be same as the 3rd one.

    Run the InitialiserTool with the config file:
        1. './InitializerTool --configFile Initializer.conf'
        2. Enter the Public IP address of the WebService
        3. Enter the SAIL login credentials
        4. Enter the Azure Credentials
        5. Process to create Virtual Machines

Note: Creating Virtual Machines may sometimes take a long time. Typically it would take 30seconds to a minute. But there have been instances when this has taken more than 3-4 minutes.


# SAIL Deployment Domain Tools

## Packaging WebServices and Compute Binaries
Package WebServices and Compute Binaries to be uploaded and installed on the Virtual Machine.

### WebServices Virtual Machine Files
    DatabaseGateway
    RestApiPortal
    SharedLibraries/DatabasePortal/libDatabaseManager.so
    SharedLibraries/RestApiPortal/libAccountDatabase.so
    SharedLibraries/RestApiPortal/libCryptographicKeyManagement.so
    SharedLibraries/RestApiPortal/libDigitalContractDatabase.so
    SharedLibraries/RestApiPortal/libVirtualMachineManager.so
    SharedLibraries/RestApiPortal/libAuditLogManager.so
    SharedLibraries/RestApiPortal/libDatasetDatabase.so
    SharedLibraries/RestApiPortal/libSailAuthentication.so

### Compute Virtual Machine Files
    RootOfTrustProcess
    InitializerProcess
    SignalTerminationProcess
    DataDomainProcess
    ComputationalDomainProcess
    libDataConnector.so

### Run the tool
    $ ./PackageWebServiceAndComputeVm
will create two packages:

    SecureComputationalVirtualMachine.binaries
    WebServicesPortal.binaries

## Deploy Web Services
Deploy WebService is a tool that can be used to create Virtual Machines that host the Rest API Portal and the database.
This can be simply done and all ones needs are the Azure credentials:
    - Application ID
    - Password/Secret
    - Tenant Id
Along with this the packages WebService binaries is also needed i.e. WebServicesPortal.binaries

Execute by:

    $ ./DeployWebServices

## DatabaseTools
This is an internal tool can is used to populate an existing databse hosted on a Virtual Machine running WebServices. The tool will add some users and relevant test data for demo and testing puposes.
All it needs is the Public IP Address of the WebServices Virtual Machine and the port number on wwhich the Rest Portal is accepting requests which is 6200 in out case.

Execute this by:

    $ ./DatabaseTools

# Data Research Domain Tools

## Researcher Interface
    <TODO>

## Audit Tool
    <TODO>
