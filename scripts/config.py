class Field:
    ABOUT = "About"
    PROFESSIONAL_SUMMARY = "Professional Summary"
    LINKED_IN = "LinkedIn"
    GIT_HUB = "GitHub"
    PROGRAMMING_LANGUAGES = "Programming Languages"
    DL_MODELS = "DL Models"
    FRAMEWORKS = "Frameworks"
    CLOUD_STACK = "Cloud Stack"
    DB_KNOWLEDGE = "Database Knowledge"
    LANGUAGES = "Languages"
    CONFIG_MANAGEMENT = "Configuration Management"

    START = "Start"
    END = "End"
    UNIVERSITY = "University"
    COURSE = "Course"
    SPECIALIZATION = "Specialization"
    PROJECT_TITLE = "Project Title"

    ROLE = "role"
    COMPANY_NAME = "company_name"
    PLACE = "place"
    DESCRIPTION = "description"
    TECH_STACK = "tech_stack"

class Parameter:
    role = "Machine Learning Engineer"
    greet = "Hi, I am Vivek Loganathan :wave:"
    "I am passionate about using data in any form "
    address = """
                Ernst Lehmann-strasse 17, \n
                Magdeburg 39106, \n
                Saxony Anhalt, \n
                Germany \n
                +49 17685983957 \n
                vivek87799@gmail.com \n
                """
    about_me = "I am passionate about Artificial Intelligence, Computer Vision, "
    work_experience = """
                        With 3 years of experience in the field of Software Development and 2+ years of experience as a Computer Vision/ Machine Learning Engineer 
                        I could finally build a black and white web page. I have created this web page using streamlit for easy access to the projects that I have worked on
                        and also summarizes my skills and work experience.
                        """
    skills = {
        Field.PROGRAMMING_LANGUAGES: """
                            c++ (17, 20), \n
                            Advanced Python, Java, \n
                            NodeJs, ABAP \n
                            """,
    Field.DL_MODELS:        """
                            YOLO, Mast R-CNN, \n
                            OpenPose, ResNet, \n
                            Transforemers, BERT, \n
                            Vision Transforerms \n
                            """,
    Field.FRAMEWORKS:       """
                            Numpy, Pandas, Scikit-Learn \n
                            PyTorch, OpenVino, MatplotLib, \n 
                            Kafka, Faust, Spark, Flink \n
                            MLFlow, SageMaker, \n
                            FastAPI, Flask, Streamlit,  \n
                            Scrum
                            """,
    
    Field.CONFIG_MANAGEMENT:"""
                            GitHub, CMake \n
                            Docker, Kubernetes \n
                            """,
    
    Field.CLOUD_STACK:      """
                            AWS, GCP \n
                            """,
    
    Field.DB_KNOWLEDGE:     """
                            SQL, NoSQL, \n
                            Elasticsearch, mongoDB \n
                            """,

    Field.LANGUAGES:        """
                            Tamil, English (C2) \n
                            German (A2) \n
                            """
    }

    education = [{
        Field.START: "2016 Oct", 
        Field.END: "2021 May",
        Field.UNIVERSITY: "OVGU",
        Field.COURSE: "M.Sc. in Digital Engineering",
        Field.SPECIALIZATION: "Advanced Machine Learning, Deep Learning, Computer Vision", 
        Field.PLACE: "Magdeburg, Germany"
    },
    {
        Field.START: "2008 June",
        Field.END: "2012 May",
        Field.UNIVERSITY: "VIT",
        Field.COURSE: "B.Tech. in Electronics and Communicaion Engineering",
        Field.SPECIALIZATION: "Specialization in Computer Vision",
        Field.PLACE: "Vellore, India"
    }
    ]

    work_history = [{
        Field.START: "2021 Oct",
        Field.END: "2022 Feb",
        Field.COMPANY_NAME: "Nullfinders",
        Field.ROLE: "Machine Learning Engineer",
        Field.PLACE: "Magdeburg, Germany",
        Field.DESCRIPTION: """
                           - Design and build a real-time machine learning life cycle landscape for NLP task.
                           - Architectured and implemented data preprocessing pipeline (stream processing) for big data, module to train, validate and deploy the model for inference, also built a asynchronous web server with load balancer for inference.
                           - Modules were contanarized for easy scaling and future enhancements. 
                           """,
        Field.TECH_STACK: "Python 3.8, Kafka, Faust, MLFlow, PyTorch, Elasticsearch, FastAPI"
    },
    {
        Field.START: "2018 Dec",
        Field.END: "2021 Jan",
        Field.COMPANY_NAME: "MetraTec GmbH",
        Field.ROLE: "Computer Vision/ Machine Learning Engineer",
        Field.PLACE: "Magdeburg, Germany",
        Field.DESCRIPTION: """
                           - Worked on Virtual Reality interaction and Visualization project.
                           - The task was to build a real-time motion capture system using the SOTA Deep Learning solutions.
                           - Migrated existing classical Computer Vision detection module to use Deep Learning which increased the performance.
                           - Successfully prototyped and deployed a Deep Learning model on an edge device using OpenVINO framework, we were able to achieve real time performance without the need of a GPU.
                           """,
        Field.TECH_STACK:"Python 3.6, c++, OpenVINO, PyTorch, TensorBoard"
    },{
        Field.START: "2018 Jan",
        Field.END: "2018 Aug",
        Field.COMPANY_NAME: "Komelo GmbH",
        Field.ROLE: "Backend Developer",
        Field.PLACE: "Magdeburg, Germany",
        Field.DESCRIPTION: """
                           - Worked on a School Management System as a backedend developer. 
                           - Architectured and developed a backend API in an Agile env.
                           - Appreciated by the CEO for the successful integration and deployment of the application.
                           """,
        Field.TECH_STACK:"NodeJS, Docker, MongoDB"
    },{
        Field.START: "2012 May",
        Field.END: "2015 May",
        Field.COMPANY_NAME: "Cognizant",
        Field.ROLE: "Data Analyst",
        Field.PLACE: "Bangalore, India",
        Field.DESCRIPTION: """
                           - Worked on SAP BI to process data from multiple sources and extract valuable insights on the data for the report
                           - Successfully Worked on automation of process chains that reduced several manual hours which was appreciated by the client.
                           - 
                           """,
        Field.TECH_STACK:"AP BI, ABAP, AdvancedJAVA"
    }]

    academic_projects = [{
        Field.START: "2017 April",
        Field.END: "2018 July",
        Field.PROJECT_TITLE: "Detection of APS failures in trucks",
        Field.UNIVERSITY: "OVGU, Magdeburg, Germany",
        Field.DESCRIPTION: """
                           - Used Random Forest, SVM and Naive Bayes to predict the failures in the truck.
                           - We obtained an outstanding score which was in the top five scores of the competition.
                           """,
        Field.TECH_STACK: "Python 3.6, Pandas, NumPy"
    },{
        Field.START: "2017 May",
        Field.END: "2018 Feb",
        Field.PROJECT_TITLE: "Swarm Behaviour in Multi Quadcopters",
        Field.UNIVERSITY: "OVGU, Magdeburg, Germany",
        Field.DESCRIPTION: """
                           - Implemented swarm behaviour in Quadcopters that adopts to environment and spatial distribution.
                           - Used classical Computer Vision and SONARS for localization and ROS for visualization.
                           """,
        Field.TECH_STACK: "Python 3.6, c++ 17, ROS"
    },{
        Field.START: "2018 Aug",
        Field.END: "2019 April",
        Field.PROJECT_TITLE: "Adaptive Camera Tracking for Robots",
        Field.UNIVERSITY: "OVGU, Magdeburg, Germany",
        Field.DESCRIPTION: """
                           - Trained CNN to detect and classify robots in the arena.
                           - The obtained information was published on the ROS ecosystem which was then used for navigation of the robots in the arena.
                           - Successfully integrated Artificial Intelligence into Swarm Behaviour in multiple Quadcopters.
                           """,
        Field.TECH_STACK: "Python 3.6, c++ 17, ROS, PyTorch"
    }]
    
    thesis = [{
        Field.START: "2020 Aug",
        Field.END: "2021 May",
        Field.PROJECT_TITLE: "3D Skeleton-Based Gesture and Action Recognition in Multi-Person Scenarios",
        Field.UNIVERSITY: "OVGU, Magdeburg, Germany",
        Field.DESCRIPTION: """
                            We implemented a two-stage framework:
                            - The first stage for multi-person 3D pose estimation to get the skeleton joints of the human from multiple calibrated cameras, used Convolutional Neural Network human pose estimator.
                            - The second stage uses the ensemble of Graph Convolutional Networks to recognise the action of the human using the human skeleton graph obtained from the first stage.
                            - We obtained a remarkable 40 percent fewer FLOPS than the existing approaches only with a trifling reduction in the accuracy.
                            - As part of the thesis, we have created an action recognition dataset to quantitatively and qualitatively evaluate our approach.
                            """,
        Field.TECH_STACK: "Python 3.6, C++17, OpenCV, PyTorch"
    }]