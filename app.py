from flask import Flask, request
from app_service import AppService
import json
import os

# -------------------------------------------------
# 🔥 Load AWS AppConfig from shared volume
# -------------------------------------------------
CONFIG_PATH = "/config/aws-appconfig.json"

def load_appconfig():
    try:
        with open(CONFIG_PATH) as f:
            data = json.load(f)
            for k, v in data.items():
                os.environ[k] = str(v)
        print("Loaded AWS AppConfig successfully.")
        print("Config values:", data)
    except Exception as e:
        print("AWS AppConfig not loaded:", e)

# Load AWS AppConfig BEFORE Flask starts
load_appconfig()
# -------------------------------------------------

app = Flask(__name__)
appService = AppService()

@app.route('/')
def home():
    return "App Works!!"

@app.route('/env')
def env():
    """Endpoint to verify AWS AppConfig values"""
    return {
        "MY_ENV_VAR": os.getenv("MY_ENV_VAR")
    }

@app.route('/api/tasks')
def tasks():
    return appService.get_tasks()

@app.route('/api/task', methods=['POST'])
def create_task():
    request_data = request.get_json()
    task = request_data['task']
    return appService.create_task(task)

@app.route('/api/task', methods=['PUT'])
def update_task():
    request_data = request.get_json()
    return appService.update_task(request_data['task'])

@app.route('/api/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    return appService.delete_task(id)
