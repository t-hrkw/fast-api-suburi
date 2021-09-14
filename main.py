from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
  return {'data': 'blog list'}

# これを@app.get('/blog/{id}')より先に書かないといけない
@app.get('/blog/unpublished')
def unpublished():
  return {'data': {'all unpublished blogs'}}

@app.get('/blog/{id}')
def show(id: int):
  return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int):
  return {'data': {'1', '2'}}
