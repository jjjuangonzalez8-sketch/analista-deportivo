name: Analista Deportivo

on:
  workflow_dispatch:
  schedule:
    - cron: "0 13 * * *"

jobs:
  ejecutar:
    runs-on: ubuntu-latest
    steps:
      - name: Ejecutar bot
        run: python bot.py
