# JupyterLab ML Pipeline Project

A complete machine learning development environment with JupyterLab, secure credential management, and GitHub integration.

## 🚀 Quick Start

1. **Setup credentials**:
   ```bash
   cp .env.template .env
   # Edit .env with your actual credentials
   python setup-credentials.py
   ```

2. **Start JupyterLab**:
   ```bash
   cd /Users/adminmac
   ./manage-sites.sh start-infra  # Start Traefik if not running
   ./manage-sites.sh start jupyter-project
   ```

3. **Access JupyterLab**:
   - URL: http://sites/jupyter
   - SSH keys and Git config automatically mounted
   - Environment variables loaded from .env

## 📁 Project Structure

```
jupyter-project/
├── notebooks/           # Jupyter notebooks
├── data/               # Datasets (ignored in git)
├── models/             # Trained models (ignored in git)
├── credentials/        # API keys and service accounts (ignored in git)
├── config/            # Configuration files
├── .env.template      # Template for environment variables
├── .env              # Your actual credentials (ignored in git)
├── setup-credentials.py # Credential setup helper
├── requirements.txt   # Python dependencies
└── docker-compose.yml # Container configuration
```

## 🔑 Credential Types & Usage

### **1. SSH Keys (Git Operations)**
- ✅ **Already configured** - Your SSH keys are mounted
- **Usage**: `git clone git@github.com:ematavfr/repo-name.git`
- **Benefits**: Secure, no tokens in notebooks

### **2. GitHub Personal Access Token (API)**
- **Setup**: https://github.com/settings/tokens
- **Scopes**: `repo`, `read:user`, `user:email`
- **Usage**: GitHub API access, automated workflows
- **Environment**: `GITHUB_TOKEN=ghp_...`

### **3. ML Platform Tokens**
```bash
# Hugging Face (for transformers, datasets)
HUGGINGFACE_TOKEN=hf_...

# OpenAI (for GPT models)
OPENAI_API_KEY=sk-...

# Weights & Biases (experiment tracking)
WANDB_API_KEY=...
```

### **4. Cloud Storage Credentials**
```bash
# AWS (for S3, SageMaker)
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...

# Google Cloud (service account JSON)
GCP_SERVICE_ACCOUNT_KEY_PATH=/home/jovyan/credentials/gcp-key.json
```

## 🛠️ Features

- **Data Science Environment**: Pre-installed ML libraries
- **Git Integration**: SSH keys and config automatically mounted
- **Secure Credentials**: Environment variables loaded from .env
- **Data Persistence**: All notebooks, data, and models saved locally
- **GitHub Ready**: Clone, commit, and push directly from notebooks
- **ML Platform Integration**: Hugging Face, OpenAI, W&B tokens
- **Cloud Storage**: AWS S3, Google Cloud Storage support

## 🔧 Setup Instructions

### **1. Copy Environment Template**
```bash
cp .env.template .env
```

### **2. Edit .env with Your Credentials**
```bash
# GitHub
GITHUB_USERNAME=ematavfr
GITHUB_EMAIL=your-email@example.com
GITHUB_TOKEN=ghp_your_token_here

# ML Platforms
HUGGINGFACE_TOKEN=hf_your_token_here
OPENAI_API_KEY=sk_your_key_here
WANDB_API_KEY=your_wandb_key_here
```

### **3. Run Setup Helper**
```bash
python setup-credentials.py
```

### **4. Install Dependencies in Jupyter**
```bash
# In a Jupyter notebook or terminal
pip install -r requirements.txt
```

## 💡 Usage Examples

### **Clone Private Repos (SSH)**
```python
# In Jupyter notebook
!git clone git@github.com:ematavfr/my-ml-project.git
```

### **Access GitHub API**
```python
import os
from github import Github

g = Github(os.getenv('GITHUB_TOKEN'))
repo = g.get_repo('ematavfr/my-repo')
```

### **Load Hugging Face Models**
```python
import os
from transformers import AutoTokenizer

# Token automatically used from environment
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
```

### **Track Experiments with W&B**
```python
import wandb
import os

wandb.login(key=os.getenv('WANDB_API_KEY'))
wandb.init(project='my-ml-project')
```

## 🔐 Security Best Practices

- ✅ **Never commit .env files** - Already in .gitignore
- ✅ **Use SSH keys for Git** - More secure than HTTPS tokens
- ✅ **Rotate tokens regularly** - Update .env as needed
- ✅ **Minimal token scopes** - Only grant necessary permissions
- ✅ **Separate credentials per project** - Use project-specific .env files

## 📚 Requirements

- Docker & Docker Compose
- SSH key configured with GitHub
- `/etc/hosts` entry: `127.0.0.1 sites` (already configured)

