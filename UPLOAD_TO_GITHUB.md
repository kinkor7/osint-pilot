# How to Upload OSINT Pilot to GitHub

Follow these steps to upload your professional OSINT platform to your GitHub account.

## Step 1: Create a New Repository on GitHub
1. Go to [github.com/new](https://github.com/new).
2. Repository name: `osint-pilot`
3. Set it to **Public** or **Private** based on your preference.
4. **Do NOT** initialize with a README, license, or .gitignore.
5. Click **Create repository**.

## Step 2: Upload the Code via Terminal (Terminator)
Open your Terminator app and run these commands one by one:

```bash
# 1. Navigate to the osint_pilot project folder
cd /Users/ag700/Downloads/RE/osint_pilot

# 2. Initialize the git repository
git init

# 3. Add all files to the staging area
git add .

# 4. Commit the changes
git commit -m "Initial commit: OSINT Pilot Intelligence Platform"

# 5. Rename the branch to main
git branch -M main

# 6. Link the local repo to your GitHub repo
git remote add origin https://github.com/kinkor7/osint-pilot.git

# 7. Push the code to GitHub
git push -u origin main
```

## Troubleshooting
- **Authentication**: If GitHub asks for a password, use your **GitHub Personal Access Token (PAT)**.
- **Permission Denied**: Ensure you are logged into the correct GitHub account in your terminal.
