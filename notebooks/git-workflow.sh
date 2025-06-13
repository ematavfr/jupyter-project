#!/bin/bash

# Git Workflow Helper for Jupyter Notebooks
# Run this script from the notebooks/ directory

set -e

echo "📚 Jupyter Notebook Git Workflow Helper"
echo "====================================="

# Function to clear notebook outputs
clear_outputs() {
    echo "🧹 Clearing notebook outputs..."
    find . -name "*.ipynb" -exec jupyter nbconvert --clear-output --inplace {} \;
    echo "✅ Outputs cleared"
}

# Function to check Git status
check_status() {
    echo "🔍 Git status:"
    cd ..
    git status notebooks/
    cd notebooks
}

# Function to commit changes
commit_changes() {
    if [ -z "$1" ]; then
        echo "❌ Please provide a commit message"
        echo "Usage: $0 commit 'Your commit message'"
        exit 1
    fi
    
    echo "💾 Committing changes..."
    cd ..
    git add notebooks/
    git commit -m "$1"
    echo "✅ Changes committed"
}

# Function to push changes
push_changes() {
    echo "🚀 Pushing to GitHub..."
    cd ..
    git push
    echo "✅ Changes pushed to GitHub"
}

# Function to pull latest changes
pull_changes() {
    echo "🔄 Pulling latest changes..."
    cd ..
    git pull
    echo "✅ Latest changes pulled"
}

# Function to show recent commits
show_history() {
    echo "📅 Recent notebook commits:"
    cd ..
    git log --oneline -10 -- notebooks/
}

# Main script logic
case $1 in
    "clear")
        clear_outputs
        ;;
    "status")
        check_status
        ;;
    "commit")
        clear_outputs
        commit_changes "$2"
        ;;
    "push")
        clear_outputs
        commit_changes "$2"
        push_changes
        ;;
    "pull")
        pull_changes
        ;;
    "history")
        show_history
        ;;
    "full")
        if [ -z "$2" ]; then
            echo "❌ Please provide a commit message"
            echo "Usage: $0 full 'Your commit message'"
            exit 1
        fi
        clear_outputs
        commit_changes "$2"
        push_changes
        ;;
    *)
        echo "🔧 Jupyter Notebook Git Workflow Helper"
        echo ""
        echo "Usage: $0 <command> [message]"
        echo ""
        echo "Commands:"
        echo "  clear           Clear outputs from all notebooks"
        echo "  status          Show git status for notebooks"
        echo "  commit 'msg'    Clear outputs and commit changes"
        echo "  push 'msg'      Clear outputs, commit, and push"
        echo "  pull            Pull latest changes from remote"
        echo "  history         Show recent notebook commits"
        echo "  full 'msg'      Complete workflow: clear, commit, push"
        echo ""
        echo "Examples:"
        echo "  $0 clear"
        echo "  $0 commit 'Add data exploration notebook'"
        echo "  $0 full 'Complete model training pipeline'"
        echo ""
        echo "💡 Run from the notebooks/ directory"
        ;;
esac

