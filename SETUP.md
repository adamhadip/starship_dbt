# 🚀 Starship dbt

**Starship dbt** helps you quickly set up your own **dbt** and **Airflow** environment with minimal hassle.

---

## 📦 Prerequisites

Make sure you have [Homebrew](https://brew.sh/) installed, then run:

```bash
brew install uv
```

## ⚒️ Installation

Clone this repository using:

```zsh
git clone https://github.com/yourusername/starship_dbt.git
cd starship_dbt
```
After that running `uv sync`

Then Install power user dbt in extension 

Setting in extension of sqlfluff executable path `/Users/adamhadipratama/projects/dbt-airflow/starship_dbt/.venv/bin/sqlfluff` 

Write files.associations in your setting then add:
| item | Value 
-- | -- 
*.sql | jinja-sql 
*.yml | jinja-yml