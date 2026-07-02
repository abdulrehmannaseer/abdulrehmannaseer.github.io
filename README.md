# 🎓 Abdul Rehman Naseer — Personal Portfolio & Research Site

<p align="center">
  <a href="https://abdulrehmannaseer.github.io/"><img src="https://img.shields.io/badge/Live%20Website-abdulrehmannaseer.github.io-4f46e5?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Live Portfolio"></a>
  <a href="https://scholar.google.com/citations?user=ZTuS-yUAAAAJ"><img src="https://img.shields.io/badge/Google%20Scholar-Profile-blue?style=for-the-badge&logo=google-scholar&logoColor=white" alt="Google Scholar"></a>
  <a href="https://orcid.org/0009-0001-0003-3932"><img src="https://img.shields.io/badge/ORCID-0009--0001--0003--3932-a6cf39?style=for-the-badge&logo=orcid&logoColor=white" alt="ORCID"></a>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/abdulrehmannaseer"><img src="https://img.shields.io/badge/LinkedIn-abdulrehmannaseer-0077b5?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://github.com/adabrh"><img src="https://img.shields.io/badge/GitHub-adabrh-181717?style=flat&logo=github&logoColor=white" alt="GitHub"></a>
  <a href="https://www.researchgate.net/profile/Abdul-Rehman-490"><img src="https://img.shields.io/badge/ResearchGate-Profile-00ccb1?style=flat&logo=researchgate&logoColor=white" alt="ResearchGate"></a>
</p>

Welcome! This repository houses the source code for my professional academic portfolio, showcasing my research, publications, and accomplishments in **Data Science, Machine Learning, and Computer Vision**.

---

## 🔍 Research Interests

My academic work focus lies at the intersection of deep learning and real-world industrial computer vision challenges. Key domains include:
* **Industrial Anomaly Detection**: Unsupervised anomaly localization in 2D and 3D sensor streams.
* **Multimodal Sensor Fusion**: Fusing point cloud data (3D) and camera frames (2D) for robust diagnosis.
* **Topological Deep Learning & Graphs**: Exploring complex structural alignments via hypergraphs.
* **Predictive Fault Diagnosis**: High-accuracy fault classification in induction motors.

---

## 📝 Featured Publications

### 1. Multimodal Fault Diagnosis (IEEE Sensors Journal, 2026)
* **Title**: *Hypergraph Contrastive Sensor Fusion for Multimodal Fault Diagnosis in Induction Motors*
* **Links**: [Paper Link](https://doi.org/10.1109/JSEN.2025.3648413) | [Official Code Repository](https://github.com/EngrUsmaanAli/MM-HCAN)

### 2. 2D-3D Feature Fusion (DICTA 2025)
* **Title**: *2D-3D Feature Fusion via Cross-Modal Latent Synthesis and Attention-Guided Restoration for Industrial Anomaly Detection*
* **Links**: [Paper Link](https://doi.org/10.1109/DICTA68720.2025.11302453) | [Official Code Repository](https://github.com/adabrh/MAFR)

---

## 💻 Tech Stack & Architecture

This portfolio has been customized with a **modern, premium, responsive light theme** with clean layout structures:
* **Core Framework**: Jekyll (GitHub Pages compatible static site builder)
* **Typography**: Outfit (headings) and Inter (body copy) loaded dynamically via Google Fonts
* **Layouts**: 
  * Sticky Glassmorphic Header navigation bar with backdrop-blur
  * Responsive Sidebar Profile Card (vertical alignment on desktop, horizontal alignment on mobile)
  * Dynamic Research Timeline for the News section
  * Modern Card Layouts for publication details with floating conference tags and outline icon buttons
* **Metadata & SEO**: Injected JSON-LD Person schema markup, canonical links, and custom title templates to index cleanly on Google.

---

## ⚡ Automation: Google Scholar Sync

This repository contains a **Google Scholar citation crawler** powered by GitHub Actions:
* **Daily citation sync**: A Python script in `.github/workflows` executes daily to update publication citation counts dynamically.
* **Live Shields.io integration**: Fetches statistics automatically and updates shields on the homepage.

---

## 🛠️ Local Development

If you wish to build or test the site locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/abdulrehmannaseer/abdulrehmannaseer.github.io.git
   cd abdulrehmannaseer.github.io
   ```
2. **Install Jekyll dependencies**:
   ```bash
   bundle install
   ```
3. **Run the local livereload server**:
   ```bash
   bundle exec jekyll serve
   ```
4. Open `http://localhost:4000` in your web browser.
