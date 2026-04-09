# Deployment Guide for Prompt Injection Demo

This guide explains how to deploy the malicious webpage to GitHub Pages for your security awareness blog demonstration.

## Prerequisites

- GitHub account
- Git installed locally
- This repository initialized with git

## Option 1: GitHub Pages Deployment (Recommended)

### Step 1: Initialize Git Repository (if not already done)

```bash
cd /Users/dmjdarshan/Experiments/Blogs/webpage-prompt-injection
git init
```

### Step 2: Create .gitignore

Create a `.gitignore` file to exclude unnecessary files:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Note: We ARE committing .env files for this demo (they contain dummy data)
# In real projects, NEVER commit .env files!
```

### Step 3: Create GitHub Repository

1. Go to https://github.com/new
2. Create a new repository (e.g., `prompt-injection-demo`)
3. Do NOT initialize with README (we already have files)
4. Copy the repository URL

### Step 4: Push to GitHub

```bash
# Add all files
git add .

# Commit
git commit -m "Initial commit: Prompt injection security demo"

# Add remote (replace with your repository URL)
git remote add origin https://github.com/YOUR_USERNAME/prompt-injection-demo.git

# Push to main branch
git branch -M main
git push -u origin main
```

### Step 5: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages** (in left sidebar)
3. Under "Source", select:
   - Branch: `main`
   - Folder: `/webpage` (or `/root` if you move webpage contents to root)
4. Click **Save**
5. Wait 1-2 minutes for deployment
6. Your site will be available at: `https://YOUR_USERNAME.github.io/prompt-injection-demo/`

### Step 6: Test the Deployment

Visit your GitHub Pages URL and verify:
- ✅ Page loads correctly
- ✅ Styling is applied
- ✅ All sections are visible
- ✅ HTML comments contain the prompt injection

## Option 2: Netlify Deployment (Fallback)

If GitHub Pages doesn't work, use Netlify:

### Step 1: Create Netlify Account

1. Go to https://netlify.com
2. Sign up (can use GitHub account)

### Step 2: Deploy via Drag & Drop

1. Go to https://app.netlify.com/drop
2. Drag the entire `webpage/` folder onto the page
3. Wait for deployment
4. Get your URL: `https://random-name-12345.netlify.app`

### Step 3: (Optional) Deploy via Git

1. Push your code to GitHub (see Option 1, Steps 1-4)
2. In Netlify, click "New site from Git"
3. Connect to GitHub and select your repository
4. Set build settings:
   - Base directory: `webpage`
   - Build command: (leave empty)
   - Publish directory: `.` (current directory)
5. Click "Deploy site"

## Verification Checklist

After deployment, verify:

- [ ] Website loads at the public URL
- [ ] All styling is correct
- [ ] Navigation works
- [ ] Code blocks are formatted properly
- [ ] View page source and confirm HTML comments are present
- [ ] The prompt injection is embedded in comments

## Security Note

⚠️ **IMPORTANT**: This deployment contains intentionally malicious content for educational purposes. 

- Only share the URL in controlled, educational contexts
- Clearly label it as a security demonstration
- Include warnings about the prompt injection
- Do not use this technique maliciously

## Next Steps

Once deployed:

1. Copy the public URL
2. Test the attack in the `test/` folder using Copilot
3. Document the results with screenshots
4. Write the blog post explaining the vulnerability

## Troubleshooting

### GitHub Pages not loading CSS

If CSS doesn't load on GitHub Pages:

1. Check that `styles.css` is in the same directory as `index.html`
2. Verify the link tag in HTML: `<link rel="stylesheet" href="styles.css">`
3. Clear browser cache and hard refresh (Ctrl+Shift+R or Cmd+Shift+R)

### 404 Error on GitHub Pages

- Wait 2-3 minutes after enabling Pages
- Check that you selected the correct branch and folder
- Verify files are actually in the repository

### Netlify Build Fails

- Ensure you're deploying the `webpage/` folder, not the root
- Check that all files (HTML, CSS, Python) are present
- Try drag-and-drop method instead of Git deployment

## URLs to Save

After deployment, save these URLs:

- **GitHub Repository**: `https://github.com/YOUR_USERNAME/prompt-injection-demo`
- **GitHub Pages URL**: `https://YOUR_USERNAME.github.io/prompt-injection-demo/`
- **Netlify URL** (if used): `https://your-site-name.netlify.app`

Use the public URL in your blog post and when testing with Copilot.