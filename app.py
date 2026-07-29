from flask import Flask, request, jsonify
from app_service import AppService

app = Flask(__name__)

appService = AppService()


@app.route("/")
def home():

    return "App Works!!!"


@app.route("/mobile")
def mobile():

    return """
    <!DOCTYPE html>
    <html>

    <head>

        <title>ECS Mobile Task App</title>

        <meta name="viewport"
              content="width=device-width, initial-scale=1">

        <style>

            body {
                font-family: Arial, sans-serif;
                padding: 20px;
                background: #f5f5f5;
            }

            h1 {
                color: #333;
            }

            button {

                width: 100%;
                padding: 15px;
                margin: 10px 0;
                font-size: 18px;
                background: #007bff;
                color: white;
                border: none;
                border-radius: 5px;

            }


            .task {

                background: white;
                padding: 15px;
                margin: 10px 0;
                border-radius: 5px;

            }

        </style>


    </head>


    <body>


        <h1>
            ECS Task Mobile App
        </h1>


        <button
            id="loadTasks"
            onclick="loadTasks()">

            Load Tasks

        </button>


        <div id="tasks"></div>



        <script>


        function loadTasks(){


            fetch('/api/tasks')


            .then(response => response.json())


            .then(data => {


                let output = "";


                data.forEach(task => {


                    output += `

                    <div class="task">

                        <h3>
                            ${task.name}
                        </h3>


                        <p>
                            ${task.description}
                        </p>


                    </div>

                    `;


                });


                document.getElementById(
                    "tasks"
                ).innerHTML = output;


            });


        }


        </script>


    </body>


    </html>
    """


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
