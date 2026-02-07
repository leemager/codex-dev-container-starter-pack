# Codex Sandbox Starter Pack (Beginner Friendly)

Thanks to GPT 5.2 for helping me create this starter pack!

This folder is a **safe training wheels setup** for running **OpenAI Codex in VS Code with Python** inside a **Docker “Dev Container”**.

The goal is to keep Codex’s actions **inside this project folder**, not across your whole device.

---
## What you get

- A ready-to-open **VS Code Dev Container** (`.devcontainer/`)
- A **Codex config** that defaults to:
  - `sandbox_mode = "workspace-write"` (can only write inside the project)
  - network **OFF**
  - approvals **OFF** (for smooth demos)
- A small fake dataset: `data/campus_cafe_sales.csv`
- A Python script that makes summaries + plots: `analysis/analyze.py`
  - Saves images into `outputs/`

---
## Quick start (the 60-second version)

1) Install **Docker Desktop** (Windows or Mac) and make sure it’s running.
2) Install **VS Code**
3) In VS Code, install the **Dev Containers** extension (and the Open AI Codex extension if you don't already have it).
4) Open this folder in VS Code.
5) Run: **Dev Containers: Reopen in Container**
6) In the VS Code terminal (now running *inside* the container), run:

   ```bash
   python analysis/analyze.py
   ```

Then open the `outputs/` folder to see the plots.

---
## If you’ve never used Linux / bash (tiny primer)

Inside the container you’re in a small Linux environment.

- `pwd`  → “where am I?”
- `ls`   → list files
- `cd foldername` → go into a folder
- `python file.py` → run a Python script

**Important:** Linux commands are powerful. In this starter pack we rely on the container boundary so mistakes don’t hit your whole computer.

---
## Safety rules for beginners

- Only open **ONE dedicated project folder** in the container (like this one).
- Do **not** open your entire `Documents` or `Desktop` as the workspace.
- Keep backups of anything important (always non-negotiable whether you're using AI or not).

---
## Where the Codex config lives

We include a template at:

- `.codex/config.toml`

And the Dev Container automatically copies it to:

- `~/.codex/config.toml` (inside the container)

change to feature branch only

---
## What to ask Codex for scenarios where internet access is needed i.e. installing libraries (since we block internet access in this dev container environment by default)

If you are new, start with plain-English requests. Codex can suggest the code *and* the exact terminal command to run.

First, open a terminal in VS Code:

1. Top menu: `Terminal` -> `New Terminal`
2. You should now see a terminal panel at the bottom of VS Code.

Then ask Codex things like:

- `I need a way to extract text from PDFs. Can you help me do this in this project? Please include any install command I need.`
- `I got ModuleNotFoundError for pypdf. Please give me the exact pip command to fix it.`

If a library is missing, Codex should usually tell you to run something like:

```bash
pip install -r analysis/requirements.txt
```

or:

```bash
pip install pypdf
```

---
## Git in VS Code (GUI workflow for beginners)

Why this matters (especially with AI coding assistants):

- You can experiment safely.
- You can keep a clean `main` branch.
- You can revert mistakes quickly.
- You can merge only the changes you trust.

Recommended workflow every time:

1. Keep `main` as your stable version.
2. Create a feature branch for each new idea.
3. Commit on that feature branch.
4. Merge to `main` only when you are happy.

### Step-by-step in VS Code (no command line required)

1. Open the **Source Control** view (branch icon on the left).
2. If repo is not initialized yet, click **Initialize Repository**.
3. Create a branch:
   - Click the branch name in the bottom status bar (or `...` menu in Source Control).
   - Choose **Create new branch...**
   - Name it something clear, e.g. `feature/green-plots`.
4. Make your file edits.
5. In Source Control, review changed files.
6. Stage changes:
   - Click `+` beside each file (or **Stage All Changes**).
7. Type a commit message, e.g. `Change plot color to dark green`.
8. Click **Commit**.
9. Switch back to `main`:
   - Click branch name in status bar -> select `main`.
10. Merge feature branch into `main`:
   - Open branch menu -> **Merge Branch...** -> choose `feature/green-plots`.
11. Run the script again to confirm everything still works.

### Example feature branch change: make plots dark green

Use this as your first practical Git exercise:

1. Create branch: `feature/green-plots`
2. In `analysis/analyze.py`, update plot calls to use a dark green color, for example:

```python
daily.plot(color="darkgreen")
by_outlet.plot(kind="bar", color="darkgreen")
top_items.sort_values().plot(kind="barh", color="darkgreen")
```

3. Commit on the feature branch.
4. Merge into `main` with the VS Code GUI.
5. Run:

```bash
python analysis/analyze.py
```

6. Open `outputs/` and confirm the new plot style.
