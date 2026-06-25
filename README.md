# Medical Equipment Manager

🏥 Sistema de gestión de equipos médicos e incidencias con autenticación JWT, bot de Telegram y deploy en Render.

**[Ver demo en vivo](https://medical-equipment-manager.onrender.com)**

## 🎯 Descripción

Aplicación full-stack para registrar, controlar y gestionar equipos médicos e incidencias en laboratorios o centros de salud. Incluye sistema de autenticación completo, notificaciones en tiempo real vía Telegram, y está completamente desplegada en la nube.

## ✨ Características

- **Autenticación JWT** — Tokens seguros de 8 horas
- **Registro y Login** — Sistema completo con validación
- **Recuperación de contraseña** — Reset vía email con token de 30 minutos
- **Bloqueo por intentos** — Protección contra ataques (3 intentos fallidos = bloqueo)
- **CRUD Completo** — Gestión total de equipos e incidencias
- **API REST** — Endpoints documentados y protegidos
- **Bot de Telegram** — Notificaciones automáticas al crear incidencias
- **Frontend responsivo** — Interfaz moderna con modales personalizados
- **Docker** — Containerizado para deployment consistente
- **Deploy automático** — CI/CD con GitHub + Render
- **Base de datos relacional** — SQLite (desarrollo) / PostgreSQL (producción)

## 🛠 Stack Técnico

**Backend:**
- Python 3.12+
- FastAPI
- SQLite / PostgreSQL
- JWT (PyJWT)
- bcrypt
- SMTP (Gmail)
- Requests (HTTP client)

**Frontend:**
- HTML5 + CSS3
- JavaScript vanilla
- LocalStorage para tokens

**DevOps:**
- Docker
- Render (hosting)
- GitHub (versionado)

## 📋 Requisitos

- Python 3.12+
- Docker (para desarrollo local)
- Cuenta de Gmail (para emails)
- Cuenta de Telegram Bot (para notificaciones)
- Git

## 🚀 Instalación y Setup Local

### 1. Clonar el repositorio

```bash
git clone https://github.com/edoardopg/medical-equipment-manager.git
cd medical-equipment-manager
```

### 2. Crear entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crea un archivo `.env` en la raíz:

```env
# JWT
SECRET_KEY=tu_clave_aleatoria_aqui
ALGORITHM=HS256

# Base de datos
DATABASE_URL=sqlite:///./medical.db

# Email (Gmail)
EMAIL_USER=tu_email@gmail.com
EMAIL_PASSWORD=tu_contraseña_app

# Telegram Bot
TELEGRAM_TOKEN=tu_token_bot_aqui
TELEGRAM_CHAT_ID=tu_chat_id_aqui

# Frontend
FRONTEND_URL=http://127.0.0.1:5500
```

**Para obtener credenciales:**

- **Gmail APP Password:** https://myaccount.google.com/apppasswords
- **Telegram TOKEN:** Habla con @BotFather en Telegram

### 5. Ejecutar la API

```bash
uvicorn api:app --reload
```

API disponible en `http://127.0.0.1:8000`

### 6. Abrir el frontend

Abre `frontend/login.html` con Live Server en VS Code.

## 🐳 Con Docker (Local)

### Construir la imagen

```bash
docker build -t medical-equipment-manager .
```

### Ejecutar el contenedor

```bash
docker run -p 8000:8000 medical-equipment-manager
```

## 🌐 Deploy en Render

### 1. Conectar GitHub a Render

1. Ve a https://render.com
2. Registrate con GitHub
3. Click en "New Web Service"
4. Selecciona este repositorio

### 2. Configurar el servicio

| Campo | Valor |
|-------|-------|
| Name | `medical-equipment-manager` |
| Environment | `Docker` |
| Branch | `main` |
| Start Command | `uvicorn api:app --host 0.0.0.0 --port 8000` |

### 3. Añadir variables de entorno

En la sección "Environment", añade:

```
SECRET_KEY=tu_clave_aqui
ALGORITHM=HS256
EMAIL_USER=tu_email@gmail.com
EMAIL_PASSWORD=tu_contraseña_app
TELEGRAM_TOKEN=tu_token_aqui
TELEGRAM_CHAT_ID=tu_chat_id_aqui
```

### 4. Deploy

Click en "Create Web Service" y Render desplegará automáticamente.

**Cada `git push` redeploya automáticamente.**

## 📂 Estructura del Proyecto

```
medical-equipment-manager/
├── crud/                      # Acceso a datos
│   ├── equipments.py
│   ├── incidents.py
│   └── users.py
│
├── routers/                   # Endpoints API
│   ├── equipments.py
│   ├── incidents.py
│   └── users.py
│
├── utils/                     # Funciones auxiliares
│   ├── security.py           # Hashing, tokens
│   ├── email.py              # Envío de emails
│   └── telegram.py           # Notificaciones Telegram
│
├── frontend/                  # Interfaz web
│   ├── login.html
│   ├── register.html
│   ├── forgot-password.html
│   ├── reset-password.html
│   └── index.html
│
├── database.py               # Configuración BD
├── models.py                 # Definición de tablas
├── api.py                    # App FastAPI
├── Dockerfile                # Configuración Docker
├── requirements.txt          # Dependencias Python
├── .env                      # Variables de entorno
└── README.md                 # Este archivo
```

## 🔑 Credenciales de Prueba

**Usuario admin (creado automáticamente):**
- Username: `admin`
- Password: `admin123`

## 📡 Endpoints API

### Autenticación

```
POST   /register              Crear nueva cuenta
POST   /login                 Iniciar sesión
POST   /forgot-password       Solicitar reset
POST   /reset-password        Actualizar contraseña
DELETE /delete-account        Eliminar cuenta
```

### Equipos (requieren JWT)

```
GET    /equipments            Listar todos
GET    /equipments/{id}       Obtener por ID
POST   /equipments            Crear nuevo
PUT    /equipments/{id}       Actualizar
DELETE /equipments/{id}       Eliminar
```

### Incidencias (requieren JWT)

```
GET    /incidents             Listar todas
GET    /incidents/{id}        Obtener por ID
POST   /incidents             Crear nueva
PUT    /incidents/{id}        Actualizar
DELETE /incidents/{id}        Eliminar
```

**Todas las peticiones requieren:**

```
Authorization: Bearer {token_jwt}
```

## 🔐 Autenticación

El token JWT se guarda automáticamente en `localStorage` tras login.

Token válido por **8 horas**. Al expirar, es necesario volver a logarse.

## 🤖 Bot de Telegram

Cuando se crea una incidencia, el bot envía automáticamente:

```
🚨 Nueva Incidencia Creada

📋 Equipo: FLUOROCYCLER
⚠️ Tipo de error: Sobrecalentamiento
📝 Descripción: El equipo alcanzó 95°C
```

## 🧪 Testing Manual

### 1. Registrarse

```bash
curl -X POST "http://localhost:8000/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "Test123!"
  }'
```

### 2. Login

```bash
curl -X POST "http://localhost:8000/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=admin123"
```

### 3. Obtener equipos (con token)

```bash
curl -H "Authorization: Bearer {token}" \
  "http://localhost:8000/equipments"
```

## 🚧 Próximas Mejoras

- [ ] Verificación de email al registrarse
- [ ] 2FA (Google Authenticator)
- [ ] Google OAuth login
- [ ] Roles de usuario (admin, técnico, viewer)
- [ ] Historial de cambios en equipos
- [ ] Exportar datos a Excel/PDF
- [ ] Panel de administración
- [ ] Tests unitarios
- [ ] PostgreSQL en producción
- [ ] Caché con Redis

## 🐛 Troubleshooting

### Error: "Token inválido"
- Token expiró (dura 8 horas)
- Solución: Vuelve a hacer login

### Email no llega
- EMAIL_PASSWORD sin espacios
- Es contraseña de aplicación de Gmail, no contraseña normal
- Revisa carpeta de spam

### Docker build falla
```bash
docker build --no-cache -t medical-equipment-manager .
```

### Base de datos vacía en Render
SQLite no persiste en Render. Próxima versión usará PostgreSQL.

## 📚 Documentación API (Swagger)

Una vez corriendo, accede a:

```
http://localhost:8000/docs
```

Swagger UI interactivo con todos los endpoints.

## 👤 Autor

**Edoardo** — Backend Developer en transición  
GitHub: [@edoardopg](https://github.com/edoardopg)

## 📄 Licencia

MIT License - ver [LICENSE](LICENSE) para detalles

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes, abre un issue primero.

---

**¿Preguntas?** Abre un [issue](https://github.com/edoardopg/medical-equipment-manager/issues) en GitHub.