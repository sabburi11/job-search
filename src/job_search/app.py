import gradio as gr
from main import run_job_search
from gradio_pdf import PDF
from pypdf import PdfReader
def greet(name, intensity):
    resume_thing = ""
    reader = PdfReader(intensity)
    for page in reader.pages:
        resume_thing+=page.extract_text()
    
    return f"Hello {name}. This is the thing: {resume_thing}"

def running_job_search(query, resume_pdf):
    reader = PdfReader(resume_pdf)
    resume_text = ""
    for page in reader.pages:
        resume_text += page.extract_text()
    result = run_job_search(query, resume_text)
    return result.raw

demo = gr.Interface(
    fn=running_job_search,
    inputs=[gr.Textbox(label="Job you are searching for"), gr.File(label="Resume")],
    outputs=[gr.Textbox(label="Report on avaliable jobs")],

)

demo.launch()