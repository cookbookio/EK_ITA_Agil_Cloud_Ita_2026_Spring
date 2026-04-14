# IaC - Infrastructure as Code

## Learning Goals

* Have knowlage about different IaC tools.
* Setup a version-controlled infrastructure, for faster path to recovery.

## Before Class

* [What is Infrastructure as Code?](https://www.youtube.com/watch?v=zWw2wuiKd5o) (8:50)

## Todays Teachings
We start out by having a look at your projects and determain what you each will do if your VM is destroyed at Azure.
 
Then we look at the **infrastructure code** in the Awsome recipe cookbook project:

* [Awsome recipe cookbook - **IaC**](https://github.com/cookbookio/awsome_recipe_cookbook/tree/IaC/infrastructure)

You should:
* Fork this repo - remember to include all branches in your fork.
* clone it to your local machine, and checkout the IaC branch.
* cd into the infrastructure folder, and `./azure-setup.sh` 

This should create a resource group with 2 vm´s and setup the secrets on github.      
You might need to change the location in the azure-setup.sh so it fits to your account settings.

Then push the code to github and watch the action run.     
You will need to create a `CR_PAT` in the secrets.    
You will need to make your packages (docker images) public.    
Run the actions again, and it should be deployed on Azure. 

* run the `azure-teardown.sh` script.

This exercise should be done several times until you are secure in the process.

## After Class

* [IaC in your own project](03._cookbook_iac.md)
