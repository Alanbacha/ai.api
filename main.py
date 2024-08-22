from fastapi import FastAPI

from controllers.api.openaiController import router as api_openai_router
from controllers.api.azureaiController import router as api_azureai_router

app = FastAPI()

app.include_router(api_openai_router)
app.include_router(api_azureai_router)

if __name__ == '__main__':
	import uvicorn
	uvicorn.run(app, host='127.0.0.1', port=8001)
