import subprocess
import datetime


REPO_PATH = r"C:\Users\engre\Documents\English"

commit_message = f"""Atualização automática Anki - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"""


def run_cmd(cmd, cwd=None):
    """Executa comandos no terminal"""
    result = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, shell=True)
    if result.returncode != 0:
        print(f"Erro: {result.stderr}")
    else:
        print(result.stdout)

def sync_repo():
    print("🔄 Adicionado cartões:\n")
    run_cmd("git add .", cwd=REPO_PATH)
    run_cmd(f'git commit -m "{commit_message}"', cwd=REPO_PATH)
    run_cmd("git push origin main", cwd=REPO_PATH)

if __name__ == "__main__":
    sync_repo()
