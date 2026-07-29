from flask import Flask, request, jsonify
from app_service import AppService

app = Flask(__name__)

appService = AppService()


@app.route("/")
def home():

    return "App Works!!!"


@app.route("/api/health")
def health():

    return jsonify(
        {
            "status": "App Works"
        }
    ), 200


@app.route("/api/tasks", methods=["GET"])
def tasks():

    return jsonify(
        appService.get_tasks()
    ), 200


@app.route("/api/task", methods=["POST"])
def create_task():

    request_data = request.get_json()

    task = request_data.get("task")

    if not task:
        return jsonify(
            {
                "error": "task is required"
            }
        ), 400


    return jsonify(
        appService.create_task(task)
    ), 201



@app.route("/api/task", methods=["PUT"])
def update_task():

    request_data = request.get_json()

    task = request_data.get("task")

    if not task:
        return jsonify(
            {
                "error": "task is required"
            }
        ), 400


    return jsonify(
        appService.update_task(task)
    ), 200



@app.route("/api/task/<int:id>", methods=["DELETE"])
def delete_task(id):

    return jsonify(
        appService.delete_task(id)
    ), 200



if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
