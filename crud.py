#basic crud operation without db


from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
app=FastAPI(title="project1")
my_db=[]
class boys(BaseModel):
    roll_no:int
    name:str
    mark:int

#post method --- create
@app.post("/boys/")
def create_boys(p:boys):
    my_db.append(p.model_dump())
    return{"status":"success","data":p}

#get method --- read 
@app.get("/boys/")
def read_boys():
    return{"status":"success","data":my_db}
#get method --- read using parameters
@app.get("/boys/{roll_no}")
def read(roll_no:int):
    for b in my_db:
        if b["roll_no"]==roll_no:
            return{"data":b}

#put method --- update
@app.put("/boys/update")
def update(roll_no:int,p:boys):
    for b in my_db:
        if b["roll_no"]==roll_no:
            b["name"]=p.name
            b["mark"]=p.mark
            return{"status":"updated","updated_data":b}
    raise HTTPException(status_code=404,detail="not found")

#delete method --- delete
@app.delete("/boys/delete")
def delete(roll_no:int):
    for b in my_db:
        if b["roll_no"]==roll_no:
            my_db.remove(b)
            return{"status":"deleted"}
    raise HTTPException(status_code=404,detail="no records to delete")