# Medical Equipment Manager

Sistema de gestión de equipos médicos e incidencias con autenticación JWT y API REST.

## 🎯 Descripción

Aplicación full-stack para registrar, controlar y gestionar equipos médicos e incidencias en laboratorios o centros de salud. Incluye sistema de autenticación completo con login, registro, recuperación de contraseña y gestión de incidencias asociadas a equipos.

## ✨ Características

- **Autenticación JWT** — Login seguro con tokens de 8 horas
- **Sistema de registro** — Registro de nuevos usuarios con validación
- **Recuperación de contraseña** — Reset vía email con token de 30 minutos
- **Bloqueo por intentos** — Bloqueo después de 3 intentos fallidos
- **CRUD Completo** — Crear, leer, actualizar y eliminar equipos e incidencias
- **API REST** — Endpoints protegidos con autenticación
- **Frontend responsivo** — Interfaz moderna con modal personalizado
- **Base de datos relacional** — SQLite con 3 tablas (equipos, incidencias, usuarios)

## 🛠 Stack Técnico

**Backend:**
- Python 3.12+
- FastAPI
- SQLite
- JWT (PyJWT)
- bcrypt (hashing de contraseñas)
- SMTP (Gmail para emails)

**Frontend:**
- HTML5
- CSS3
- JavaScript vanilla
- LocalStorage para tokens

## 📋 Requisitos

- Python 3.12+
- pip
- Un email de Gmail (para reset de contraseña)

## 🚀 Instalación y Setup

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/P_1_Equipos_Medicos.git
cd P_1_Equipos_Medicos
```

### 2. Crear entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install fastapi uvicorn python-jose bcrypt python-dotenv python-multipart pydantic
```

### 4. Configurar variables de entorno
Crea un archivo `.env` en la raíz del proyecto:
```env
SECRET_KEY=long_secret_key_and_secure_change_this_in_production
ALGORITHM=HS256
DATABASE_URL=sqlite:///./medical.db
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=tu_email@gmail.com
EMAIL_PASSWORD=tu_contraseña_app
FRONTEND_URL=http://127.0.0.1:5500
```

**Para la contraseña de Gmail:**
1. Ve a https://myaccount.google.com/apppasswords
2. Selecciona Mail + tu dispositivo
3. Copia la contraseña de aplicación (sin espacios)

### 5. Ejecutar la API
```bash
uvicorn api:app --reload
```

La API estará disponible en `http://127.0.0.1:8000`

### 6. Abrir el frontend
1. Abre `frontend/index.html` con Live Server en VS Code
2. O manualmente en `http://127.0.0.1:5500/frontend/login.html`

## 📂 Estructura del Proyecto

```
P_1_Equipos_Medicos/
│
├── crud/                      # Lógica de base de datos
│   ├── equipments.py
│   ├── incidents.py
│   └── users.py
│
├── routers/                   # Endpoints de la API
│   ├── equipments.py
│   ├── incidents.py
│   └── users.py
│
├── utils/                     # Funciones auxiliares
│   ├── security.py           # Hashing y tokens
│   └── email.py              # Envío de emails
│
├── frontend/                  # Interfaz del usuario
│   ├── login.html
│   ├── register.html
│   ├── forgot-password.html
│   ├── reset-password.html
│   └── index.html
│
├── database.py               # Configuración de BD
├── models.py                 # Definición de tablas
├── api.py                    # Aplicación FastAPI
├── .env                      # Variables de entorno
├── .gitignore
└── README.md
```

## 🔑 Credenciales de Prueba

**Usuario admin (creado automáticamente):**
- Username: `admin`
- Password: `admin123`

## 📡 Endpoints API

### Autenticación
- `POST /register` — Registro de nuevo usuario
- `POST /login` — Login (devuelve JWT token)
- `POST /forgot-password` — Solicitar reset de contraseña
- `POST /reset-password` — Actualizar contraseña con token
- `DELETE /delete-account` — Eliminar cuenta (requiere token)

### Equipos (requieren JWT)
- `GET /equipments` — Listar todos los equipos
- `GET /equipments/{id}` — Obtener equipo por ID
- `POST /equipments` — Crear nuevo equipo
- `PUT /equipments/{id}` — Actualizar equipo
- `DELETE /equipments/{id}` — Eliminar equipo

### Incidencias (requieren JWT)
- `GET /incidents` — Listar todas las incidencias
- `GET /incidents/{id}` — Obtener incidencia por ID
- `POST /incidents` — Crear nueva incidencia
- `PUT /incidents/{id}` — Actualizar incidencia
- `DELETE /incidents/{id}` — Eliminar incidencia

## 🔐 Autenticación

Todos los endpoints de equipos e incidencias requieren un JWT token en el header:

```bash
curl -H "Authorization: Bearer TOKEN_AQUI" http://localhost:8000/equipments
```

El frontend maneja esto automáticamente guardando el token en `localStorage`.

## 🎨 Características de UI

- **Modal personalizado** para confirmaciones
- **Mensajes de error y éxito** visuales
- **Diseño responsive** con gradientes modernos
- **Protección de sesión** — Redirige a login si no hay token

## 🚧 Próximas mejoras

- [ ] Bot de Telegram para notificaciones
- [ ] Deploy en Render con PostgreSQL
- [ ] Panel de administración
- [ ] Exportar datos a Excel/PDF
- [ ] Historial de cambios en equipos
- [ ] Filtrado y búsqueda avanzada
- [ ] Roles de usuario (admin, técnico, viewer)

## 🐛 Troubleshooting

**Error CORS:**
- Verifica que el frontend esté en `http://127.0.0.1:5500`
- Asegúrate de que la API está corriendo en `http://127.0.0.1:8000`

**Email no llega:**
- Comprueba que `EMAIL_PASSWORD` no tiene espacios
- Verifica que es una contraseña de aplicación de Gmail, no tu contraseña normal
- Revisa la carpeta de spam

**Token expirado:**
- El token dura 8 horas
- Si expira, vuelve a hacer login

## 👤 Autor

Edoardo — Backend Developer en transición

## 📜 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.