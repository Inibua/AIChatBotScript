import subprocess
import os
import venv


def create_virtualenv(venv_dir="venv"):
    if os.path.exists(venv_dir):
        print(f"Virtual environment '{venv_dir}' already exists. Skipping creation.")
        return
    print("Creating virtual environment...")
    venv.create(venv_dir, with_pip=True)


def install_requirements(venv_dir="venv"):
    if os.name == 'nt':
        activate_script = os.path.join(venv_dir, 'Scripts', 'python.exe')
    else:
        activate_script = os.path.join(venv_dir, 'bin', 'python')

    print("Upgrading pip...")
    subprocess.check_call([activate_script, '-m', 'pip', 'install', '--upgrade', 'pip'])

    print("Installing requirements from requirements.txt...")
    subprocess.check_call([activate_script, '-m', 'pip', 'install', '-r', 'requirements.txt'])


def main():
    venv_name = "venv"
    venv_dir = f"../{venv_name}"
    create_virtualenv(venv_dir)
    install_requirements(venv_dir)
    print("Virtual environment set up and dependencies installed.")


if __name__ == "__main__":
    main()
