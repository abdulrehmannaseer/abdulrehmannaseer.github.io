---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Motivated Data Scientist, AI researcher, and Lab Instructor at GIFT University specializing in computer vision, multimodal learning, anomaly detection, and retrieval-augmented generation (RAG). Co-author of research accepted in leading venues including IEEE TPAMI, ECCV, IEEE Sensors Journal, and DICTA. Experienced in developing PyTorch-based research systems and end-to-end AI applications involving website crawling, hybrid information retrieval, grounded question answering, and interactive user interfaces.

My research interests focus on Machine Learning and Computer Vision, specifically Industrial Anomaly Detection, Multimodal Sensor Fusion, Topological Deep Learning, and Predictive Fault Diagnosis. I secured 1st Position in my academic cohort during my studies.

You can find my publications on <a href='https://scholar.google.com/citations?user=ZTuS-yUAAAAJ'><img src="https://img.shields.io/badge/Google%20Scholar-f6f6f6?logo=google-scholar&logoColor=4285F4&style=flat" style="vertical-align:middle;" alt="Google Scholar"></a>.

# 🔥 News
- *2026.01*: &nbsp;🎉🎉 Co-authored paper accepted in **IEEE TPAMI** (*Learning Topology-Aware Representations via Test-Time Adaptation for Anomaly Segmentation*).
- *2026.01*: &nbsp;🎉🎉 Co-authored paper accepted in **ECCV 2026** (*Learning Structurally Consistent Representations for Multi-View Radar Semantic Segmentation*).
- *2026.01*: &nbsp;🎉🎉 Co-authored paper accepted in **IEEE Sensors Journal** (*Hypergraph Contrastive Sensor Fusion for Multimodal Fault Diagnosis in Induction Motors*).
- *2025.12*: &nbsp;🎉🎉 Co-authored paper accepted in **DICTA 2025** (*2D-3D Feature Fusion via Cross-Modal Latent Synthesis and Attention-Guided Restoration for Industrial Anomaly Detection*).
- *2025.10*: &nbsp;💼 Appointed as Lab Instructor at Department of Computer Science, GIFT University.

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE TPAMI</div><img src='images/tpami.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Learning Topology-Aware Representations via Test-Time Adaptation for Anomaly Segmentation](#)

Ali Zia, Usman Ali, **Abdul Rehman**, Umer Ramzan, Kang Han, Muhammad Faheem, Shahnawaz Qureshi, and Wei Xiang

[**PROJECT PAGE**](#)

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2026</div><img src='images/radar.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Learning Structurally Consistent Representations for Multi-View Radar Semantic Segmentation](#)

Ali Zia, Muhammad Umer Ramzan, Abdelwahed Khamis, Usman Ali, and **Abdul Rehman**

[**PROJECT PAGE**](#)

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE Sensors Journal</div><img src='images/Hypergraph.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Hypergraph Contrastive Sensor Fusion for Multimodal Fault Diagnosis in Induction Motors](https://doi.org/10.1109/JSEN.2025.3648413)

Usman Ali, Ali Zia, Waqas Ali, Umer Ramzan, **Abdul Rehman**, Muhammad Tayyab Chaudhry, Wei Xiang

[**PAPER**](https://doi.org/10.1109/JSEN.2025.3648413) | [**GITHUB**](https://github.com/EngrUsmaanAli/MM-HCAN) 

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">DICTA 2025</div><img src='images/Fusion.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[2D-3D Feature Fusion via Cross-Modal Latent Synthesis and Attention-Guided Restoration for Industrial Anomaly Detection](https://doi.org/10.1109/DICTA68720.2025.11302453)

Usman Ali, Ali Zia, **Abdul Rehman**, Umer Ramzan, Zohaib Hassan, Talha Sattar, Jing Wang, Wei Xiang

[**PAPER**](https://doi.org/10.1109/DICTA68720.2025.11302453) | [**GITHUB**](https://github.com/adabrh/MAFR) 

</div>
</div>

# 📬 Manuscripts Under Review
- *Anomaly Segmentation*: **Topology-Aware Optimal Transport for Source-Free Test-Time Adaptation in Anomaly Segmentation**  
  Ali Zia, Usman Ali, Abdelwahed Khamis, Muhammad Umer Ramzan, **Abdul Rehman**, and Wei Xiang.
- *Radar Segmentation*: **TopoRadar: Topology-Aware Multi-View Radar Semantic Segmentation**  
  Ali Zia, Muhammad Umer Ramzan, Usman Ali, **Abdul Rehman**, and Abdelwahed Khamis.
- *Object Detection*: **Residual Object Recovery via Topology-Guided Multimodal Transport for Training-Free Open-Vocabulary Detection**  
  Ali Zia, Usman Ali, Muhammad Umer Ramzan, **Abdul Rehman**, Shahnawaz Qureshi, and Wei Xiang.

# 💡 Projects

<div class="project-box">
  <div class="project-card" markdown="1">
    <h3>🤖 AI-Powered Website Chatbot <span class="project-date">May 2026</span></h3>
    *Website-Grounded Hybrid Question Answering System*
    * Developed an end-to-end platform that crawls public websites and converts their content into website-specific conversational assistants.
    * Engineered content extraction, cleaning, structuring, and indexing workflows.
    * Implemented hybrid retrieval using keyword search, vector search, structured records, metadata, full-page context, and fact-level knowledge.
    * Built grounded response controls and a unified interface for website ingestion, chat interaction, and indexed-site history.
  </div>
  
  <div class="project-card" markdown="1">
    <h3>📐 3D Industrial Anomaly Detection <span class="project-date">Nov 2024 – Aug 2025</span></h3>
    *Final Year Research Project*
    * Developed a multimodal anomaly-detection framework for identifying industrial defects from complementary 2D image and 3D point-cloud features.
    * Integrated cross-modal feature learning and attention-guided restoration to improve representation quality.
    * Achieved **97.2% image-level AUROC** and **99.3% pixel-level AUROC** during experimental evaluations.
  </div>
  
  <div class="project-card" markdown="1">
    <h3>🧬 Cervical Cancer Image Classification <span class="project-date">Aug 2024 – Oct 2024</span></h3>
    *Deep Learning Project*
    * Constructed an ensemble classification framework using EfficientNetB0, MobileNet, and ResNet50 architectures.
    * Incorporated attention mechanisms and feature-level fusion to combine complementary representations while maintaining efficiency.
    * Attained **97% classification accuracy** through model evaluation, hyperparameter refinement, and ensemble prediction.
  </div>
  
  <div class="project-card" markdown="1">
    <h3>🍃 Potato Leaf Disease Classification <span class="project-date">Mar 2024 – Apr 2024</span></h3>
    *Computer Vision Project*
    * Prepared and preprocessed plant-leaf image data to improve training consistency and model generalization.
    * Trained and optimized a convolutional neural network that achieved **98% classification accuracy**.
    * Developed a web-based interface for image submission and real-time disease prediction.
  </div>
  
  <div class="project-card" markdown="1">
    <h3>🚗 Real-Time Driver Drowsiness Detection <span class="project-date">Nov 2023 – Jan 2024</span></h3>
    *Computer Vision Project*
    * Engineered a real-time driver-monitoring system using facial-landmark analysis to identify visual indicators of drowsiness.
    * Implemented continuous camera-based inference to monitor eye closure and head-position patterns.
    * Integrated an automated alert mechanism to warn drivers when drowsiness-related behavior was detected.
  </div>
</div>

# 🏫 Experience
* **Lab Instructor** (2025 – Present)  
  *Department of Computer Science, GIFT University, Gujranwala, Pakistan*
  * Deliver laboratory instruction for Artificial Intelligence, Data Mining, Data Visualization, and Introduction to Data Science.
  * Guide students in implementing machine-learning workflows, data-analysis techniques, visualization methods, and programming assignments.
  * Support laboratory assessments, debugging activities, and the evaluation of student projects.
  * Conduct collaborative research in computer vision, multimodal learning, anomaly detection, and semantic segmentation.
  * Contribute to literature reviews, dataset preparation, ablation studies, result analysis, and the preparation of manuscripts.

# 🛠️ Technical Skills

<div class="skills-container">
  <div class="skills-category">
    <h4>Programming</h4>
    <p>Python, R, C++, Java</p>
  </div>
  <div class="skills-category">
    <h4>Machine Learning</h4>
    <p>PyTorch, TensorFlow, scikit-learn, CNNs, representation learning, multimodal learning</p>
  </div>
  <div class="skills-category">
    <h4>Generative AI</h4>
    <p>Retrieval-augmented generation (RAG), hybrid retrieval, vector search, keyword search, grounded QA, prompt engineering</p>
  </div>
  <div class="skills-category">
    <h4>Computer Vision</h4>
    <p>Image classification, anomaly detection, semantic segmentation, feature fusion, attention mechanisms</p>
  </div>
  <div class="skills-category">
    <h4>Data & Tools</h4>
    <p>NumPy, pandas, Jupyter Notebook, Git, GitHub, LaTeX, Markdown</p>
  </div>
  <div class="skills-category">
    <h4>Research Methods</h4>
    <p>Test-time adaptation, optimal transport, topological deep learning, unsupervised learning, feature alignment</p>
  </div>
</div>

# 🎖️ Honors and Awards

<ul class="awards-list">
  <li><em>2022</em> secured **1st Position** in the BS Data Science program academic cohort during the Spring 2022 semester at GIFT University.</li>
  <li><em>Oct 2023</em> **Introduction to Data Science in Python**, University of Michigan (via Coursera).</li>
  <li><em>Sept 2023</em> **What Is Data Science?**, IBM (via Coursera).</li>
  <li><em>Aug 2023</em> **Python for Data Science, AI & Development**, IBM (via Coursera).</li>
</ul>

# 📖 Education
- *2021.12 - 2025.10*, **Bachelor of Science in Data Science**, GIFT University, Gujranwala, Pakistan.  
  **CGPA**: 3.53/4.00  
  **Selected Coursework**: Deep Learning, Machine Learning, Computer Vision, Data Mining, Big Data Analytics, Data Warehousing, Applications of Data Science.  
  **Undergraduate Thesis**: *2D-3D Feature Fusion via Cross-Modal Latent Synthesis and Attention-Guided Restoration for Industrial Anomaly Detection* (accepted at DICTA 2025).
