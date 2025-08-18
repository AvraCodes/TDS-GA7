    ---
    marp: true
    theme: default
    paginate: true
    size: 16:9
    style: |
    /* Custom theme specification (overrides default) */
    :root {
        --brand: #0b5fff;
        --muted: #6b7280;
        --card: #f8fafc;
    }
    section {
        font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
        color: #111827;
        background-color: var(--card);
    }
    h1, h2 { color: var(--brand); }
    .email { font-size: 0.9rem; color: var(--muted); }
    .math { font-family: 'Cambria Math', 'Times New Roman', serif; font-size: 1.05rem; }
    /* small footer styling (page number still shown by paginate:true) */
    footer { color: var(--muted); font-size: 0.85rem; }
    ---

    <!-- _class: lead -->

    # Product Documentation — Acme Search Service

    24f1002255@ds.study.iitm.ac.in

    _Maintainable Marp slides, version-control friendly, exportable to PDF/HTML/PNG_

    ---

    ## Quick agenda

    - Problem statement
    - Design & architecture
    - Complexity & algorithms (with equations)
    - How to convert & raw GitHub URL

    ---

    ## Problem statement

    - Fast, reliable full-text search for structured documents
    - Maintain docs in Git, render with Marp for easy exports

    ---

    <!-- backgroundImage: url('https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1400&q=80') -->
    <!-- _class: center, middle -->

    ## Architecture snapshot

    This slide uses a background image and Marp slide directives for presentation polish.

    ---

    ## Algorithmic complexity

    We're using a divide-and-conquer indexing algorithm whose recurrence is:

    $$T(n) = 2T\left(\frac{n}{2}\right) + \Theta(n)$$

    By the Master Theorem, this yields:

    $$T(n) = \Theta(n\log n)$$

    <div class="math">Notes: n = number of documents; log is base 2.</div>

    ---

    ## Marp directives & custom styling

    - Front-matter controls: `marp: true`, `theme`, `paginate`, `style` (CSS block)
    - Slide directives: `<!-- backgroundImage: url('...') -->`, `<!-- _class: center -->`
    - Use KaTeX for math via `$$ ... $$`

    ---

    ## Raw GitHub URL (how to reference this file)

    Pattern for raw file on GitHub:

    https://raw.githubusercontent.com/[USER]/[REPO]/[BRANCH]/[PATH]

    Assuming this repo is pushed under the GitHub user "avra" and repository name "GA7" on branch `main`, the raw URL for this slide file would be:

    https://raw.githubusercontent.com/avra/GA7/main/docs.marp.md

    (If your GitHub username or repo differs, replace the segments accordingly.)

    ---

    ## Conversion tips

    - Export to PDF: marp --pdf docs.marp.md
    - Export to HTML: marp docs.marp.md --html
    - Keep one source file per deck to simplify CI exports

    ---

    ## Contact

    Author: 24f1002255@ds.study.iitm.ac.in

    ---
    marp: true
    lang: en
    size: 16:9
    title: "Product Documentation Presentation"
    description: "A maintainable Marp deck for software product documentation"
    author: "Avra (Technical Writer)"
    theme: custom
    math: katex
    paginate: true
    footer: "© 2025 • 24f1002255@ds.study.iitm.ac.in"
    ---

    <!--
    This single-file Marp deck is designed to be version-controlled (e.g., Git) and exportable
    via the Marp CLI to PDF/HTML/PPTX:

    marp docs.marp.md --pdf
    marp docs.marp.md --html
    marp docs.marp.md --pptx

    It includes: a custom theme, global footer with email, page numbers, background image,
    custom styling via Marp directives, and KaTeX math support.
    -->

    ```css
    /* @theme custom */
    @import 'default';

    :root {
    --accent: #3b82f6; /* Tailwind-ish indigo-500 */
    --muted: #64748b;  /* slate-500 */
    }

    section {
    font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, "Noto Sans", Ubuntu, Cantarell, "Helvetica Neue", Arial, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
    }

    /* Title styling */
    section.lead h1 {
    color: var(--accent);
    letter-spacing: 0.02em;
    }

    h2, h3 {
    color: #0f172a; /* slate-900 */
    }

    p, li {
    color: #1f2937; /* gray-800 */
    }

    /* Page numbers: uses marpit pagination data attributes */
    section::after {
    content: attr(data-marpit-pagination) " / " attr(data-marpit-pagination-total);
    position: absolute;
    bottom: 24px;
    right: 32px;
    font-size: 14px;
    opacity: .6;
    }

    /* Footer placement (content comes from front-matter `footer`) */
    footer {
    position: absolute;
    left: 32px;
    bottom: 24px;
    font-size: 14px;
    opacity: .7;
    }

    /* Utility classes for layout */
    section.two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    }

    section.emphasis h2 {
    border-left: 8px solid var(--accent);
    padding-left: 12px;
    }

    /* Background/hero slide text legibility */
    section.hero {
    color: #fff;
    text-shadow: 0 2px 8px rgba(0,0,0,.45);
    }
    ```

    ---
    class: lead

    # Product Documentation
    ### Single-Source, Version-Controlled, Multi-Format

    **Author:** Avra — *Technical Writer*

    **Contact:** 24f1002255@ds.study.iitm.ac.in

    ---
    class: hero
    backgroundImage: url('https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=1920&auto=format&fit=crop')
    backgroundSize: cover

    # Why Marp for Docs?

    - Keep docs as **Markdown** in Git
    - Export **PDF / HTML / PPTX** with Marp CLI
    - **Custom theming** & **KaTeX math**
    - Reuse content across teams and releases

    ---
    class: emphasis

    ## Goals

    - **Maintainable** documentation that lives with the codebase
    - **Consistent** look via a custom theme
    - **Automatable** exports in CI/CD (PDF/HTML/PPTX)
    - **Clear** complexity & SLA communication with math

    ---
    class: two-col

    ## Structure

    - `README.md` — quick start
    - `docs/` — detailed guides
    - `changelog.md` — release notes
    - `slides/docs.marp.md` — this deck

    ::: right
    ### Conventions
    - Use **sentence case** headings
    - Wrap at ~100 chars
    - Prefer **active voice**
    - Link to source files / issues
    :::

    ---

    ## Build & Export (CLI)

    ```bash
    # Install marp-cli locally
    npm i -D @marp-team/marp-cli

    # Export formats
    npx marp slides/docs.marp.md --pdf   # PDF
    npx marp slides/docs.marp.md --html  # Standalone HTML
    npx marp slides/docs.marp.md --pptx  # PowerPoint

    # Watch mode while writing
    npx marp -w slides/docs.marp.md --html
    ```

    > Tip: Add these as npm scripts and wire them into CI to publish artifacts per release.

    ---

    ## Algorithmic Complexity (KaTeX)

    When documenting performance, include formal complexity:

    - **Sorting (mergesort)**: $$T(n)=2\,T(\tfrac{n}{2})+\Theta(n) \implies T(n)=\Theta(n\log n)$$
    - **Binary search**: $$T(n)=T(\tfrac{n}{2})+\Theta(1) = \Theta(\log n)$$
    - **Hash table (amortized)**: $$\mathbb{E}[T_{insert}] = \Theta(1)$$
    - **Graph BFS**: $$T(V,E)=\Theta(V+E)$$

    Communicate constants where relevant (I/O, network RTT, cache effects).

    ---

    ## API Stability Policy

    - **MAJOR**: breaking changes (rare, guarded)
    - **MINOR**: additive, backwards compatible
    - **PATCH**: bug fixes only

    Document deprecations with a removal **horizon** (e.g., 2 minor releases) and provide migration steps.

    ---

    ## Example: Error Model

    Let failure probability per request be \(p\). For \(k\) retries with exponential backoff,

    $$P(\text{total failure}) = p^{\,k+1}$$

    Expected attempts:

    $$\mathbb{E}[A]=\sum_{i=1}^{k+1} i\,p^{\,i-1}(1-p) + (k+1)\,p^{\,k+1}$$

    Use this to justify client-side retry budgets and server rate limits.

    ---

    ## Custom Styling via Directives

    - `class: two-col` for simple 2-column layouts
    - `class: emphasis` to accent headings
    - Global **footer** and page numbers via theme + front-matter
    - **Hero** slide uses `backgroundImage` + `class: hero`

    ---

    ## References & Contacts

    - **Style guide**: based on internal standards + Chicago/Apple mix
    - **Issue tracker**: link to your repo board
    - **Contact**: 24f1002255@ds.study.iitm.ac.in

    Thank you!
