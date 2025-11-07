# 📤 How to Publish to GitHub

Follow these steps to publish your ETF Screener to GitHub:

## Option 1: Using GitHub Website (Easiest)

### Step 1: Create a New Repository on GitHub

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right → "New repository"
3. Repository settings:
   - **Name**: `etf-screener` (or any name you prefer)
   - **Description**: "Live ETF screening tool with moving averages and advanced filtering"
   - **Public** or **Private**: Your choice
   - ⚠️ **DO NOT** initialize with README, .gitignore, or license (we already have these)
4. Click "Create repository"

### Step 2: Initialize and Push from Terminal

Open Terminal and run these commands:

```bash
# Navigate to your project
cd "/Users/rhuria/ETF search"

# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Commit the files
git commit -m "Initial commit: ETF Screener with live Yahoo Finance data"

# Add your GitHub repository as remote (replace with your actual repository URL)
git remote add origin https://github.com/YOUR_USERNAME/etf-screener.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Update README on GitHub

After pushing, you may want to:
1. Delete or rename the Salesforce `README.md` 
2. Rename `README_ETF.md` to `README.md`

Run:
```bash
cd "/Users/rhuria/ETF search"
rm README.md
mv README_ETF.md README.md
git add .
git commit -m "Update README for ETF Screener"
git push
```

---

## Option 2: Using GitHub Desktop (GUI)

### Step 1: Download GitHub Desktop
- Download from: https://desktop.github.com/

### Step 2: Create Repository
1. Open GitHub Desktop
2. File → Add Local Repository
3. Choose: `/Users/rhuria/ETF search`
4. Click "Create Repository"

### Step 3: Publish
1. Click "Publish repository" button
2. Choose name and description
3. Select Public or Private
4. Click "Publish Repository"

---

## ⚠️ Important: Clean Up Salesforce Files (Optional)

If you want this repository to be ONLY for the ETF Screener (not Salesforce), consider removing these files before publishing:

```bash
cd "/Users/rhuria/ETF search"

# Remove Salesforce-specific files
rm -rf force-app/
rm -rf scripts/apex/
rm -rf scripts/soql/
rm -rf config/
rm sfdx-project.json
rm .forceignore
rm eslint.config.js
rm jest.config.js
rm package.json

# Update README
rm README.md
mv README_ETF.md README.md

# Commit changes
git add .
git commit -m "Remove Salesforce files, ETF Screener only"
git push
```

---

## 📋 Before Publishing Checklist

- [ ] `.gitignore` is in place (✅ Already created)
- [ ] `LICENSE` file exists (✅ Already created)
- [ ] `README.md` or `README_ETF.md` has proper documentation (✅ Already created)
- [ ] No sensitive information (API keys, passwords) in code
- [ ] `requirements.txt` is up to date (✅ Already created)
- [ ] Test that the app works after cloning

---

## 🔐 Security Note

✅ **Good news**: Your code doesn't contain any API keys or sensitive information!

The application uses Yahoo Finance's public data, which doesn't require API keys.

---

## 📝 Recommended Repository Settings

After publishing, consider:

1. **Add Topics** (on GitHub):
   - `etf`
   - `finance`
   - `stock-market`
   - `yahoo-finance`
   - `flask`
   - `python`
   - `trading`

2. **Add Description**:
   "Live ETF screening tool with real-time data from Yahoo Finance. Features moving averages, advanced filtering, and sortable columns."

3. **Enable Issues**: So users can report bugs or request features

4. **Add a `.github/workflows/` folder** for CI/CD (optional, advanced)

---

## 🚀 Quick Command Summary

```bash
# Navigate to project
cd "/Users/rhuria/ETF search"

# Clean up (optional - removes Salesforce files)
rm -rf force-app scripts/apex scripts/soql config
rm sfdx-project.json .forceignore eslint.config.js jest.config.js package.json
rm README.md && mv README_ETF.md README.md

# Initialize and publish
git init
git add .
git commit -m "Initial commit: ETF Screener"
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

---

## ✅ You're Done!

Your ETF Screener is now published and ready to share! 🎉

Share the repository URL with others, and they can clone and use your screener.

