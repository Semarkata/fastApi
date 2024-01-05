from fastapi import FastAPI

app = FastAPI(
    title='Fast Api',
    description='My Fast Api project',
    version='0.0.1',
)

@app.get('/', tags=['Root'])

def read_root():
    return {"Hello": "World"}