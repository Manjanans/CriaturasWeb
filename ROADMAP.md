# CriaturasWeb - Roadmap de Desarrollo

> **Estado actual:** Autenticación completa + estructura base  
> **Fecha:** 31 Enero 2026

---

## ✅ Completado

- [x] Sistema de autenticación JWT (login, registro, logout)
- [x] Modelo `User` con bcrypt password hashing
- [x] Perfil de usuario con cambio de contraseña
- [x] Esquema de base de datos PostgreSQL definido (`sqlite_master.sql`)
- [x] Docker Compose con backend + frontend + PostgreSQL
- [x] UI base con tema de fantasía
- [x] Navegación básica (Criaturas, Batalla, Perfil)

---

## 🔴 Fase 1: Modelos y Base de Datos

### 1.1 Crear modelos SQLAlchemy para todas las entidades
Archivo: `app/models/criatura.py`

| Modelo | Campos principales | Notas |
|--------|-------------------|-------|
| `Criatura` | id, nombre, cantDados, tipoDado, vidaTotal, modificadorVida, cantEXP, publico, id_privado | FK a `usuarios.users` |
| `CriaturaStats` | claseArmadura, velocidad, fuerza, destreza, constitucion, inteligencia, sabiduria, carisma | FK a `Criatura` |
| `CriaturaDetalle` | tituloDetalle, descripcionDetalle, cantDados, tipoDado, modificadorAtaque, idTipoDesc | Para habilidades y acciones |

### 1.2 Modelos de catálogos (datos fijos)
Archivo: `app/models/catalogos.py`

| Modelo | Descripción |
|--------|-------------|
| `TipoSentido` | Visión Ciega, Visión Oscuridad, etc. |
| `TipoDesc` | Habilidad, Acción |
| `Caracteristica` | Fuerza, Destreza, Constitución, etc. |
| `Habilidad` | Acrobacias, Atletismo, Percepción, etc. |
| `TipoCondicion` | Asustado, Cegado, Paralizado, etc. |
| `TipoDanio` | Ácido, Fuego, Perforante, etc. |

### 1.3 Modelos de relaciones criatura-atributos
Archivo: `app/models/criatura_extras.py`

| Modelo | Descripción |
|--------|-------------|
| `SentidoCriatura` | Qué sentidos tiene y con qué alcance |
| `TiradaSalvacion` | Bonificadores de salvación por característica |
| `HabilidadCriatura` | Bonificadores de habilidades |
| `InmunidadCondicion` | Condiciones a las que es inmune |
| `Resistencia` | Resistencias/vulnerabilidades a tipos de daño |

### 1.4 Modelos de combate
Archivo: `app/models/combate.py`

| Modelo | Campos | Notas |
|--------|--------|-------|
| `Iniciativa` | id_usuario, nombre_criatura, valor_iniciativa, id_criatura, vida | Por usuario |
| `Turno` | id_usuario, num_turno | Tracker del turno actual |

---

## 🟠 Fase 2: Schemas Pydantic

### 2.1 Schemas de Criatura
Archivo: `app/schemas/criatura.py`

- `CriaturaBase` - Campos comunes
- `CriaturaCreate` - Para POST (incluye stats, detalles, etc.)
- `CriaturaUpdate` - Para PUT (campos opcionales)
- `CriaturaResponse` - Respuesta completa con todas las relaciones
- `CriaturaListItem` - Versión resumida para listados

### 2.2 Schemas de Combate
Archivo: `app/schemas/combate.py`

- `IniciativaCreate` - Agregar criatura al combate
- `IniciativaResponse` - Criatura en iniciativa con vida actual
- `TurnoUpdate` - Avanzar/retroceder turno

---

## 🟡 Fase 3: API de Criaturas

### 3.1 Endpoints CRUD básicos
Archivo: `app/api/criaturas/routes.py`

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/criaturas` | Listar criaturas (públicas + homebrew del usuario) |
| `GET` | `/criaturas/{id}` | Obtener criatura con todos sus detalles |
| `POST` | `/criaturas` | Crear nueva criatura (homebrew) |
| `PUT` | `/criaturas/{id}` | Actualizar criatura (solo owner) |
| `DELETE` | `/criaturas/{id}` | Eliminar criatura (solo owner) |

### 3.2 Endpoints auxiliares

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/criaturas/catalogos` | Obtener todos los catálogos (sentidos, habilidades, etc.) |
| `POST` | `/criaturas/{id}/duplicar` | Clonar una criatura pública como homebrew |
| `GET` | `/criaturas/buscar?q=` | Buscar criaturas por nombre |

---

## 🔵 Fase 4: API de Batallas

### 4.1 Endpoints de Iniciativa
Archivo: `app/api/batallas/routes.py`

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/batallas/iniciativa` | Obtener lista de iniciativa del usuario |
| `POST` | `/batallas/iniciativa` | Agregar criatura a la iniciativa |
| `PUT` | `/batallas/iniciativa/{nombre}` | Actualizar vida de criatura |
| `DELETE` | `/batallas/iniciativa/{nombre}` | Remover criatura de la iniciativa |
| `DELETE` | `/batallas/iniciativa` | Limpiar toda la iniciativa |

### 4.2 Endpoints de Turno

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/batallas/turno` | Obtener turno actual |
| `POST` | `/batallas/turno/siguiente` | Avanzar al siguiente turno |
| `POST` | `/batallas/turno/anterior` | Retroceder al turno anterior |
| `POST` | `/batallas/turno/reset` | Reiniciar a turno 1 |

### 4.3 Funcionalidades adicionales

- Ordenamiento automático por valor de iniciativa
- Persistencia de la batalla (no se pierde al cerrar navegador)
- Opción de tirar iniciativa automáticamente

---

## 🟣 Fase 5: Frontend - Vista de Criaturas

### 5.1 Componentes nuevos

| Componente | Descripción |
|------------|-------------|
| `Criaturas.vue` | Vista principal con lista de criaturas |
| `CriaturaCard.vue` | Tarjeta resumen de una criatura |
| `CriaturaForm.vue` | Formulario de creación/edición completo |
| `CriaturaDetalle.vue` | Vista detallada de una criatura |
| `StatsDisplay.vue` | Visualización de stats (FUE, DES, etc.) |

### 5.2 Funcionalidades UI

- Lista con filtros (públicas/homebrew, búsqueda)
- Modal o página de detalle completo
- Formulario paso a paso o con tabs:
  1. Info básica (nombre, vida, EXP)
  2. Stats (6 características + CA + velocidad)
  3. Sentidos y salvaciones
  4. Habilidades y acciones
  5. Resistencias e inmunidades
- Botón de duplicar criatura pública
- Indicador visual de público vs homebrew

---

## ⚫ Fase 6: Frontend - Vista de Batalla

### 6.1 Componentes nuevos

| Componente | Descripción |
|------------|-------------|
| `Batalla.vue` | Vista principal del tracker de combate |
| `IniciativaTracker.vue` | Lista ordenada de combatientes |
| `CombatanteCard.vue` | Tarjeta de criatura en combate (con vida) |
| `AddToBattle.vue` | Modal para agregar criaturas a la batalla |
| `DiceRoller.vue` | Tirador de dados integrado |

### 6.2 Funcionalidades UI

- Lista de iniciativa ordenada por valor
- Indicador visual del turno actual
- Controles de navegación de turno (anterior/siguiente)
- Barra de vida editable para cada combatiente
- Botón de agregar criatura (abre selector)
- Tirar iniciativa automáticamente (d20 + DEX)
- Botón de limpiar batalla
- Vista de detalle rápido de la criatura (modal)

---

## 🟤 Fase 7: Mejoras y Polish

### 7.1 UX/UI
- [ ] Animaciones de transición entre vistas
- [ ] Loading states para operaciones async
- [ ] Notificaciones toast para acciones (criatura creada, etc.)
- [ ] Modo oscuro/claro toggle
- [ ] Responsive design para móviles

### 7.2 Funcionalidades extra
- [ ] Exportar/Importar criaturas (JSON)
- [ ] Historial de batallas pasadas
- [ ] Notas por batalla
- [ ] Condiciones activas en criaturas (poisoned, stunned, etc.)
- [ ] Contador de concentración

### 7.3 Técnico
- [ ] Tests unitarios backend (pytest)
- [ ] Tests E2E frontend (Cypress/Playwright)
- [ ] CI/CD pipeline
- [ ] Logging estructurado
- [ ] Rate limiting

---

## 📋 Orden de Implementación Sugerido

```
Fase 1.1 → 1.2 → 1.3 → 1.4  (Modelos)
           ↓
Fase 2.1 → 2.2              (Schemas)
           ↓
Fase 3.1 → 3.2              (API Criaturas)
           ↓
Fase 5                       (Frontend Criaturas)
           ↓
Fase 4                       (API Batallas)
           ↓
Fase 6                       (Frontend Batalla)
           ↓
Fase 7                       (Polish)
```

---

## ⏱️ Estimación de Tiempo

| Fase | Estimación |
|------|------------|
| Fase 1 (Modelos) | 2-3 horas |
| Fase 2 (Schemas) | 1-2 horas |
| Fase 3 (API Criaturas) | 3-4 horas |
| Fase 4 (API Batallas) | 2-3 horas |
| Fase 5 (Frontend Criaturas) | 4-6 horas |
| Fase 6 (Frontend Batalla) | 4-6 horas |
| Fase 7 (Polish) | Variable |

**Total estimado MVP:** ~16-24 horas de desarrollo

---

> **Siguiente paso recomendado:** Comenzar con Fase 1.1 - Crear el modelo `Criatura` y sus relaciones básicas.
