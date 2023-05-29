#!/bin/bash

set -e

# Check if .env file exists
if [ ! -f ../.env ]; then
  echo "Error: .env file not found"
  exit 1
fi

# Load environment variables
source ../.env

# Check if ENVIRONMENT env variable is present
if [[ -z "${ENVIRONMENT-}" ]]; then
  echo "Error: ENVIRONMENT env variable is not found."
  exit 1
fi

PACKAGE_NAME="poetry"

# Checking the type of environment
if command -v "$PACKAGE_NAME" >/dev/null 2>&1; then     # check if Poetry is installed
  PYP=poetry

elif [[ -d venv ]]; then    # check if venv is present
  PYP=venv

elif [[ -n "$DOCKER_CONTAINER_ID" ]]; then    # check if running in docker container
  PYP=docker

else
  echo "Error: Neither poetry or venv nor docker environ is found."
  exit 1
fi

# activate environment
if [[ $ENVIRONMENT == "local" && $PYP == "poetry" ]]; then
  echo "Project running in your local pc and you are using poetry to manage your virtual environment."
  echo "Checking If Any Migration Need To Apply..."

  # poetry update

  poetry run python manage.py makemigrations common files errors api product
  poetry run python manage.py migrate

elif [[ $ENVIRONMENT == "local" && $PYP == "venv" ]]; then
  echo "Project running in your local pc and you are using venv to manage your virtual environment."
  source venv/bin/activate
  echo "Checking If Any Migration Need To Apply..."

  # pip install --upgrade pip setuptools
  # echo "Uninstalling Some Orphane packages.."
  # pip freeze > uninstall.txt
  # # Uninstall each package
  # while read -r package; do
  #     pip uninstall --yes "$package" >/dev/null 2>&1 || true
  # done < uninstall.txt
  # echo "Uninstalling Done.."
  # # pip uninstall --yes -r uninstall.txt > /dev/null 2>&1
  # pip install -r requirements.txt

  python manage.py makemigrations product 
  python manage.py migrate
  deactivate

elif [ $ENVIRONMENT == "development" ]; then
  echo "*** Development Server ***"
  # pip install --upgrade pip setuptools
  source venv/bin/activate

  # pip install --upgrade pip setuptools
  # echo "Uninstalling Some Orphane packages.."
  # pip freeze > uninstall.txt
  # # Uninstall each package
  # while read -r package; do
  #     pip uninstall --yes "$package" >/dev/null 2>&1 || true
  # done < uninstall.txt
  # echo "Uninstalling Done.."
  # pip install -r requirements.txt

  echo "Checking If Any Migration Need To Apply..."
  python manage.py makemigrations product inventory user_api ambulance career Contribution dashboard DeliveryTeam Doctor_appointment Doctor_Career header_content live_doctor notification Online_Doctor_Booking pathology Patient payment physio_care pos slider_image upload_prescription_api vendor_order Wishlist warehouse pharmacist careboxQuiz
  python manage.py migrate
  deactivate

fi

if [ "$ENVIRONMENT" == "production" ]; then
  echo "*** Production Server ***"
  source venv/bin/activate

  # pip install --upgrade pip setuptools
  # echo "Uninstalling Some Orphane packages.."
  # pip freeze > uninstall.txt
  # # Uninstall each package
  # while read -r package; do
  #     pip uninstall --yes "$package" >/dev/null 2>&1 || true
  # done < uninstall.txt
  # echo "Uninstalling Done.."
  # pip install -r requirements.txt

  echo "Checking If Any Migration Need To Apply..."
  python manage.py makemigrations product inventory user_api ambulance career Contribution dashboard DeliveryTeam Doctor_appointment Doctor_Career header_content live_doctor notification Online_Doctor_Booking pathology Patient payment physio_care pos slider_image upload_prescription_api vendor_order Wishlist warehouse pharmacist careboxQuiz
  python manage.py migrate
  deactivate
fi

