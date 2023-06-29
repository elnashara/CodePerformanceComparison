# Copyright Jules White, 2023

from sparc.ai_coder import generate_python_module

root_prompt = """
        Your functionality must be implemented in Python as a class with a method called
        handle that accepts a FastAPI request and a function called router() that returns
        the router for the functionality. 
        The class must have mount and unmount methods that are called when the functionality
        is mounted and unmounted. These methods will be passed a FastAPI app object so
        that the methods can add and remove routes from the app.
        
        The format of a feature that adds routes to a FastAPI app is this:
        
        ```Python
        
        class SomeFeature:
          def __init__(self):
            self.app = app
        
          def mount(self, app):
            # logic to create needed routes in the FastAPI app and anything
            # else that is needed to implement the feature goes here
        
          def unmount(self, app):
            # logic to remove routes from the FastAPI app
            # and anything else that is needed to undo the feature
            # changes to the app goes here
        
          # Helper methods go down here
        
        # You MUST MUST have a global instance of the class named instance
        instance = SomeFeature()
        
    ```
"""

feature_description = "A feature to store information about cars and their owners. The feature should allow me to send json that includes car make, model, year, mileage, color, and other relevant information and then information about each cars's ownership history"

# feature_description = input("What feature would you like to add to the app? ")

desired_feature = f"""
        Create python code for the following feature: {feature_description}
        """

def exec_check(feature_module):
    print("Checking if the module has the correct interface...")
    if not feature_module.instance:
        raise Exception("You must have a global variable named instance")


generated_module = generate_python_module(
    "feature_module",
    [root_prompt],
    [desired_feature],
    module_checkfn=exec_check,
    max_tries=10
)

print(f"Compiling code with instance variable: \n\n{generated_module.code}\n\n")
input("Press enter to continue")

from fastapi import FastAPI
app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("Starting up")

@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down")

generated_module.module.instance.mount(app)

import uvicorn
# start the server as a background task
uvicorn.run(app, host="localhost", port=8000)
