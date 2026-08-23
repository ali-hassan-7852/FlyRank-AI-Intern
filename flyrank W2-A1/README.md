Title/Description:
    
    This is Assignment#1 of week#3 at FlyRank Ai internship. In this, we had created app having a CRUD operation that connected with Database. 

Tech stack:	
    
    Python, FastAPI, PostgreSQL, SQLAlchemy, pydantic

Setup / installation	
    
                    Clone 
                    create venv
                    pip install -r requirements.txt
                    set up .env

How to run:

    Run this in your main.py terminal:

                    python dev main.py --reload

Environment variables List:


    Create a `.env` file in the project root and add:

                    DB_CONNECTION="postgresql://postgres:your_password@localhost:5432/postgres"


Endpoint table:

        CRUD operation        HTTP Method         Example Method        Meaning
        
        Create                GET                /create_task           Create new task
        Read                  POST               /all_task              Show all task 
        Update                PUT                /update_task/1         Update any task by id  
        Delete                DEL                /delete_task/1         Delete any task by id  


	
Example request/response

This file also works the proof is:
                    
                    http://127.0.0.1:8000/tasks/create     
            After running your applilcation run this in your browser
	

