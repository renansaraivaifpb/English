import subprocess
import datetime


REPO_PATH = r"C:\Users\engre\Documents\English"

commit_message = f"""Atualização automática Anki - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
I implemented an algorithm to recognize gesture in real time
This algorithm is easy to implement on embedding systems
During the week, I like to work out at the gym...
"""


def run_cmd(cmd, cwd=None):
    """Executa comandos no terminal"""
    result = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, shell=True)
    if result.returncode != 0:
        print(f"Erro: {result.stderr}")
    else:
        print(result.stdout)

def sync_repo():
    print(
    "🔄 Adicionado cartões:\n"
    "I implemented an algorithm to recognize gesture in real time\n"
    "This algorithm is easy to implement on embedding systems\n"
    "During the week, I like to work out at the gym..."
    )
    run_cmd("git add .", cwd=REPO_PATH)
    run_cmd(f'git commit -m "{commit_message}"', cwd=REPO_PATH)
    run_cmd("git push origin main", cwd=REPO_PATH)

if __name__ == "__main__":
    sync_repo()
