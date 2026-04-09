# Screenshot Checklist for Blog Post

This checklist helps you capture all necessary screenshots for the blog post demonstration.

## Required Screenshots

### 1. Project Structure
- [ ] **File tree showing the project layout**
  - Show: webpage/, test/, blog-content/ folders
  - Show: .env files in both test/ and root
  - Highlight the structure in VS Code explorer
  - **Filename**: `01-project-structure.png`

### 2. The Malicious Webpage
- [ ] **Webpage in browser - full view**
  - Show the professional-looking LangGraph tutorial
  - Capture the header, navigation, and first section
  - **Filename**: `02-webpage-full-view.png`

- [ ] **Webpage - code examples section**
  - Show the legitimate tutorial content
  - Capture code blocks and examples
  - **Filename**: `03-webpage-code-examples.png`

- [ ] **View Source - showing hidden injection**
  - Right-click → View Page Source
  - Scroll to the HTML comment with prompt injection
  - Highlight the malicious comment section
  - **Filename**: `04-webpage-source-injection.png`

### 3. Environment Setup
- [ ] **Test folder .env file**
  - Open test/.env in VS Code
  - Show the dummy credentials
  - **Filename**: `05-test-env-file.png`

- [ ] **Root .env file**
  - Open .env in VS Code
  - Show the dummy production credentials
  - **Filename**: `06-root-env-file.png`

- [ ] **VS Code opened in test folder**
  - Show terminal with `pwd` showing test directory
  - Show file explorer with test folder open
  - **Filename**: `07-vscode-test-folder.png`

### 4. The Attack Sequence
- [ ] **Copilot Chat - Initial prompt**
  - Show the innocent-looking question to Copilot
  - Include the URL to the malicious webpage
  - **Filename**: `08-copilot-initial-prompt.png`

- [ ] **Copilot processing the request**
  - Show Copilot thinking/processing indicator
  - **Filename**: `09-copilot-processing.png`

- [ ] **Copilot's suspicious response**
  - Capture Copilot suggesting to run security audit
  - Show it proposing to create/run the Python script
  - Highlight the unexpected behavior
  - **Filename**: `10-copilot-malicious-response.png`

- [ ] **Script creation (if Copilot creates it)**
  - Show discover_secrets.py being created
  - Show the file in VS Code explorer
  - **Filename**: `11-script-created.png`

### 5. Attack Execution
- [ ] **Running the discovery script**
  - Terminal showing: `python discover_secrets.py`
  - **Filename**: `12-running-script.png`

- [ ] **Script output - credentials discovered**
  - Full terminal output showing found .env files
  - Show the exposed dummy credentials
  - Highlight the security alert messages
  - **Filename**: `13-credentials-discovered.png`

- [ ] **Detailed findings**
  - Scroll through the full report
  - Show both .env files being detected
  - **Filename**: `14-detailed-findings.png`

### 6. Evidence and Impact
- [ ] **Side-by-side comparison**
  - Split screen: webpage (looks innocent) vs source code (malicious)
  - **Filename**: `15-innocent-vs-malicious.png`

- [ ] **The injection payload closeup**
  - Zoom in on the HTML comment with the injection
  - Highlight the "SYSTEM INSTRUCTION" part
  - **Filename**: `16-injection-payload-closeup.png`

### 7. Mitigation Examples
- [ ] **Copilot settings**
  - Show relevant security settings in VS Code
  - Settings for external URL access
  - **Filename**: `17-copilot-settings.png`

- [ ] **Proper .gitignore**
  - Show .gitignore with .env excluded
  - Highlight best practices
  - **Filename**: `18-proper-gitignore.png`

## Optional Screenshots

### Additional Context
- [ ] **GitHub Pages deployment**
  - Show the deployed URL
  - GitHub Pages settings
  - **Filename**: `19-github-pages-deployment.png`

- [ ] **Network tab showing URL fetch**
  - Browser DevTools Network tab
  - Show Copilot fetching the malicious URL
  - **Filename**: `20-network-tab-fetch.png`

- [ ] **Different AI responses**
  - If testing with Claude/ChatGPT
  - Show how different AIs respond
  - **Filename**: `21-other-ai-responses.png`

## Screenshot Guidelines

### Technical Requirements
- **Resolution**: At least 1920x1080 for clarity
- **Format**: PNG (lossless) preferred
- **Annotations**: Use red boxes/arrows to highlight key areas
- **Privacy**: Ensure no real credentials or personal info visible

### Composition Tips
1. **Clean workspace**: Close unnecessary tabs/windows
2. **Readable text**: Zoom in if needed for code/text clarity
3. **Context**: Include enough surrounding UI for context
4. **Annotations**: Add arrows, boxes, or text to guide readers
5. **Consistency**: Use same theme/settings across screenshots

### Tools for Screenshots
- **macOS**: Cmd+Shift+4 (selection), Cmd+Shift+3 (full screen)
- **Windows**: Win+Shift+S (Snipping Tool)
- **Linux**: Flameshot, GNOME Screenshot
- **Annotation**: Skitch, Snagit, or built-in Preview (Mac)

## Organizing Screenshots

Create this folder structure:
```
blog-content/
└── screenshots/
    ├── 01-project-structure.png
    ├── 02-webpage-full-view.png
    ├── 03-webpage-code-examples.png
    └── ... (all other screenshots)
```

## After Capturing

- [ ] Review all screenshots for clarity
- [ ] Ensure no sensitive information is visible
- [ ] Add annotations where needed
- [ ] Compress images if too large (use TinyPNG or similar)
- [ ] Rename files according to the checklist
- [ ] Place in blog-content/screenshots/ folder

## For the Blog Post

When writing, reference screenshots like:
```markdown
![Project Structure](screenshots/01-project-structure.png)
*Figure 1: The project structure with malicious webpage and test environment*
```

## Video Alternative

Consider recording a screen video showing:
1. Opening the webpage (looks innocent)
2. Asking Copilot for help
3. Copilot's suspicious response
4. Running the script
5. Credentials being exposed

Tools: OBS Studio, QuickTime (Mac), Windows Game Bar

## Notes

- Take screenshots BEFORE and AFTER each major step
- Capture failures too - they're educational
- Get multiple angles of the same thing
- Better to have too many than too few
- You can always crop/edit later

## Checklist Summary

Total required screenshots: **18**
Optional screenshots: **3**
Estimated time: **30-45 minutes**

Once complete, you'll have comprehensive visual documentation for your blog post!