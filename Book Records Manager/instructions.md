# === C Program: [Program Name] ===

📌 **Description**  
[Provide a short description of what the C program does. This could be an overview of its functionality or goal.]

---

## 🖥️ Requirements

- A Unix-like terminal (Linux, macOS, or WSL on Windows)
- GCC compiler (e.g., via `build-essential` on Ubuntu)
- `make` utility (optional but recommended)

---

## 🔧 How to Compile and Run (GitHub Codespaces)

1. Open this repository in the GitHub Codespace you created, as outlined in the main `README.md`.
2. Wait for the environment to initialize.
3. In the terminal, navigate to the program's folder. Example:

    ```bash
    cd "Book Records Manager"
    ```

4. Compile and run the program using one of the following:

    **Option A: Using `gcc` directly**
    ```bash
    gcc lab2.c -o lab2
    ./lab2 < lab2in
    ```

    **Option B: Using `make` (if a Makefile is provided)**
    ```bash
    make run
    ```

---

## 🧹 How to Clean Up

If a Makefile is present:

```bash
make clean
