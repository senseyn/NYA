# NYA

> High-performance content streaming and catalog platform

---

## Overview

NYA — платформа потоковой доставки медиаконтента, совмещающая видеохостинг и каталог (картотеку).  
Проект ориентирован на стабильность, контроль инфраструктуры и масштабируемость под высокий онлайн.

Система реализует единый доступ к контенту без перегруженного интерфейса и сторонних зависимостей.

---

## Core Features

- централизованный каталог контента
- потоковое воспроизведение (HLS)
- быстрый поиск и фильтрация
- минималистичный UI
- управление медиаданными
- масштабируемая backend-архитектура

---

## Tech Stack

**Frontend**
- React / Next.js
- TypeScript
- Tailwind / CSS Modules

**Backend**
- Node.js (NestJS / Express)
- REST API
- JWT Authentication

**Data Layer**
- PostgreSQL
- Redis

**Media Pipeline**
- FFmpeg (HLS segmentation)
- .m3u8 playlists
- .ts segments

**Infrastructure**
- Docker
- Nginx (reverse proxy + caching)
- CDN (planned)

---

## Architecture

```txt
Client (Browser)
        ↓
Frontend (React / Next.js)
        ↓
API Layer (Node.js)
        ↓
---------------------------------
| PostgreSQL | Redis | Media FS |
---------------------------------
        ↓
Nginx (cache / proxy / HLS delivery)
