import typer
from typing import List, Optional
import questionary
import subprocess
app = typer.Typer()

@app.command()
def hello(name: str, age: int):
    print(f"Hello {name}! You are {age} years old.")

@app.command()
def rayzer():
    """Interactive Ray cluster and job management."""
    
    choice = questionary.select(
        "What would you like to do?",
        choices=[
            "Launch a new job",
            "Launch a new service",
            "Launch a Ray Cluster",
            "Exit"
        ]
    ).ask()

    if choice == "Create a new job":
        job_type = questionary.select(
            "What type of job would you like to create?",
            choices=[
                "init Ray Job",
                "Example: Train a xgboost model",
                "Example: Train a pytorch model",
            ]
        ).ask()

        if job_type == "init Ray Job":
            print("Initializing Ray Job...")
        elif job_type == "Example: Train a xgboost model":
            print("Training a xgboost model...")
        elif job_type == "Example: Train a pytorch model":
            print("Training a pytorch model...")

    elif choice == "Create a new service":
        service_type = questionary.select(  
            "What type of service would you like to create?",
            choices=[
                "Example: Train a xgboost model",
                "Example: Train a pytorch model",
            ]
        ).ask()
        if service_type == "Example: Train a xgboost model":
            print("Training a xgboost model...")
        elif service_type == "Example: Train a pytorch model":
            print("Training a pytorch model...")

    elif choice == "Setup a Ray Cluster":
        cluster_type = questionary.select(
            "How would you like to set up your Ray Cluster?",
            choices=[
                "Deploy a Ray Cluster locally",
                "Deploy a Ray Cluster on AWS",
                "Deploy a managed Ray Cluster on Anyscale"
            ]
        ).ask()
        
        if cluster_type == "Deploy a Ray Cluster locally":
            print(f"Setting up local autoscaling Ray Cluster...")
            print(f"This will take a few minutes and open a few browser windows.")
            
            subprocess.run(["bash", "ray_infra_local.sh"], check=True)
            print("Local Ray cluster launched successfully!")
            
        elif cluster_type == "Deploy a Ray Cluster on AWS":
            print(f"Setting up Ray cluster on AWS...")
            print(f"This will take a few minutes and open a few browser windows.")
            subprocess.run(["bash", "ray_infra_aws.sh"], check=True)
            print("Ray cluster on AWS launched successfully!")


        elif cluster_type == "Deploy a managed Ray Cluster on Anyscale":
            print(f"Setting up Ray cluster on Anyscale...")
            print(f"This will take a few minutes and open a few browser windows.")
            subprocess.run(["bash", "ray_infra_anyscale.sh"], check=True)
            print("Ray cluster on Anyscale launched successfully!")

    
    elif choice == "Exit":
        print("Exiting Rayzer CLI. Goodbye!")
        return

if __name__ == "__main__":
    app()
