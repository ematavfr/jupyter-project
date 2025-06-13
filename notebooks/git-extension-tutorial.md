# JupyterLab Git Extension Tutorial

A visual guide to using the `@jupyterlab/git` extension for notebook version control.

## 📱 Accessing the Git Extension

1. **Open JupyterLab**: http://sites/jupyter
2. **Find Git Tab**: Look for the Git icon 🔍 in the left sidebar
3. **Click to Open**: The Git panel will show your repository status

## 👁️ Visual Interface Overview

### **Git Panel Sections:**
- **📊 Current Repository**: Shows branch and status
- **📝 Changes**: Modified, added, and deleted files
- **📋 Staged Changes**: Files ready for commit
- **📋 Commit History**: Browse past commits
- **🌿 Branch Selector**: Switch between branches

## 🚀 Common Workflows

### **1. Making Your First Commit**

1. **Create/Edit a Notebook**
   - Open a new notebook or edit existing one
   - Make your changes and save

2. **View Changes in Git Panel**
   - Modified files appear under "Changes"
   - Click file name to see diff view

3. **Stage Changes**
   - Click "+" next to file name, OR
   - Drag file from "Changes" to "Staged Changes"

4. **Write Commit Message**
   - Type message in the commit box
   - Example: "Add data exploration notebook"

5. **Commit**
   - Click "Commit" button
   - Changes are now committed locally

6. **Push to GitHub**
   - Click the "Push" button (up arrow)
   - Your changes are now on GitHub!

### **2. Working with Branches**

1. **Create New Branch**
   - Click branch dropdown (current branch name)
   - Click "New Branch"
   - Enter branch name: `feature/new-model`
   - Click "Create Branch"

2. **Switch Branches**
   - Click branch dropdown
   - Select branch from list
   - JupyterLab will switch to that branch

3. **Merge Branches**
   - Switch to target branch (usually `main`)
   - Click "Merge Branch" button
   - Select source branch
   - Confirm merge

### **3. Viewing Notebook Diffs**

1. **Click Modified Notebook**
   - In the Git panel, click any modified `.ipynb` file
   - Diff view opens in main area

2. **Understand Diff View**
   - 🟢 **Green**: Added cells/content
   - 🔴 **Red**: Removed cells/content
   - 🟡 **Yellow**: Modified cells/content
   - **Cell-by-cell**: See exactly which cells changed

3. **Review Changes**
   - Scroll through to review all modifications
   - Ensure you're happy with changes before committing

### **4. Cleaning Notebook Outputs**

1. **Before Committing** (Important!)
   - Notebook outputs can be large and change frequently
   - Clear outputs before committing

2. **Manual Clearing**
   - In notebook: `Kernel` → `Restart & Clear Output`
   - Or use terminal: `jupyter nbconvert --clear-output --inplace *.ipynb`

3. **Using Git Script**
   - In terminal: `./git-workflow.sh clear`
   - This clears all notebook outputs automatically

### **5. Resolving Conflicts**

1. **When Conflicts Occur**
   - Git panel will show conflicted files with ⚠️
   - Click on conflicted file

2. **Visual Conflict Resolution**
   - JupyterLab shows both versions
   - Choose which changes to keep
   - Edit directly in the interface

3. **Mark as Resolved**
   - Save the resolved file
   - Stage the resolved file
   - Commit the resolution

## 📅 Git History Browser

1. **Access History**
   - Click "History" tab in Git panel
   - Browse chronological list of commits

2. **View Commit Details**
   - Click any commit to see:
     - Full commit message
     - Author and timestamp
     - List of changed files

3. **Compare Commits**
   - Select two commits to compare
   - See differences between versions

## 📡 Remote Operations

### **Pull Latest Changes**
1. Click "Pull" button (down arrow)
2. Fetches and merges remote changes
3. Resolves conflicts if any

### **Push Local Changes**
1. Make sure all changes are committed
2. Click "Push" button (up arrow)
3. Sends commits to GitHub

### **Clone Repositories**
1. Use terminal: `git clone git@github.com:ematavfr/repo-name.git`
2. Or use JupyterLab's Git menu: `Git` → `Clone a Repository`

## 📝 Best Practices

### **✅ Do:**
- Clear notebook outputs before committing
- Write descriptive commit messages
- Commit frequently with small, focused changes
- Use branches for experimental work
- Review diffs before committing
- Pull latest changes before starting work

### **❌ Don't:**
- Commit notebooks with large outputs
- Make huge commits with many unrelated changes
- Work directly on main branch for experiments
- Ignore merge conflicts
- Commit sensitive data or credentials

## 🔧 Troubleshooting

### **Git Extension Not Showing**
- Refresh JupyterLab browser tab
- Check if you're in a Git repository
- Restart JupyterLab container

### **SSH Authentication Issues**
- Check SSH keys are mounted: `ls -la ~/.ssh`
- Test connection: `ssh -T git@github.com`
- Verify SSH key is added to GitHub

### **Large File Issues**
- Use `.gitignore` for large data files
- Consider Git LFS for large model files
- Clear notebook outputs regularly

## 🎉 Advanced Tips

1. **Keyboard Shortcuts**
   - `Ctrl+Shift+G`: Open Git panel
   - `Ctrl+Shift+P`: Command palette → search "Git"

2. **Git Configuration**
   - Set user name: `git config user.name "Your Name"`
   - Set email: `git config user.email "your@email.com"`

3. **Integration with GitHub**
   - Your SSH keys enable seamless push/pull
   - Use GitHub issues and pull requests
   - Link commits to issues with #issue-number

The JupyterLab Git extension makes version control visual and intuitive for notebook development! 🚀

