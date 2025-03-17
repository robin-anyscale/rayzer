import typer
from typing import List, Optional
import questionary
import subprocess
import atexit
import time
import sys

app = typer.Typer()

@app.command()
def hello(name: str, age: int):
    print(f"Hello {name}! You are {age} years old.")

@app.command()
def rayzer(
    # default_option: Optional[str] = typer.Option(
    #     None, 
    #     "--option", 
    #     "-o", 
    #     help="Specify a default option to run without interactive prompts"
    # )
):
    """Interactive Ray cluster and job management."""
    print("\033[1m" + """
██████╗  █████╗ ██╗   ██╗███████╗███████╗██████╗ 
██╔══██╗██╔══██╗╚██╗ ██╔╝╚══███╔╝██╔════╝██╔══██╗
██████╔╝███████║ ╚████╔╝   ███╔╝ █████╗  ██████╔╝
██╔══██╗██╔══██║  ╚██╔╝   ███╔╝  ██╔══╝  ██╔══██╗
██║  ██║██║  ██║   ██║   ███████╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝
""" + "\033[0m")

    # handle_option("ColdStart")
        

    # Otherwise, show the interactive menu
    choice = questionary.select(
        "Welcome to Rayzer! Fastest way to get started with Ray.",
        choices=[
            "Launch a new job",
            "Launch a new service",
            "Launch a Ray Cluster",
            "ColdStart",
            "Exit"
        ]
    ).ask()

    handle_option(choice)

def handle_option(choice: str):
    """Handle the selected option."""
    if choice == "Launch a new job":
        
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

    elif choice == "Launch a new service":
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

    elif choice == "Launch a Ray Cluster":
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
            
            proc = subprocess.Popen(["bash", "ray_infra_local.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            atexit.register(lambda p: p.kill(), proc)  # Kill subprocess when Python exits
        
            # time.sleep(5)
            # Create a loading spinner animation
            def spinner(time_to_run=5):
                chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
                start_time = time.time()
                while time.time() - start_time < time_to_run:
                    for char in chars:
                        sys.stdout.write('\r' + 'Setting up cluster ' + char)
                        sys.stdout.flush()
                        time.sleep(0.1)
                sys.stdout.write('\r' + ' ' * 20 + '\r')  # Clear the line
                sys.stdout.flush()
            
            spinner()  # Run the spinner for 5 seconds
            print("Local Ray cluster launched successfully!")
            # Return to the main menu
            return app()
            
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

    elif choice == "ColdStart":
        print(f"Running ColdStart...")
        proc = subprocess.Popen(["bash", "ray_infra_local.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        atexit.register(lambda p: p.kill(), proc)  # Kill subprocess when Python exits
        # return app()

    elif choice == "Exit":
        print("Exiting Rayzer CLI. Goodbye!")
        return

if __name__ == "__main__":
    app()
