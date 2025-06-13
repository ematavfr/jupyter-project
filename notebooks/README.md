# Notebooks Directory

This directory contains your Jupyter notebooks that will be edited and modified in the JupyterLab container.

## 📁 Organization Structure

```
notebooks/
├── 01-data-exploration/     # Data analysis and EDA notebooks
├── 02-preprocessing/        # Data cleaning and feature engineering
├── 03-modeling/            # Model training and evaluation
├── 04-experiments/         # Experiment tracking and hyperparameter tuning
├── 05-deployment/          # Model deployment and serving
├── utils/                  # Utility functions and helper notebooks
└── templates/              # Notebook templates for common tasks
```

## 🔄 Git Workflow for Notebooks

### **📱 JupyterLab Git Extension (GUI)**
The `@jupyterlab/git` extension is pre-installed! Access Git features directly in JupyterLab:

- **Git Tab**: Click the Git icon in the left sidebar
- **Visual Diff**: See changes highlighted in notebooks
- **Commit Interface**: Stage, commit, and push via GUI
- **Branch Management**: Create, switch, and merge branches
- **History View**: Browse commit history visually

### **💻 Command Line Options:**

#### **1. Using Git Helper Script (Recommended)**
```bash
# Complete workflow (clear outputs + commit + push)
./git-workflow.sh full "Add data exploration notebook"

# Just commit
./git-workflow.sh commit "Update preprocessing pipeline"

# Clear outputs only
./git-workflow.sh clear
```

#### **2. Manual Git Commands**
```bash
# Clear outputs first (important!)
jupyter nbconvert --clear-output --inplace *.ipynb

# Standard Git workflow
git add .
git commit -m "Add new notebook"
git push
```

### **Best Practices:**

1. **✨ Use JupyterLab Git Extension for:**
   - Visual diffs of notebook changes
   - Easy staging and committing
   - Branch management
   - Conflict resolution

2. **📋 Clear Outputs Before Committing**
   - Use script: `./git-workflow.sh clear`
   - Or manually: `jupyter nbconvert --clear-output --inplace *.ipynb`

3. **📝 Use Descriptive Commit Messages**
   - `01_data_exploration.ipynb`
   - `02_feature_engineering.ipynb`
   - `03_model_training_v1.ipynb`

4. **🔄 Commit Frequently**
   - Small, focused commits
   - Document major experiments
   - Use branches for experimental work

## 🛠️ Container Integration

- **Container Path**: `/home/jovyan/work/` (mounted from `./notebooks/`)
- **Git Access**: SSH keys automatically available
- **Environment**: All credentials loaded from `.env`
- **Persistence**: All changes saved to host filesystem

## 📊 Notebook Types

### **1. Data Exploration**
- Load and explore datasets
- Generate visualizations
- Statistical analysis

### **2. Preprocessing**
- Data cleaning
- Feature engineering
- Data transformation pipelines

### **3. Model Training**
- Train ML models
- Hyperparameter tuning
- Cross-validation

### **4. Evaluation**
- Model evaluation metrics
- Performance comparison
- Result visualization

### **5. Deployment**
- Model serving code
- API endpoints
- Production pipelines

## 💡 Tips

- Use relative paths: `../data/dataset.csv`
- Keep notebooks focused on single tasks
- Use markdown cells for documentation
- Clear outputs before committing to Git
- Use version control for important iterations

