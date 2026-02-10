#!/bin/bash
# Presentation Workflow - Git Push Script
# Usage: ./git_push.sh <project_dir> <repo_name> <commit_message>

set -e

PROJECT_DIR="${1:?Error: Project directory required}"
REPO_NAME="${2:?Error: Repository name required}"
COMMIT_MSG="${3:-Presentation update}"

cd "$PROJECT_DIR"

# Initialize Git if not already initialized
if [ ! -d ".git" ]; then
    git init
    echo "Git repository initialized."
fi

# Add all files
git add -A

# Commit changes
git commit -m "$COMMIT_MSG" || echo "Nothing to commit."

# Create remote repository if it doesn't exist
if ! gh repo view "$REPO_NAME" &>/dev/null; then
    gh repo create "$REPO_NAME" --private --source=. --push
    echo "Repository '$REPO_NAME' created and pushed."
else
    # Push to existing repository
    git push origin main 2>/dev/null || git push origin master 2>/dev/null || echo "Push complete or remote setup needed."
fi

echo "=== GIT PUSH COMPLETE ==="
