Title/Description:
    
    This is Assignment#1 of week#2 at FlyRank Ai internship. In this, we had created app having a CRUD operation with MockData without connection of database.

Tech stack:	
    
    Python, FastAPI, SQLAlchemy, 

Setup / installation	
    
                    Clone 
                    create venv
                    pip install -r requirements.txt
                    set up .env

How to run:

    Run this in your main.py terminal:

                    python dev main.py --reload



Endpoint table:

        CRUD operation        HTTP Method         Example Method        Meaning
        
        Create                POST                /addProduct           Create new task
        Read                  GET                 /all_Products         Show all task 
        Update                PUT                 /updateProduct/1      Update any task by id  
        Delete                DEL                 /deleteProduct/1      Delete any task by id  


	
Example request/response

This file also works the proof is:
                    
                    http://127.0.0.1:8000/addProduct    
            After running your applilcation run this in your browser