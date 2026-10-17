---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<span class="anchor" id="about-me"></span>

I am an AI and computer vision researcher working on multimodal learning, 2D–3D representation learning, point-cloud analysis, anomaly detection, semantic segmentation, radar perception, and sensor fusion. My research contributions have been accepted at NeurIPS, IEEE TPAMI, ECCV, IEEE Sensors Journal, and DICTA.

I develop PyTorch-based research frameworks for cross-modal representation learning, topology-aware modelling, test-time adaptation, and feature alignment, with an emphasis on rigorous experimental evaluation. My goal is to build robust perception systems that adapt to changing environments. I secured 1st Position in my academic cohort during my studies.

{% assign citations = site.data.scholar %}
<p class="scholar-line">Publications on <a href="{{ site.author.googlescholar }}" aria-label="Scholar — view publications and the live citation count">Scholar</a><span id="scholar-citations" class="scholar-citations" data-snapshot-url="{{ '/scholar.json' | relative_url }}" data-citations="{{ citations.citations }}" data-updated="{{ citations.updated }}"> · <span data-citation-count>{{ citations.citations }}</span> <span data-citation-label>citations</span></span></p>

My research interests include:

<div class="research-topics" role="list" aria-label="Research topics">
  <div class="research-topic" role="listitem">
    <i class="fas fa-search" aria-hidden="true"></i>
    <div><h3>Industrial Anomaly Detection</h3><ul><li>Unsupervised anomaly segmentation</li><li>Test-time adaptation</li></ul></div>
  </div>
  <div class="research-topic" role="listitem">
    <i class="fas fa-layer-group" aria-hidden="true"></i>
    <div><h3>Multimodal Sensor Fusion</h3><ul><li>2D–3D feature alignment</li><li>Multi-view radar segmentation</li></ul></div>
  </div>
  <div class="research-topic" role="listitem">
    <i class="fas fa-project-diagram" aria-hidden="true"></i>
    <div><h3>Topological Deep Learning</h3><ul><li>Topology-aware representations</li><li>Structural consistency</li></ul></div>
  </div>
  <div class="research-topic" role="listitem">
    <i class="fas fa-heartbeat" aria-hidden="true"></i>
    <div><h3>Predictive Fault Diagnosis</h3><ul><li>Multimodal condition monitoring</li><li>Sensor representation learning</li></ul></div>
  </div>
</div>

## News {#news}

- **2026** — Our paper, “[Topology-Aware Optimal Transport for Source-Free Test-Time Adaptation in Anomaly Segmentation](https://topoot.github.io/),” has been accepted at **NeurIPS 2026**.
- **2026** — Our paper, “[Learning Topology-Aware Representations via Test-Time Adaptation for Anomaly Segmentation](https://topotta.github.io/),” has been accepted for publication in **IEEE TPAMI**.
- **2026** — Our paper, “[Learning Structurally Consistent Representations for Multi-View Radar Semantic Segmentation](https://hyperradar.github.io/),” has been accepted at **ECCV 2026**.
- **Feb 2026** — Our paper, “[Hypergraph Contrastive Sensor Fusion for Multimodal Fault Diagnosis in Induction Motors](https://doi.org/10.1109/JSEN.2025.3648413),” has been published in **IEEE Sensors Journal**.
- **Dec 2025** — Our paper, “[2D-3D Feature Fusion via Cross-Modal Latent Synthesis and Attention-Guided Restoration for Industrial Anomaly Detection](https://doi.org/10.1109/DICTA68720.2025.11302453),” has been published in the proceedings of **DICTA 2025**.
- **Oct 2025** — Joined the School of Engineering & Applied Sciences at GIFT University as a **Lab Instructor**.

## Publications {#publications}

<div class="paper-box"><div class="paper-box-image"><div><div class="badge">IEEE TPAMI</div><img src="images/tpami.png" alt="Overview diagram of topology-aware test-time adaptation for anomaly segmentation"></div></div>
<div class="paper-box-text" markdown="1">

**Learning Topology-Aware Representations via Test-Time Adaptation for Anomaly Segmentation**

Ali Zia, Usman Ali, **Abdul Rehman**, Umer Ramzan, Kang Han, Muhammad Faheem, Shahnawaz Qureshi, and Wei Xiang

[**Project Page**](https://topotta.github.io)

</div>
</div>

<div class="paper-box"><div class="paper-box-image"><div><div class="badge">ECCV 2026</div><img src="images/radar.png" alt="Overview diagram of structurally consistent multi-view radar semantic segmentation"></div></div>
<div class="paper-box-text" markdown="1">

**Learning Structurally Consistent Representations for Multi-View Radar Semantic Segmentation**

Ali Zia, Muhammad Umer Ramzan, Abdelwahed Khamis, Usman Ali, and **Abdul Rehman**

[**Project Page**](https://hyperradar.github.io)

</div>
</div>

<div class="paper-box"><div class="paper-box-image"><div><div class="badge">NeurIPS 2026</div><img src="images/TopoOT.png" alt="TopoOT framework for topology-aware optimal transport and source-free test-time adaptation" loading="lazy"></div></div>
<div class="paper-box-text" markdown="1">

**Topology-Aware Optimal Transport for Source-Free Test-Time Adaptation in Anomaly Segmentation**

Ali Zia, Usman Ali, Abdelwahed Khamis, Muhammad Umer Ramzan, **Abdul Rehman**, and Wei Xiang

[**Project Page**](https://topoot.github.io/) [**GitHub**](https://github.com/adabrh/TopoOT)

</div>
</div>

<div class="paper-box"><div class="paper-box-image"><div><div class="badge">IEEE Sensors Journal</div><img src="images/Hypergraph.png" alt="Architecture diagram of hypergraph contrastive sensor fusion for multimodal fault diagnosis"></div></div>
<div class="paper-box-text" markdown="1">

[Hypergraph Contrastive Sensor Fusion for Multimodal Fault Diagnosis in Induction Motors](https://doi.org/10.1109/JSEN.2025.3648413)

Usman Ali, Ali Zia, Waqas Ali, Umer Ramzan, **Abdul Rehman**, Muhammad Tayyab Chaudhry, Wei Xiang

[**Paper**](https://doi.org/10.1109/JSEN.2025.3648413) [**GitHub**](https://github.com/EngrUsmaanAli/MM-HCAN)

</div>
</div>

<div class="paper-box"><div class="paper-box-image"><div><div class="badge">DICTA 2025</div><img src="images/Fusion.png" alt="Pipeline diagram of 2D-3D feature fusion with attention-guided restoration for industrial anomaly detection"></div></div>
<div class="paper-box-text" markdown="1">

[2D-3D Feature Fusion via Cross-Modal Latent Synthesis and Attention-Guided Restoration for Industrial Anomaly Detection](https://doi.org/10.1109/DICTA68720.2025.11302453)

Usman Ali, Ali Zia, **Abdul Rehman**, Umer Ramzan, Zohaib Hassan, Talha Sattar, Jing Wang, Wei Xiang

[**Paper**](https://doi.org/10.1109/DICTA68720.2025.11302453) [**GitHub**](https://github.com/adabrh/MAFR)

</div>
</div>

## Manuscripts Under Review {#manuscripts}

- *Radar Segmentation*: **TopoRadar: Topology-Aware Multi-View Radar Semantic Segmentation**  
  Ali Zia, Muhammad Umer Ramzan, Usman Ali, **Abdul Rehman**, and Abdelwahed Khamis.
- *Object Detection*: **Residual Object Recovery via Topology-Guided Multimodal Transport for Training-Free Open-Vocabulary Detection**  
  Ali Zia, Usman Ali, Muhammad Umer Ramzan, **Abdul Rehman**, Shahnawaz Qureshi, and Wei Xiang.

## Experience {#experience}

- **Lab Instructor & Researcher** (2025 – Present)<br>
  *School of Engineering & Applied Sciences, GIFT University, Gujranwala, Pakistan*
  - Deliver laboratory instruction for Artificial Intelligence, Data Mining, Data Visualization, and Introduction to Data Science.
  - Guide students in implementing machine-learning workflows, data-analysis techniques, visualization methods, and programming assignments.
  - Support laboratory assessments, debugging activities, and the evaluation of student projects.
  - Conduct collaborative research in computer vision, multimodal learning, anomaly detection, and semantic segmentation.
  - Contribute to literature reviews, dataset preparation, ablation studies, result analysis, and the preparation of manuscripts.

## Technical Skills {#skills}

<div class="skills-container">
  <div class="skills-category">
    <h3>Programming</h3>
    <p>Python, R, C++, Java</p>
  </div>
  <div class="skills-category">
    <h3>Machine Learning</h3>
    <p>PyTorch, TensorFlow, scikit-learn, CNNs, representation learning, multimodal learning</p>
  </div>
  <div class="skills-category">
    <h3>Generative AI</h3>
    <p>Retrieval-augmented generation (RAG), hybrid retrieval, vector search, keyword search, grounded QA, prompt engineering</p>
  </div>
  <div class="skills-category">
    <h3>Computer Vision</h3>
    <p>Image classification, anomaly detection, semantic segmentation, feature fusion, attention mechanisms</p>
  </div>
  <div class="skills-category">
    <h3>Data &amp; Tools</h3>
    <p>NumPy, pandas, Jupyter Notebook, Git, GitHub, LaTeX, Markdown</p>
  </div>
  <div class="skills-category">
    <h3>Research Methods</h3>
    <p>Test-time adaptation, optimal transport, topological deep learning, unsupervised learning, feature alignment</p>
  </div>
</div>

## Honors and Awards {#awards}

- *2022*: Secured **1st Position** in the BS Data Science program academic cohort during the Spring 2022 semester at GIFT University.
- *Oct 2023*: **Introduction to Data Science in Python**, University of Michigan (via Coursera).
- *Sept 2023*: **What Is Data Science?**, IBM (via Coursera).
- *Aug 2023*: **Python for Data Science, AI & Development**, IBM (via Coursera).

## Education {#education}

- *2021.12 – 2025.10*: **Bachelor of Science in Data Science**, GIFT University, Gujranwala, Pakistan.  
  **CGPA**: 3.53/4.00  
  **Selected Coursework**: Deep Learning, Machine Learning, Computer Vision, Data Mining, Big Data Analytics, Data Warehousing, Applications of Data Science.  
  **Undergraduate Thesis**: *2D-3D Feature Fusion via Cross-Modal Latent Synthesis and Attention-Guided Restoration for Industrial Anomaly Detection* (accepted at DICTA 2025).
