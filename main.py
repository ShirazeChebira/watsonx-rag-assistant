from dotenv import load_dotenv
load_dotenv()

from ui.gradio_app import launch_app

if __name__ == "__main__":
    launch_app()