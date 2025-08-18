    ---
    marp: true
    theme: default
    math: katex
    paginate: true
    size: 16:9
    title: "Product Docs — Minimal"
    author: "Avra"
    footer: "24f1002255@ds.study.iitm.ac.in"
    style: |
        :root { --accent: #0b5fff; --muted: #6b7280; }
        section { font-family: system-ui, -apple-system, 'Segoe UI', Roboto, Arial; color:#111; background:#fff; }
        h1 { color: var(--accent); }
        section::after { content: attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total); position: absolute; bottom: 18px; right: 24px; opacity:.6; font-size:13px; }
        footer { position: absolute; left: 24px; bottom: 18px; font-size:13px; opacity:.7; }
    ---

    class: lead

    # Product Docs
    24f1002255@ds.study.iitm.ac.in

    ---

    class: hero
    backgroundImage: url('https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=1920&auto=format&fit=crop')
    backgroundSize: cover

    # Architecture snapshot

    ---

    ## Complexity

    $$T(n)=2T\left(\frac{n}{2}\right)+\Theta(n)\implies T(n)=\Theta(n\log n)$$

    ---

    ## Raw GitHub URL

    https://raw.githubusercontent.com/avra/GA7/main/docs.marp.md

    ---

    Thank you!
