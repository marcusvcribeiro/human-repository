import pyautogui
import time
import random
import cv2
import numpy as np
from PIL import Image

# --- CONFIGURACOES ---
urls_para_visitar = [
    "https://primeng.org/table",
    "https://primeng.org/dialog",
    "https://primeng.org/inputtext",
    "https://seusistema.com.br/dashboard",
    "https://seusistema.com.br/relatorios"
]
TEMPO_MIN_ESPERA = 60
TEMPO_MAX_ESPERA = 120

# --- FUNCOES DE TEMPO E MOVIMENTO ---
def esperar(min_s, max_s):
    tempo = random.uniform(min_s, max_s)
    print(f"⏳ Esperando por {round(tempo, 2)} segundos...")
    time.sleep(tempo)

def mover_mouse_suavemente(x, y):
    pyautogui.moveTo(x, y, duration=random.uniform(0.2, 0.8))

def clicar_com_duracao(x, y):
    mover_mouse_suavemente(x, y)
    pyautogui.mouseDown()
    esperar(0.05, 0.15)
    pyautogui.mouseUp()
    print(f"🖱️ Clicou em: ({x}, {y})")

def clicar_centro_aleatorio():
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2
    rand_x = center_x + random.randint(-50, 50)
    rand_y = center_y + random.randint(-30, 30)
    clicar_com_duracao(rand_x, rand_y)

# --- NAVEGACAO CHROME ---
def abrir_url_em_aba(url):
    pyautogui.hotkey('ctrl', 't')
    esperar(1, 2)
    pyautogui.typewrite(url, interval=random.uniform(0.03, 0.09))
    pyautogui.press('enter')
    print(f"🌐 Acessou: {url}")
    esperar(5, 8)

def interagir_com_site():
    for _ in range(random.randint(2, 5)):
        pyautogui.scroll(-random.randint(200, 600))
        esperar(1, 3)
    clicar_centro_aleatorio()

# --- USO DO VS CODE COMO DESENVOLVEDOR ---
def simular_codigo_vs_code():
    for _ in range(random.randint(3, 7)):
        pyautogui.press(random.choice(['down', 'up', 'right', 'left']))
        esperar(0.1, 0.3)
    pyautogui.hotkey('ctrl', '`')
    esperar(1, 2)
    comandos = ['npm run start', 'git status', 'clear']
    comando = random.choice(comandos)
    pyautogui.typewrite(comando, interval=0.1)
    pyautogui.press('enter')
    esperar(2, 5)

# --- VISÃO COMPUTACIONAL (IMAGEM ALVO) ---
def encontrar_elemento_na_tela(imagem_alvo_path):
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
    imagem_alvo = cv2.imread(imagem_alvo_path, 0)
    res = cv2.matchTemplate(screenshot_gray, imagem_alvo, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(res)
    if max_val > 0.8:
        return max_loc
    return None

# --- POSICIONAMENTO INICIAL ---
print("Posicione o mouse sobre o ícone do VS Code em 5 segundos...")
time.sleep(5)
vscode_pos = pyautogui.position()
print(f"✅ Posição do VS Code: {vscode_pos}")

print("Agora posicione o mouse sobre o ícone do Chrome em 5 segundos...")
time.sleep(5)
chrome_pos = pyautogui.position()
print(f"✅ Posição do Chrome: {chrome_pos}")

# --- LOOP PRINCIPAL ---
while True:
    print("\n🔄 Novo ciclo iniciado...\n")
    clicar_com_duracao(*vscode_pos)
    esperar(2, 4)
    clicar_centro_aleatorio()
    esperar(2, 4)
    pyautogui.hotkey('ctrl', 'a')
    esperar(1, 2)
    pyautogui.hotkey('alt', 'shift', 'f')
    esperar(2, 3)
    pyautogui.hotkey('ctrl', 's')
    esperar(2, 3)
    simular_codigo_vs_code()

    clicar_com_duracao(*chrome_pos)
    esperar(2, 4)
    url = random.choice(urls_para_visitar)
    abrir_url_em_aba(url)
    interagir_com_site()

    # Verifica se botao_salvar.png aparece na tela
    local = encontrar_elemento_na_tela("botao_salvar.png")
    if local:
        print("📍 Botão Salvar detectado na tela!")
        clicar_com_duracao(local[0], local[1])

    esperar(TEMPO_MIN_ESPERA, TEMPO_MAX_ESPERA)
