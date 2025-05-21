# 🏥 IMPERIUM - Sistema de Gestão de Clínicas - 2024

Frontend do sistema IMPERIUM, desenvolvido com [Vue 3](https://vuejs.org/), [TypeScript](https://www.typescriptlang.org/), [Tailwind CSS](https://tailwindcss.com/), e [Pinia](https://pinia.vuejs.org/).

---

## ⚙️ Pré-requisitos

Antes de iniciar, certifique-se de que possui o seguinte instalado:

- **Node.js** (versão 18 ou superior)  
  👉 Baixe e instale em: https://nodejs.org/

> A instalação do Node.js já inclui o `npm` (Node Package Manager)

Para verificar se a instalação foi concluída com sucesso, deve abrir o CMD e digitar o seguinte comando para ver a versão instalada:

```bash
node -v
npm -v
```

### 🚀 Executando o projeto frontend localmente

1. **Clone o repositório:**

```
git clone https://github.com/EJECT4UFRN/imperium_2024.git
```

2. **Acesse a pasta FRONT:**
   
   **A API do backend já está disponível remotamente, então não é necessário rodá-la localmente.**
   
   * Pode acessar diretamente pelo VS CODE, e abrir diretamente a página do FRONT
   * Ou pode abrir via cmd
     ```
     cd imperium_2024/FRONT
     ```
3. **Instale as dependências do projeto:**
   * Abra o terminal do VS CODE e digite o seguinte comando:
     ```
     npm install
     ```
     
   * Ainda no terminal, digite:
     ```
     npm install -g pnpm
     ```
     
   * E em seguida:
     ```
     pnpm install
     ```

   **Isso fará a instalação dos modulos do NODE**

4. **Rode o projeto VUE**
   ```
   pnpm run dev
   ```

    * No terminal, terá um retorno como esse.
      
  
    ```
    > front@0.0.0 dev
    > vite
    VITE v5.4.18  ready in 384 ms
  
    ➜  Local:   http://localhost:5173/
    ➜  Network: use --host to expose
    ➜  Vue DevTools: Open http://localhost:5173/__devtools__/ as a separate window
    ➜  Vue DevTools: Press Alt(⌥)+Shift(⇧)+D in App to toggle the Vue DevTools
    ➜  press h + enter to show help
  
    🌼   daisyUI 4.12.24
    ├─ ✔︎ 1 theme added              https://daisyui.com/docs/themes
    ╰─ ★ Star daisyUI on GitHub     https://github.com/saadeghi/daisyui
    ```  

    * Clice no link gerado em "Local" com o botão esquerdo do mouse + ctrl


5. **Acessando o projeto**
   
 * Ao acessar, irá diretamente para página HOME
 * Acesse o login de acordo com o perfil que deseja e bom teste :D
   
    * ADMIN
      - email: admin@example.com
      - senha: admin123
      - 
    * DOCTOR
      - email: camila.torres@clinicavital.com
      - senha: Med@2025!

    * RECEPTIONIST
        - email: joao.lima@clinicavital.com
        - senha: Recep@123
    
    * PATIENT
        - email: mariana.silva@gmail.com
        - senha: Paciente@2025
     
    * CLINIC
        - email: clinic@example.com
        - senha: clinic123
     
   



🧩 Tecnologias Utilizadas
Vue 3 + Vite

* TypeScript

* Tailwind CSS

* Pinia

* Vite

---

### 🚀 Executando a API Localmente — **Imperium 2024**

#### ⚙️ Pré-requisitos

- Python **≥ 3.12**
- (Opcional) Docker instalado na máquina

##### 🧪 Ambiente Local (sem Docker)

##### 1. Abra o terminal no diretório do projeto

Navegue até a pasta do backend:

```bash
cd imperium_2024/Backend/
```

##### 2. Crie e ative o ambiente virtual

**Criação:**

```bash
python3 -m venv venv
```

**Ativação:**

- **Windows**:

  ```bash
  .\venv\Scripts\activate
  ```

- **Linux/Mac**:

  ```bash
  source venv/bin/activate
  ```

##### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

##### 4. Configure o ambiente

Crie um arquivo `.env` na raiz do projeto e adicione:

```env
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = ""
EMAIL_PORT = ""
EMAIL_HOST = ""
```

##### 5. Realize as migrações

**Criar os arquivos de migração:**

```bash
python manage.py makemigrations
```

**Aplicar as migrações:**

```bash
python manage.py migrate
```

**Rode o script para criar os tipos de usuarios do sistema e o user ADMIN**:
```bash
python scripts/seed.py
```

o usuario admin criado possui as seguintes credenciais:

```txt
email: admin@example.com
senha: admin123
```

##### 6. Inicie o servidor

```bash
python manage.py runserver
```

##### ✅ Log Esperado

```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 25, 2025 - 22:38:20
Django version 4.2, using settings 'imperium.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

---

### 🐳 Executando com Docker (mais simples)

Caso tenha Docker instalado, basta criar o arquivo `.env`:

##### Configure o ambiente

Crie um arquivo `.env` na raiz do projeto e adicione:

```env
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = ""
EMAIL_PORT = ""
EMAIL_HOST = ""
```

e rodar os comandos abaixo no diretório raiz do projeto:

```bash
docker compose build && docker compose up
```

##### ✅ Log Esperado

```bash
docker compose build && docker compose up
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 33.5s (10/10) FINISHED                                      docker:default
 => [web internal] load build definition from dockerfile                           0.0s
 => => transferring dockerfile: 264B                                               0.0s
 => [web internal] load metadata for docker.io/library/python:3.12                 0.2s
 => [web internal] load .dockerignore                                              0.0s
 => => transferring context: 2B                                                    0.0s
 => [web 1/4] FROM docker.io/library/python:3.12@sha256:f282c100bbcd0db4346ba7261  0.0s
 => [web internal] load build context                                              0.0s
 => => transferring context: 8.11kB                                                0.0s
 => CACHED [web 2/4] WORKDIR /app                                                  0.0s
 => [web 3/4] COPY . .                                                             0.1s
 => [web 4/4] RUN pip install --no-cache-dir -r requirements.txt                  29.1s
 => [web] exporting to image                                                       3.9s 
 => => exporting layers                                                            3.8s 
 => => writing image sha256:309e3f221816fab3afb9bd64b2f4db5f7893ce95dfdf43ace0bae  0.0s 
 => => naming to docker.io/library/backend-web                                     0.0s 
 => [web] resolving provenance for metadata file                                   0.0s 
[+] Building 1/1                                                                        
 ✔ web  Built                                                                      0.0s 
[+] Running 2/2
 ✔ Network backend_default  Created                                                0.0s 
 ✔ Container backend-web-1  Created                                                0.1s 
Attaching to web-1
web-1  | Migrations for 'commom':
web-1  |   commom/migrations/0001_initial.py
web-1  |     - Create model Address
web-1  | Migrations for 'clinic':
web-1  |   clinic/migrations/0001_initial.py
web-1  |     - Create model Appointment
web-1  |     - Create model Clinic
web-1  |     - Create model MedicalRecord
web-1  |     - Create model Notification
web-1  |     - Create model Room
web-1  |     - Create model WaitingList
web-1  |     - Create model WorkingHours
web-1  |   clinic/migrations/0002_initial.py
web-1  |     - Add field user to workinghours
web-1  |     - Add field clinic to waitinglist
web-1  |     - Add field doctor to waitinglist
web-1  |     - Add field patient to waitinglist
web-1  |     - Add field clinic to room
web-1  |     - Add field user to notification
web-1  |     - Add field appointment to medicalrecord
web-1  |     - Add field address to clinic
web-1  |     - Add field admins_clinic to clinic
web-1  |     - Add field clinic to appointment
web-1  |     - Add field doctor to appointment
web-1  |     - Add field patient to appointment
web-1  |     - Add field room to appointment
web-1  |     - Alter unique_together for room (1 constraint(s))
web-1  | Migrations for 'users':
web-1  |   users/migrations/0001_initial.py
web-1  |     - Create model User
web-1  |     - Create model Expedient
web-1  |     - Create model Role
web-1  |     - Create model Tag
web-1  |     - Create model UserPolicies
web-1  |     - Create model UserSupport
web-1  |     - Create model Receptionist
web-1  |     - Create model Patient
web-1  |     - Create model FAQ
web-1  |     - Create model Doctor
web-1  |     - Create model Admin
web-1  |     - Add field expedient to user
web-1  |     - Add field groups to user
web-1  |     - Add field role to user
web-1  |     - Add field user_permissions to user
web-1  | Operations to perform:
web-1  |   Apply all migrations: admin, auth, clinic, commom, contenttypes, sessions, token_blacklist, users
web-1  | Running migrations:
web-1  |   Applying commom.0001_initial... OK
web-1  |   Applying clinic.0001_initial... OK
web-1  |   Applying contenttypes.0001_initial... OK
web-1  |   Applying contenttypes.0002_remove_content_type_name... OK
web-1  |   Applying auth.0001_initial... OK
web-1  |   Applying auth.0002_alter_permission_name_max_length... OK
web-1  |   Applying auth.0003_alter_user_email_max_length... OK
web-1  |   Applying auth.0004_alter_user_username_opts... OK
web-1  |   Applying auth.0005_alter_user_last_login_null... OK
web-1  |   Applying auth.0006_require_contenttypes_0002... OK
web-1  |   Applying auth.0007_alter_validators_add_error_messages... OK
web-1  |   Applying auth.0008_alter_user_username_max_length... OK
web-1  |   Applying auth.0009_alter_user_last_name_max_length... OK
web-1  |   Applying auth.0010_alter_group_name_max_length... OK
web-1  |   Applying auth.0011_update_proxy_permissions... OK
web-1  |   Applying auth.0012_alter_user_first_name_max_length... OK
web-1  |   Applying users.0001_initial... OK
web-1  |   Applying admin.0001_initial... OK
web-1  |   Applying admin.0002_logentry_remove_auto_add... OK
web-1  |   Applying admin.0003_logentry_add_action_flag_choices... OK
web-1  |   Applying clinic.0002_initial... OK
web-1  |   Applying sessions.0001_initial... OK
web-1  |   Applying token_blacklist.0001_initial... OK
web-1  |   Applying token_blacklist.0002_outstandingtoken_jti_hex... OK
web-1  |   Applying token_blacklist.0003_auto_20171017_2007... OK
web-1  |   Applying token_blacklist.0004_auto_20171017_2013... OK
web-1  |   Applying token_blacklist.0005_remove_outstandingtoken_jti... OK
web-1  |   Applying token_blacklist.0006_auto_20171017_2113... OK
web-1  |   Applying token_blacklist.0007_auto_20171017_2214... OK
web-1  |   Applying token_blacklist.0008_migrate_to_bigautofield... OK
web-1  |   Applying token_blacklist.0010_fix_migrate_to_bigautofield... OK
web-1  |   Applying token_blacklist.0011_linearizes_history... OK
web-1  |   Applying token_blacklist.0012_alter_outstandingtoken_user... OK
web-1  | Watching for file changes with StatReloader
web-1  | Performing system checks...
web-1  | 
web-1  | System check identified no issues (0 silenced).
web-1  | April 25, 2025 - 22:58:54
web-1  | Django version 4.2, using settings 'imperium.settings'
web-1  | Starting development server at http://0.0.0.0:8000/
web-1  | Quit the server with CONTROL-C.
```



