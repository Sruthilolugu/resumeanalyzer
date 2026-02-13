from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

from resume_parser import extract_text_from_pdf
from llm_service import analyze_resume

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze")
async def analyze(request: Request,
                  resume: UploadFile = File(...),
                  job_description: str = Form(...)):
    
    resume_text = extract_text_from_pdf(resume.file)
    result = analyze_resume(resume_text, job_description)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result
    })
