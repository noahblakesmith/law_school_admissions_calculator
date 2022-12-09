# My Freestyle Project

## About

This app predicts the user's probability of being admitted to a law school based on the information provided.

The app uses a logit model that was cross-validated using self-reported admissions data from LSD.law.

## Setup

Create and activate a virtual environment:

```sh
conda create -n freestyle_project_env python

conda activate freestyle_project_env
```

Install package dependencies:

```sh
Navigate to the directory where files are located.

pip install -r requirements.txt
```

## Usage

Run the web app locally:

```sh
python routes.py
```

Then go to the indicated URL followed by /input, e.g.,

```sh
http://127.0.0.1:5000/input
```

## Testing

```sh

```