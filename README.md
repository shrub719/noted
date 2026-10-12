# Noted

Like [Mark](https://github.com/shrub719/mark), but for lecture notes.

The proper setup looks like this:

```
├── build
│   ├── main.py
│   ├── noted.sh
│   ├── README.md
│   └── template.html
├── include
│   ├── default.min.css
│   ├── highlight.min.js
│   ├── style.css
│   └── tex-chtml.js
├── src
└── view
```

- `build/` contains this repository.
    - `build/noted.sh` should be sourced in your terminal.
- `include/` has the relevant files from MathJax and `highlight.js` included 
   in `build/template.html`.
- `src/` is where the actual written notes go, in the form of `.md` files.
- `view/` is where output is generated, as `.html` files that can be viewed in a web browser.

To use Noted, just run `noted` in your terminal. While the command is running, it will
generate a live preview of `src/` in `view/` with full Markdown, syntax highlighting
and `$`-delimited $\TeX$ support.

