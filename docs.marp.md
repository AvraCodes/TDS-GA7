# CloudSync API Documentation Repository

## File Structure
```
cloudsync-docs/
├── .github/
│   └── workflows/
│       ├── build.yml
│       └── deploy.yml
├── docs/
│   └── slides.md
├── themes/
│   └── custom.css
├── images/
│   ├── api-architecture.png
│   └── error-handling.png
├── dist/
│   ├── .gitkeep
│   └── (generated files)
├── .gitignore
├── package.json
├── README.md
└── marp.config.js
```

## File Contents:

### 1. `package.json`
```json
{
  "name": "cloudsync-api-docs",
  "version": "1.0.0",
  "description": "CloudSync API Documentation Presentation",
  "main": "index.js",
  "scripts": {
    "start": "marp -s docs/ -p 8080",
    "build": "marp docs/slides.md -o dist/slides.html --theme themes/custom.css",
    "build:pdf": "marp docs/slides.md --pdf --allow-local-files -o dist/slides.pdf",
    "build:pptx": "marp docs/slides.md --pptx -o dist/slides.pptx",
    "build:all": "npm run build && npm run build:pdf && npm run build:pptx",
    "clean": "rm -rf dist/*",
    "watch": "marp -w docs/slides.md -o dist/slides.html",
    "serve": "marp -s docs/ --theme themes/custom.css"
  },
  "keywords": [
    "marp",
    "presentation",
    "documentation",
    "api"
  ],
  "author": "Technical Documentation Team <24f1002255@ds.study.iitm.ac.in>",
  "license": "MIT",
  "devDependencies": {
    "@marp-team/marp-cli": "^3.4.0"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/yourusername/cloudsync-docs.git"
  },
  "bugs": {
    "url": "https://github.com/yourusername/cloudsync-docs/issues"
  },
  "homepage": "https://github.com/yourusername/cloudsync-docs#readme"
}
```

### 2. `docs/slides.md` (Your main presentation)
```markdown
---
marp: true
title: CloudSync API Documentation
author: Technical Documentation Team
email: 24f1002255@ds.study.iitm.ac.in
theme: gaia
paginate: true
math: katex
---

<style>
section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  font-family: 'Segoe UI', system-ui, sans-serif;
}
section.lead {
  text-align: center;
  background: linear-gradient(45deg, #1e3c72, #2a5298);
}
section.content {
  background: #f8f9fa;
  color: #333;
}
section.code {
  background: #1e1e1e;
  color: #d4d4d4;
}
h1 {
  color: #ffffff;
  border-bottom: 3px solid #ffd700;
  padding-bottom: 10px;
}
h2 {
  color: #ffd700;
  border-left: 4px solid #ffd700;
  padding-left: 15px;
}
blockquote {
  background: rgba(255, 255, 255, 0.1);
  border-left: 4px solid #ffd700;
  padding: 10px 20px;
  font-style: italic;
}
.footer-email {
  position: absolute;
  bottom: 10px;
  right: 20px;
  font-size: 0.8em;
  opacity: 0.7;
}
.complexity-box {
  background: rgba(255, 215, 0, 0.2);
  border: 2px solid #ffd700;
  border-radius: 8px;
  padding: 15px;
  margin: 10px 0;
}
</style>

<!-- _class: lead -->

# CloudSync API Documentation

## Real-time Data Synchronization Platform

**Version 2.1.0** | **Enterprise Edition**

<div class="footer-email">Contact: 24f1002255@ds.study.iitm.ac.in</div>

---

<!-- _class: content -->

## Interactive Forecast Slider

Adjust the projected **growth rate** using the slider below:

<div id="slider-demo" style="margin-top:20px; background:#fff; color:#333; padding:20px; border-radius:8px; max-width:500px;">
  <label for="growthSlider"><strong>Growth Rate (%):</strong></label><br>
  <input type="range" id="growthSlider" min="0" max="20" value="5" step="1" style="width:100%;">
  <p>Selected Growth: <span id="growthValue">5%</span></p>
  <p>Projected Revenue (baseline $1M): <span id="projectedRevenue">$1.05M</span></p>
</div>

<script>
  const slider = document.getElementById("growthSlider");
  const growthValue = document.getElementById("growthValue");
  const revenueValue = document.getElementById("projectedRevenue");
  const baseline = 1000000;

  slider.addEventListener("input", () => {
    const rate = slider.value;
    growthValue.textContent = rate + "%";
    const projected = baseline * (1 + rate/100);
    revenueValue.textContent = "$" + (projected/1000000).toFixed(2) + "M";
  });
</script>

## Table of Contents

1. **Overview & Architecture**
2. **Getting Started**
3. **Authentication & Security**
4. **Core API Endpoints**
5. **Performance Metrics**
6. **Error Handling**
7. **SDK Integration**
8. **Deployment Strategies**

> This documentation is version-controlled and automatically generated from our codebase

---

<!-- _backgroundColor: #2c3e50 -->
<!-- _color: white -->

![bg right:40% fit](../images/api-architecture.png)

## System Architecture

### Core Components

- **Sync Engine**: Real-time data processing
- **Message Queue**: Redis-based buffering
- **Rate Limiter**: Token bucket algorithm
- **Cache Layer**: Distributed caching system

### Performance Characteristics

<div class="complexity-box">

**Time Complexity Analysis:**
- Single record sync: $O(1)$  
- Batch operations: $O(n \log n)$
- Search queries: $O(\log n)$

</div>

---

<!-- _class: code -->

## Authentication Flow

```javascript
// Initialize CloudSync client
const client = new CloudSync({
  apiKey: 'your-api-key',
  environment: 'production',
  timeout: 30000
});

// Authenticate and get token
const auth = await client.authenticate({
  clientId: 'your-client-id',
  clientSecret: 'your-client-secret'
});

console.log('Access token:', auth.accessToken);
```

**Security Features:**
- OAuth 2.0 + PKCE
- JWT tokens with 1-hour expiry
- Rate limiting: 1000 req/min per API key

---

<!-- _header: **CloudSync API Endpoints** -->

## Core API Operations

| Endpoint | Method | Purpose | Rate Limit |
|----------|--------|---------|------------|
| `/sync/create` | POST | Create sync job | 100/min |
| `/sync/{id}` | GET | Get sync status | 500/min |
| `/sync/{id}/cancel` | DELETE | Cancel sync | 50/min |
| `/data/stream` | WebSocket | Real-time updates | 1000 msgs/min |

### Webhook Configuration

```bash
curl -X POST https://api.cloudsync.com/webhooks \
  -H "Authorization: Bearer {token}" \
  -d '{"url": "https://your-app.com/webhook", "events": ["sync.completed"]}'
```

---

<!-- _footer: Performance metrics updated in real-time -->

## Performance & Scalability

### Throughput Metrics

The system performance follows these mathematical models:

**Throughput Formula:**
$$T = \frac{N \times C}{L + P}$$

Where:
- $T$ = Throughput (requests/second)
- $N$ = Number of worker threads
- $C$ = CPU efficiency factor
- $L$ = Network latency (ms)
- $P$ = Processing time per request (ms)

### SLA Guarantees

- **Uptime**: 99.9% availability
- **Response Time**: < 200ms (95th percentile)
- **Data Consistency**: Eventually consistent within 5 seconds

---

<!-- _class: content -->
<!-- _backgroundColor: #ecf0f1 -->

![bg left:30% fit](../images/error-handling.png)

## Error Handling Strategy

### HTTP Status Codes

```json
{
  "error": {
    "code": "SYNC_CONFLICT",
    "message": "Data conflict detected during sync",
    "details": {
      "conflictedFields": ["lastModified", "version"],
      "resolution": "manual_merge_required"
    },
    "timestamp": "2025-08-20T10:30:00Z"
  }
}
```

### Retry Logic

Exponential backoff with jitter:
$$\text{delay} = \min(2^n \times 1000 + \text{random}(0, 1000), 30000)$$

---

<!-- _class: code -->

## SDK Integration Examples

### Python SDK

```python
from cloudsync import CloudSyncClient
import asyncio

async def sync_data():
    client = CloudSyncClient(api_key="your-key")
    
    # Create sync job
    job = await client.create_sync({
        "source": "database_a",
        "target": "database_b", 
        "strategy": "incremental"
    })
    
    # Monitor progress
    while not job.is_complete():
        status = await job.get_status()
        print(f"Progress: {status.progress}%")
        await asyncio.sleep(5)

# Run the sync
asyncio.run(sync_data())
```

---

<!-- _header: **Deployment & Operations** -->

## Deployment Strategies

### Container Deployment

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

### Kubernetes Configuration

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cloudsync-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: cloudsync-api
  template:
    metadata:
      labels:
        app: cloudsync-api
    spec:
      containers:
      - name: api
        image: cloudsync/api:2.1.0
        resources:
          requests:
            memory: "256Mi"
            cpu: "200m"
          limits:
            memory: "512Mi"
            cpu: "500m"
```

---

<!-- _backgroundColor: #27ae60 -->
<!-- _color: white -->

## Monitoring & Analytics

### Key Metrics Dashboard

- **Request Volume**: Real-time API calls per second
- **Error Rate**: Percentage of failed requests
- **Data Transfer**: Bytes synchronized per hour
- **Active Connections**: WebSocket connections count

### Performance Optimization

**Cache Hit Ratio Formula:**
$$\text{Hit Ratio} = \frac{\text{Cache Hits}}{\text{Cache Hits} + \text{Cache Misses}} \times 100\%$$

**Target**: > 85% cache hit ratio for optimal performance

### Alert Thresholds
- Response time > 500ms
- Error rate > 5%
- Memory usage > 80%

---

<!-- _class: lead -->

## Questions & Support

### Documentation Resources

- **API Reference**: https://docs.cloudsync.com/api
- **SDK Downloads**: https://github.com/cloudsync/sdks
- **Status Page**: https://status.cloudsync.com

### Contact Information

**Technical Support**: 24f1002255@ds.study.iitm.ac.in  
**Documentation Team**: docs@cloudsync.com  
**Emergency Support**: +1-800-SYNC-911

> This presentation is maintained in Git and auto-deployed on updates

**Thank you for using CloudSync!**
```

### 3. `.gitignore`
```gitignore
# Dependencies
node_modules/
package-lock.json

# Build outputs
dist/*.html
dist/*.pdf
dist/*.pptx
dist/*.png
dist/*.jpg

# System files
.DS_Store
Thumbs.db

# Editor files
.vscode/
.idea/
*.swp
*.swo

# Logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# Temporary files
*.tmp
*.temp

# Cache
.cache/
```

### 4. `README.md`
```markdown
# CloudSync API Documentation

Professional presentation slides for CloudSync API documentation, built with [Marp](https://marp.app/).

## 🚀 Quick Start

### Prerequisites
- Node.js 16+ 
- npm or yarn

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/cloudsync-docs.git
cd cloudsync-docs

# Install dependencies
npm install

# Start development server
npm start
```

## 📝 Development

### Available Scripts

| Command | Description |
|---------|-------------|
| `npm start` | Start development server with live preview |
| `npm run build` | Build HTML presentation |
| `npm run build:pdf` | Generate PDF version |
| `npm run build:pptx` | Generate PowerPoint version |
| `npm run build:all` | Build all formats |
| `npm run watch` | Watch for changes and rebuild |
| `npm run serve` | Serve presentation locally |

### File Structure

- `docs/slides.md` - Main presentation content
- `themes/custom.css` - Custom theme styles
- `images/` - Presentation images
- `dist/` - Generated output files

## 🎨 Customization

### Themes
Edit `themes/custom.css` to customize the presentation appearance:

```css
section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}
```

### Images
Add images to the `images/` directory and reference them in slides:

```markdown
![bg fit](../images/your-image.png)
```

## 🚢 Deployment

### GitHub Pages
The presentation automatically deploys to GitHub Pages via GitHub Actions.

### Manual Deployment
```bash
# Build all formats
npm run build:all

# Deploy to your hosting service
rsync -av dist/ your-server:/path/to/docs/
```

## 📊 Features

- ✅ Responsive design
- ✅ Math equations with KaTeX
- ✅ Code syntax highlighting
- ✅ Custom themes and styling
- ✅ Multiple export formats (HTML, PDF, PPTX)
- ✅ Version controlled
- ✅ Automated builds

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make changes and commit: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Create a Pull Request

## 📞 Support

- **Email**: 24f1002255@ds.study.iitm.ac.in
- **Issues**: [GitHub Issues](https://github.com/yourusername/cloudsync-docs/issues)
- **Marp Documentation**: https://marpit.marp.app/

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### 5. `.github/workflows/build.yml`
```yaml
name: Build Presentation

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
      
    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '18'
        cache: 'npm'
        
    - name: Install dependencies
      run: npm ci
      
    - name: Build presentation
      run: npm run build:all
      
    - name: Upload artifacts
      uses: actions/upload-artifact@v4
      with:
        name: presentation-files
        path: dist/
        retention-days: 30
        
    - name: Check file sizes
      run: |
        echo "Generated files:"
        ls -la dist/
        echo "File sizes:"
        du -h dist/*
```

### 6. `.github/workflows/deploy.yml`
```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18'
          cache: 'npm'
          
      - name: Install dependencies
        run: npm ci
        
      - name: Build presentation
        run: npm run build:all
        
      - name: Setup Pages
        uses: actions/configure-pages@v4
        
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: './dist'

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### 7. `marp.config.js`
```javascript
module.exports = {
  // Input directory
  inputDir: './docs',
  
  // Output directory
  outputDir: './dist',
  
  // Theme directory
  themeSet: './themes',
  
  // Default options
  options: {
    allowLocalFiles: true,
    html: true,
    pdf: {
      format: 'A4',
      landscape: true,
      margin: {
        top: '20mm',
        right: '20mm',
        bottom: '20mm',
        left: '20mm'
      }
    },
    pptx: {
      author: 'Technical Documentation Team',
      subject: 'CloudSync API Documentation',
      title: 'CloudSync API Documentation'
    }
  },
  
  // Watch options for development
  watch: {
    ignored: ['node_modules/**', 'dist/**'],
    awaitWriteFinish: {
      stabilityThreshold: 500,
      pollInterval: 100
    }
  }
};
```

### 8. `themes/custom.css`
```css
/* Custom Marp theme for CloudSync Documentation */

section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 28px;
  line-height: 1.4;
  padding: 60px;
}

/* Lead slide styling */
section.lead {
  text-align: center;
  background: linear-gradient(45deg, #1e3c72, #2a5298);
  display: flex;
  flex-direction: column;
  justify-content: center;
}

/* Content slides */
section.content {
  background: #f8f9fa;
  color: #333;
}

/* Code slides */
section.code {
  background: #1e1e1e;
  color: #d4d4d4;
}

/* Headers */
h1 {
  color: #ffffff;
  border-bottom: 3px solid #ffd700;
  padding-bottom: 15px;
  margin-bottom: 30px;
  font-size: 2.5em;
}

h2 {
  color: #ffd700;
  border-left: 4px solid #ffd700;
  padding-left: 20px;
  margin: 30px 0 20px 0;
  font-size: 1.8em;
}

h3 {
  color: #ffffff;
  font-size: 1.4em;
  margin: 25px 0 15px 0;
}

/* Paragraphs and text */
p {
  margin: 15px 0;
  text-align: left;
}

/* Lists */
ul, ol {
  margin: 20px 0;
  padding-left: 30px;
}

li {
  margin: 10px 0;
}

/* Blockquotes */
blockquote {
  background: rgba(255, 255, 255, 0.1);
  border-left: 4px solid #ffd700;
  padding: 20px;
  margin: 20px 0;
  font-style: italic;
  border-radius: 5px;
}

/* Code blocks */
pre {
  background: rgba(0, 0, 0, 0.3);
  border-radius: 8px;
  padding: 20px;
  margin: 20px 0;
  overflow-x: auto;
}

code {
  font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
  font-size: 0.85em;
}

/* Inline code */
p code, li code {
  background: rgba(255, 255, 255, 0.2);
  padding: 2px 6px;
  border-radius: 3px;
  color: #ffd700;
}

/* Tables */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  overflow: hidden;
}

th, td {
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 12px 15px;
  text-align: left;
}

th {
  background: rgba(255, 215, 0, 0.3);
  color: #ffffff;
  font-weight: bold;
}

tr:nth-child(even) {
  background: rgba(255, 255, 255, 0.05);
}

/* Images */
img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
}

/* Footer */
footer {
  position: absolute;
  bottom: 20px;
  left: 60px;
  right: 60px;
  font-size: 0.8em;
  opacity: 0.8;
  text-align: center;
}

/* Custom classes */
.footer-email {
  position: absolute;
  bottom: 10px;
  right: 20px;
  font-size: 0.8em;
  opacity: 0.7;
}

.complexity-box {
  background: rgba(255, 215, 0, 0.2);
  border: 2px solid #ffd700;
  border-radius: 8px;
  padding: 20px;
  margin: 20px 0;
}

/* Math equations */
.katex {
  font-size: 1.1em;
}

/* Animations */
section {
  animation: fadeIn 0.3s ease-in;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
```

### 9. `images/.gitkeep`
```
# Keep this directory in git
# Add your images here:
# - api-architecture.png
# - error-handling.png
# - Any other presentation images
```

### 10. `dist/.gitkeep`
```
# This directory will contain generated files
# Files here are automatically generated and should not be committed
```

## 🚀 Usage Instructions

1. **Create the repository:**
   ```bash
   mkdir cloudsync-docs
   cd cloudsync-docs
   git init
   ```

2. **Create all the files above** in their respective directories

3. **Install dependencies:**
   ```bash
   npm install
   ```

4. **Add placeholder images:**
   - Add any PNG/JPG images to the `images/` directory
   - Or use placeholder services as shown in the slides

5. **Start development:**
   ```bash
   npm start
   ```

6. **Build the presentation:**
   ```bash
   npm run build:all
   ```

7. **Commit and push to GitHub:**
   ```bash
   git add .
   git commit -m "Initial commit: CloudSync API Documentation"
   git branch -M main
   git remote add origin https://github.com/yourusername/cloudsync-docs.git
   git push -u origin main
   ```

This setup provides a complete, professional GitHub repository with automated building, deployment, and all the features you requested for your Marp presentation!
