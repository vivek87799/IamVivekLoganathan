from distutils.log import error
import logging
from typing import Dict
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from config import Field, Parameter

# logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler("main_page.log", mode="w")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def add_education(edu: Dict[str, str], content: DeltaGenerator) -> None:
    
    with content:
        # st.write("---")
        st.write(f"{edu[Field.START]} - {edu[Field.END]}")
        
    with content:
        st.markdown(f"**{edu[Field.COURSE]}** , *{edu[Field.PLACE]}*")
        st.write(edu[Field.SPECIALIZATION])
        st.write("---")
    
def add_work_exp(work_exp: Dict[str, str], content: DeltaGenerator) -> None:
    with content:
        st.write(f"{work_exp[Field.START]} - {work_exp[Field.END]}")        
        st.markdown(f"**{work_exp[Field.COMPANY_NAME]}** , {work_exp[Field.ROLE]}, *{work_exp[Field.PLACE]}*")
        st.write(work_exp[Field.DESCRIPTION])
        st.write(f"{'Tech-Stack: '} {work_exp[Field.TECH_STACK]}")
        st.write("---")

def add_thesis(thesis: Dict[str, str], content: DeltaGenerator) -> None:
    with content:
        st.write(f"{thesis[Field.START]} - {thesis[Field.END]}")        
        st.markdown(f"**{thesis[Field.PROJECT_TITLE]}** , {thesis[Field.UNIVERSITY]}")
        st.write(thesis[Field.DESCRIPTION])
        st.write(f"{'Tech-Stack: '} {thesis[Field.TECH_STACK]}")
        st.write("---")

def add_academic_project(project: Dict[str, str], content: DeltaGenerator) -> None:
    with content:
        st.write(f"{project[Field.START]} - {project[Field.END]}")        
        st.markdown(f"**{project[Field.PROJECT_TITLE]}** , {project[Field.UNIVERSITY]}")
        st.write(project[Field.DESCRIPTION])
        st.write(f"{'Tech-Stack: '} {project[Field.TECH_STACK]}")
        st.write("---")

def add_header() -> None:
    try:        
        st.set_page_config(page_title="I am Vivek Loganathan", page_icon=":tada:", layout="wide")  
        # ----HEADER-----#
        with st.container():
            st.subheader(Parameter.greet)
            st.title(Parameter.role)
            st.sidebar.subheader(Field.ABOUT)
            st.sidebar.write(Parameter.address)
            st.sidebar.write(f"[{Field.LINKED_IN} >](https://www.linkedin.com/in/vivek-loganathan-8515873b/)")
            st.sidebar.write("""[![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/vivek87799)""")
            # st.sidebar.write(f"[{Field.GIT_HUB} >](https://github.com/vivek87799)")
            professional_summary, border = st.columns((4,1))
            with professional_summary:
                st.subheader(Field.PROFESSIONAL_SUMMARY)
                st.write(Parameter.work_experience)
            

    except Exception as error:
            logger.exception(error)
            logger.error(error)

def add_sidebar() -> None:
    # Adding skills
    try:
        with st.container():
            logger.info(f"Adding skills")
            for title, skill in Parameter.skills.items():
                st.sidebar.subheader(f'{title}')
                st.sidebar.write(skill)
    except Exception as error:
        logger.exception(error)
    
def add_body() -> None:
    try:
        with st.container():
            logger.info(f"Adding body")
            content, border = st.columns([4,1])
            logger.info(f"Adding Education")
            with content:
                # st.write("---")
                st.subheader("Education")
            for edu in Parameter.education:
                add_education(edu, content)


            logger.info("Adding Work Experience")            
            with content:
                # st.write("---")
                st.subheader("Work Experience")
            for work_exp in Parameter.work_history:
                add_work_exp(work_exp, content)

            logger.info("Adding thesis information")
            with content:
                st.subheader("Master Thesis")
            for thesis in Parameter.thesis:
                add_thesis(thesis, content)

            logger.info("Adding academic projects")
            with content:
                st.subheader("Academic Projects")
            for project in Parameter.academic_projects:
                add_academic_project(project, content)
    except Exception as error:
        logger.exception(error)


if __name__ == "__main__":
    logger.info("Creating the web page")
    add_header()
    add_sidebar()
    add_body()