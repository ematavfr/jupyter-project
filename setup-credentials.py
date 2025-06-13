#!/usr/bin/env python3
"""
Credential Setup Helper for Jupyter ML Project

This script helps you set up credentials for your ML pipeline.
Run this in a Jupyter notebook or terminal to configure your environment.
"""

import os
import json
from pathlib import Path

def setup_github_credentials():
    """Setup GitHub credentials for Git operations"""
    print("📚 Setting up GitHub credentials...")
    
    # Check if SSH keys are available
    ssh_key_path = Path.home() / '.ssh' / 'id_ed25519'
    if ssh_key_path.exists():
        print("✅ SSH key found - Git operations will use SSH")
        print("   You can clone repos with: git clone git@github.com:ematavfr/repo-name.git")
    else:
        print("❌ SSH key not found")
        print("   You'll need to use HTTPS with Personal Access Token")
    
    # Check for GitHub token in environment
    github_token = os.getenv('GITHUB_TOKEN')
    if github_token:
        print("✅ GitHub token found in environment")
    else:
        print("💡 Consider setting GITHUB_TOKEN for API access")

def setup_ml_credentials():
    """Setup ML platform credentials"""
    print("\n🤖 Setting up ML platform credentials...")
    
    credentials = {
        'HUGGINGFACE_TOKEN': 'Hugging Face Hub access',
        'OPENAI_API_KEY': 'OpenAI API access',
        'WANDB_API_KEY': 'Weights & Biases tracking',
    }
    
    for env_var, description in credentials.items():
        if os.getenv(env_var):
            print(f"✅ {env_var} found - {description}")
        else:
            print(f"💡 {env_var} not set - {description}")

def create_sample_config():
    """Create sample configuration files"""
    print("\n⚙️ Creating sample configuration...")
    
    # Sample requirements.txt for ML
    requirements = [
        "# Core ML libraries",
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "scikit-learn>=1.0.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "",
        "# Deep Learning",
        "torch>=1.11.0",
        "transformers>=4.15.0",
        "datasets>=2.0.0",
        "",
        "# MLOps",
        "mlflow>=1.24.0",
        "wandb>=0.12.0",
        "dvc>=2.8.0",
        "",
        "# GitHub Integration",
        "PyGithub>=1.55",
        "gitpython>=3.1.0",
        "",
        "# Utilities",
        "python-dotenv>=0.19.0",
        "tqdm>=4.62.0",
        "click>=8.0.0",
    ]
    
    with open('requirements.txt', 'w') as f:
        f.write('\n'.join(requirements))
    
    print("✅ Created requirements.txt")
    
    # Sample .env file
    if not os.path.exists('.env'):
        print("💡 Copy .env.template to .env and fill in your credentials")
        print("   cp .env.template .env")
    else:
        print("✅ .env file already exists")

def setup_git_config():
    """Setup Git configuration for the project"""
    print("\n🔧 Git configuration...")
    
    git_config = Path.home() / '.gitconfig'
    if git_config.exists():
        print("✅ Git config found")
    else:
        print("💡 Set up Git config:")
        print("   git config --global user.name 'Your Name'")
        print("   git config --global user.email 'your.email@example.com'")

def main():
    """Main setup function"""
    print("🚀 Jupyter ML Project Credential Setup")
    print("=" * 40)
    
    setup_github_credentials()
    setup_ml_credentials()
    create_sample_config()
    setup_git_config()
    
    print("\n" + "=" * 40)
    print("🎯 Next Steps:")
    print("1. Copy .env.template to .env and fill in your credentials")
    print("2. Install requirements: pip install -r requirements.txt")
    print("3. Test Git access: git clone git@github.com:ematavfr/your-repo.git")
    print("4. Start building your ML pipeline!")
    print("\n💡 Access this project at: http://sites/jupyter")

if __name__ == '__main__':
    main()

