---
marp: true
theme: custom   # 👈 use a custom theme name, not "default"
math: katex
paginate: true
size: 16:9
title: "Product Docs — Minimal"
author: "Avra"
footer: "24f1002255@ds.study.iitm.ac.in"
style: |
  /* @theme custom */   /* 👈 required: declare the custom theme */
  :root { --accent: #0b5fff; --muted: #6b7280; }

  section {
    font-family: system-ui, -apple-system, 'Segoe UI', Roboto, Arial;
    color:#111;
    background:#fff;
  }

  h1 { color: var(--accent); }

  section::after {
    content: attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
    position: absolute;
    bottom: 18px;
    right: 24px;
    opacity:.6;
    font-size:13px;
  }

  footer {
    position: absolute;
    left: 24px;
    bottom: 18px;
    font-size:13px;
    opacity:.7;
  }
---
  section.lead h1 {
    color: var(--accent);
    letter-spacing: 0.02em;
  }

  section.hero {
    color: #fff;
    text-shadow: 0 2px 8px rgba(0,0,0,.45);
  }
---

class: lead

# Product Documentation
### Single-Source & Version-Controlled  
Contact: **24f1002255@ds.study.iitm.ac.in**

---

class: hero
backgroundImage: url("./assets/bg.jpg")
backgroundSize: cover

# Architecture Snapshot

---

## Algorithmic Complexity

- Sorting (MergeSort):  
  $$T(n) = 2T\!\left(\frac{n}{2}\right) + \Theta(n) \;\;\implies\;\; T(n)=\Theta(n \log n)$$

- Binary Search:  
  $$T(n)=T\!\left(\tfrac{n}{2}\right)+\Theta(1) \;\;\implies\;\; T(n)=\Theta(\log n)$$

---

## Source Reference

📄 View raw deck in GitHub:  
[docs.marp.md](https://raw.githubusercontent.com/avra/GA7/main/docs.marp.md)

---

# Thank You!  
📩 24f1002255@ds.study.iitm.ac.in
