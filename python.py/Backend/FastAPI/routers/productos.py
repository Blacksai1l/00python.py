from fastapi import APIRouter

router = APIRouter(prefix="/productos", 
                   responses= { 404 : {"message" : "No encontrado" }},
                   tags= ["productos"]) # agrupa en la documentacion

# para llamar al server --> uvicorn productos:app --reload

listadeproductos = ["producto 1" ,"producto 2" ,"producto 3" ,"producto 4" ,"producto 5" ]

@router.get("/")
async def productos ():
    return listadeproductos 

@router.get("/{id}")
async def productos (id:int):
    return listadeproductos[id-1] 


